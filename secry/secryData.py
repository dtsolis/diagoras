# synartiseis gia na trabaw dedomena apo tin basi dedomenwn

from diagoras.tei.models import *
from diagoras.tei.data import *
from django.db import connection, transaction
from django.utils import translation

def wildcardValue():
    return "--wildcard--"

# -------------------------
# secretary program courses
# -------------------------
def getSecryCoursesQueryString(iddepartment, course_id):
    var = "SELECT tei_courses_translate.courseType, tei_courses.active, tei_courses.idcourses, tei_courses_translate.title1,"
    var += "     tei_courses_translate.title2, tei_professors_translate.lastName, tei_professors_translate.name,"
    var += "     tei_courses_translate.knownObject, tei_courses.gradeScale, tei_courses_translate.teachPeriod, tei_courses.scolarships,"
    var += "     tei_courses.teachHours, tei_courses.cdm, tei_courses.replacedBy_id, tei_courses.didasketai, tei_courses.department_id"
    var += " FROM tei_courses"
    var += " INNER JOIN tei_courses_translate"
    var += "     ON tei_courses.idcourses=tei_courses_translate.courses_id AND tei_courses_translate.language='" + getLanguageLocale() +"'"
    var += " LEFT JOIN tei_professors"
    var += "     ON tei_courses.professors_id=tei_professors.idprofessors"
    var += " LEFT JOIN tei_professors_translate"
    var += "     ON tei_professors.idprofessors=tei_professors_translate.Professors_id AND tei_professors_translate.language='" + getLanguageLocale() +"'"
    var += " WHERE tei_courses.department_id=" + iddepartment
    if course_id != wildcardValue():
        var += " AND tei_courses.idcourses='" + course_id + "'"
    var += " ORDER BY tei_courses.idcourses, tei_courses_translate.title1;"
    print var
    return var

def getSecryCourses(iddepartment):
    var = getSecryCoursesQueryString(iddepartment, wildcardValue())
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getSingleSecryCourse(department_id, course_id):
    var = getSecryCoursesQueryString(department_id, course_id)
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows


# -------------------------
# secretary program classes
# -------------------------
def getSecryClassesQueryString(iddepartment, classlist_id):
    var = "SELECT tei_courses_translate.courseType, tei_classlist.active, tei_classlist.idclassList, tei_courses.idcourses, tei_classlist.academicYear,"
    var += "     tei_classlist_translate.classPeriod, tei_classlist_translate.title, tei_classlist.weeklyHours, tei_professors_translate.lastName,"
    var += "     tei_professors_translate.name, tei_classlist_translate.cstate, tei_classlist.totalStudents, tei_classlist.maxStudents, tei_courses.department_id"
    var += " FROM tei_classlist"
    var += " INNER JOIN tei_classlist_translate"
    var += "     ON tei_classlist.id=tei_classlist_translate.classlist_id AND tei_classlist_translate.language='" + getLanguageLocale() +"'"
    var += " INNER JOIN tei_courses"
    var += "     ON tei_classlist.courses_id=tei_courses.idcourses"
    var += " INNER JOIN tei_courses_translate"
    var += "     ON tei_courses.idcourses=tei_courses_translate.courses_id AND tei_courses_translate.language='" + getLanguageLocale() +"'"
    var += " LEFT JOIN tei_professors"
    var += "     ON tei_classlist.professors_id=tei_professors.idprofessors"
    var += " LEFT JOIN tei_professors_translate"
    var += "     ON tei_professors.idprofessors=tei_professors_translate.Professors_id AND tei_professors_translate.language='" + getLanguageLocale() +"'"
    var += " WHERE tei_courses.department_id=" + iddepartment
    if classlist_id != wildcardValue():
        var += "AND classlist.idclassList='" + classlist_id + "'"
    var += " ORDER BY tei_classlist.idclassList, tei_courses.idcourses, tei_classlist.academicYear, tei_classlist_translate.classPeriod, tei_classlist_translate.title;"
    
    return var

def getSecryClasses(iddepartment):
    var = getSecryClassesQueryString(iddepartment, wildcardValue())
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getSingleSecryClass(iddepartment, classlist_id):
    var = getSecryClassesQueryString(iddepartment, classlist_id)
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows


# -------------------------
# secretary program exams
# -------------------------
def getSecryExamsQueryString(iddepartment, exams_id):
    var = "SELECT tei_courses_translate.courseType, tei_courses.active, tei_courses.idcourses, tei_courses_translate.title1,"
    var += "     tei_courses_translate.description, tei_exams.academicYear, tei_exams.examsPeriod, tei_exams_has_courses.repeat,"
    var += "     tei_exams_has_courses.examDate, tei_professors_translate.lastName, tei_professors_translate.name,"
    var += "     tei_exams.idexams, tei_exams.department_id"
    var += " FROM tei_exams"
    var += " INNER JOIN tei_exams_has_courses"
    var += "     ON tei_exams.idexams=tei_exams_has_courses.exams_id"
    var += " INNER JOIN tei_courses"
    var += "     ON tei_exams_has_courses.courses_id=tei_courses.idcourses"
    var += " INNER JOIN tei_courses_translate"
    var += "     ON (tei_courses.idcourses=tei_courses_translate.courses_id AND tei_courses_translate.language='" + getLanguageLocale() +"')"
    var += " LEFT JOIN tei_professors"
    var += "     ON tei_courses.professors_id=tei_professors.idprofessors"
    var += " LEFT JOIN tei_professors_translate"
    var += "     ON (tei_professors.idprofessors=tei_professors_translate.Professors_id AND tei_professors_translate.language='" + getLanguageLocale() +"')"
    var += " WHERE tei_exams.department_id=" + iddepartment
    if exams_id != wildcardValue():
        var += " AND tei_exams.idexams=" + exams_id
    var += " ORDER BY tei_courses.idcourses, tei_courses_translate.title1"
    
    return var

def getSecryExams(iddepartment):
    var = getSecryExamsQueryString(iddepartment, wildcardValue())
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getSingleSecryExam(iddepartment, exams_id):
    var = getSecryExamsQueryString(iddepartment, exams_id)
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows


# -------------------------------------
# secretary program programList courses
# -------------------------------------
def getSecryProgList_CoursesQueryString(idprogList, courses_id):
    var = "SELECT tei_orientcourses_translate.orientationName, tei_courses_translate.courseType, tei_orientcourses.idorientCourses, tei_courses.active,"
    var += " tei_courses.idcourses, tei_courses_translate.title1, tei_courses_translate.knownObject, tei_orientcourses_has_courses_translate.selectionType,"
    var += " tei_courses.cdm, tei_courses.ects, tei_department_translate.depTitle, tei_courses.teachHours, tei_professors_translate.lastName,"
    var += " tei_professors_translate.name, tei_courses.validationPeriod, tei_orientcourses_has_proglist.progList_id"
    var += " FROM tei_courses"
    var += " INNER JOIN tei_courses_translate" 
    var += "     ON (tei_courses.idcourses=tei_courses_translate.courses_id AND tei_courses_translate.language='" + getLanguageLocale() +"')"
    var += " INNER JOIN tei_orientcourses_has_courses"
    var += "     ON tei_courses.idcourses=tei_orientcourses_has_courses.courses_id"
    var += " INNER JOIN tei_orientcourses_has_courses_translate"
    var += "     ON (tei_orientcourses_has_courses.id=tei_orientcourses_has_courses_translate.orientAndCourses_id AND tei_orientcourses_has_courses_translate.language='" + getLanguageLocale() +"')"
    var += " INNER JOIN tei_orientcourses"
    var += "     ON tei_orientcourses_has_courses.orientCourses_id=tei_orientcourses.idorientCourses"
    var += " INNER JOIN tei_orientcourses_translate"
    var += "     ON (tei_orientcourses.idorientCourses=tei_orientcourses_translate.orientcourses_id AND tei_orientcourses_translate.language='" + getLanguageLocale() +"')"
    var += " INNER JOIN tei_orientcourses_has_proglist"
    var += "     ON tei_orientcourses.idorientCourses=tei_orientcourses_has_proglist.orientCourses_id"
    var += " INNER JOIN tei_department_translate"
    var += "     ON (tei_courses.department_id=tei_department_translate.department_id AND tei_department_translate.language='" + getLanguageLocale() +"')"
    var += " LEFT JOIN tei_professors"
    var += "     ON tei_courses.professors_id=tei_professors.idprofessors"
    var += " LEFT JOIN tei_professors_translate"
    var += "     ON (tei_professors.idprofessors=tei_professors_translate.Professors_id AND tei_professors_translate.language='" + getLanguageLocale() +"')"
    var += " WHERE tei_orientcourses_has_proglist.progList_id=" + idprogList
    if courses_id != wildcardValue():
        var += " AND tei_courses.idcourses='" + courses_id + "'"
    var += " ORDER BY tei_orientcourses_translate.orientationName, tei_courses.idcourses, tei_courses_translate.title1;"
    #print var
    return var
    
def getSecryProgList_Courses(idprogList):
    var = getSecryProgList_CoursesQueryString(idprogList, wildcardValue())
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getSingleSecryProgList_Courses(idprogList, courses_id):
    var = getSecryProgList_CoursesQueryString(idprogList, courses_id)
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

# -------------------------------------
# secretary program professors
# -------------------------------------
def getSecryProfessors():
    var = "SELECT idprofessors, tei_professors_translate.title, tei_professors_translate.lastName, tei_professors_translate.name,"
    var += " tei_professors_translate.fatherName, tei_professors_translate.sex, tei_professors_translate.state,"
    var += " tei_professors.teaches, tei_professors.hireDate, tei_professors.email"
    var += " FROM tei_professors"
    var += " INNER JOIN tei_professors_translate"
    var += "     ON tei_professors.idprofessors=tei_professors_translate.Professors_id AND tei_professors_translate.language='" + getLanguageLocale() +"'"
    var += " ORDER BY tei_professors_translate.lastName, tei_professors_translate.name, tei_professors_translate.fatherName;"
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows
    

# -------------------------------------
# other functions
# -------------------------------------
def getMaxPlusOneKeyFromTable(pk, tableName):
    select = "max(" + pk + ")"
    var = "select " + select +" from " + tableName + ";"
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows[0][select]

def getSchoolList():
    var = "select school_id, title"
    var += " from tei_school_translate"
    var += " where language='" + getLanguageLocale() + "'"
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getDepartmentList():
    var = "select department_id, depTitle"
    var += " from tei_department_translate"
    var += " where language='" + getLanguageLocale() + "'"
    var += " order by depTitle;"
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getProfessorsList():
    var = "select Professors_id, lastName, name"
    var += " from tei_professors_translate"
    var += " where language='" + getLanguageLocale() + "'"
    var += " order by lastName, name;"
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getCurriculumList(department_id):
    var = "select idprogList, progTitle"
    var += " from tei_proglist"
    var += " inner join tei_proglist_translate"
    var += "     on tei_proglist.idprogList=tei_proglist_translate.proglist_id and tei_proglist_translate.language='" + getLanguageLocale() + "'"
    var += "where department_id=" + department_id + " and tei_proglist.active=1"
    var += " order by progTitle;"
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getCourseListFromDepartment(department_id):
    var = "select idcourses, title1"
    var += " from tei_courses"
    var += " inner join tei_courses_translate"
    var += "     on tei_courses.idcourses=tei_courses_translate.courses_id and language='" + getLanguageLocale() + "'"
    var += "where department_id=" + department_id
    var += " order by title1;"
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getParentCourseList(orientation_id):
    var = "select tei_courses_translate.courses_id, tei_courses_translate.title1"
    var += " from tei_courses"
    var += " inner join tei_courses_translate"
    var += "     on tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='" + getLanguageLocale() + "'"
    var += " inner join tei_orientcourses_has_courses"
    var += "     on tei_courses.idcourses=tei_orientcourses_has_courses.courses_id and orientCourses_id=" + str(orientation_id)
    var += " where tei_courses.parentCourse_id is null or tei_courses.parentCourse_id=''"
    var += " order by tei_courses_translate.title1;"
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getOrientcoursesList(proglist_id):
    var = "select tei_orientcourses_translate.orientcourses_id, tei_orientcourses_translate.orientationName"
    var += " from tei_orientcourses"
    var += " inner join tei_orientcourses_translate"
    var += "     on tei_orientcourses.idorientCourses=tei_orientcourses_translate.orientcourses_id"
    var += " inner join tei_orientcourses_has_proglist"
    var += "     on tei_orientcourses_translate.orientcourses_id=tei_orientcourses_has_proglist.orientCourses_id and tei_orientcourses_translate.language='" + getLanguageLocale() + "'"
    var += " where tei_orientcourses_has_proglist.progList_id=" + str(proglist_id) + " and tei_orientcourses.active=1"
    var += " order by tei_orientcourses_translate.orientationName;"

    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getCourseStatusList():
    var = "select id, status from tei_course_settings_translate;"
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def courseIdAvailable(course_id):
    available = False
    try:
        a = Courses.objects.get(pk=course_id)
    except Exception,e:
        print e
        available = True
    print available
    return available

# -------------------------------------
# get single entry info
# -------------------------------------
def getClassInfo(classlist_id):
    var = "select idclassList, active, academicYear, weeklyHours, courses_id, department_id, professors_id, totalStudents, maxStudents,"
    var += " classPeriod, title, language, cstate"
    var += " from tei_classlist"
    var += " inner join tei_classlist_translate"
    var += "     on tei_classlist.id=tei_classlist_translate.classlist_id"
    var += " where idclassList = '" + classlist_id + "'"
    var += "order by language;"
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows

def getProglistInfo(proglist_id):
    var = "select tei_proglist.idprogList, tei_proglist.active, tei_proglist.fee, tei_proglist.semestersNum, tei_proglist_translate.studyLevel," 
    var += " tei_proglist_translate.progTitle, tei_proglist_translate.diplomaTitle, tei_proglist_translate.id, tei_proglist.department_id"
    var += " from tei_proglist"
    var += " left join tei_proglist_translate"
    var += "     on tei_proglist.idprogList=tei_proglist_translate.proglist_id"
    var += " where tei_proglist.idprogList=" + proglist_id +";"
    
    cursor = connection.cursor()
    cursor.execute(var)
    rows = dictfetchall(cursor)
    
    return rows





# -------------------------------------
# adding data into tables
# -------------------------------------
class SecryDataController:
    # schools
    # -------------------------------------
    @staticmethod
    def addSchool(institution_id):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tei_school (idschool, institution_id) VALUES (IFNULL((select max(idschool) from tei_school), 0)+1, "+institution_id+");")
        transaction.commit_unless_managed()
    
    @staticmethod
    def addSchoolTranslate(title, language, school_id):
        isDefault = '0'
        if school_id == 'lastEntry':
            school_id = "(select max(idschool) from tei_school)"
        if language == 'el_GR':
            isDefault = '1'
            
        var = "INSERT INTO tei_school_translate (title, language, isDefault, school_id)"
        var += " VALUES ('" + title + "', '" + language + "', " + isDefault + ", " + school_id + ");"
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()
        
    # departments
    # -------------------------------------
    @staticmethod
    def addDepartment(email, website, school_id):
        var = "INSERT INTO tei_department (iddepartment, email, website, school_id)"
        var += " VALUES (IFNULL((select max(iddepartment) from tei_department), 0)+1, '" + email + "', '" + website + "', " + school_id + ");"
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()
    
    @staticmethod
    def addDepartmentTranslate(depTitle, director, studylevel, language, department_id):
        isDefault = '0'
        if department_id == 'lastEntry':
            department_id = "(select max(iddepartment) from tei_department)"
        if language == 'el_GR':
            isDefault = '1'
        var = "INSERT INTO tei_department_translate (depTitle, director, studyLevel, language, isDefault, department_id)"
        var += " VALUES ('" + depTitle + "', '" + director + "', '" + studylevel + "', '" + language + "', " + isDefault + ", " + department_id +");"
        
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()
        
    # curriculum
    # -------------------------------------
    @staticmethod
    def addProglist(active, fee, semestersNum, department_id):
        var = "INSERT INTO tei_proglist (idprogList, active, fee, semestersNum, department_id)"
        var += " VALUES (IFNULL((select max(idprogList) from tei_proglist), 0)+1, " + active + ", " + fee + ", " + semestersNum + ", " + department_id + ");"
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()
    
    @staticmethod
    def addProglistTranslate(studyLevel, progTitle, diplomaTitle, language, proglist_id):
        isDefault = '0'
        if proglist_id == 'lastEntry':
            proglist_id = "(select max(idprogList) from tei_proglist)"
        if language == 'el_GR':
            isDefault = '1'
        
        var = "INSERT INTO tei_proglist_translate (studyLevel, progTitle, diplomaTitle, language, isDefault, proglist_id)"
        var += " VALUES ('"+studyLevel+"', '"+progTitle+"', '"+diplomaTitle+"', '"+language+"', "+isDefault+", "+proglist_id+");"
        
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()
    
    @staticmethod
    def updateProglist(curriculmID, active, fee, semesters, department_id, studyLevel_gr, title_gr, diplomaTitle_gr, studyLevel_en, title_en, diplomaTitle_en):
        a = ProgList.objects.get(pk=curriculmID)
        if active == '1':
            a.active = True
        else:
            a.active = False
        if fee == '1':
            a.fee = True
        else:
            a.fee = False
        a.semestersNum = semesters
        a.save()
        
        b = ProgList_Translate.objects.get(proglist=a.idprogList, language='el_GR')
        b.studyLevel = studyLevel_gr
        b.progTitle = title_gr
        b.diplomaTitle = diplomaTitle_gr
        b.save()
        
        c = ProgList_Translate.objects.get(proglist=a.idprogList, language='en_US')
        c.studyLevel = studyLevel_en
        c.progTitle = title_en
        c.diplomaTitle = diplomaTitle_en
        c.save()


    # orientation
    # -------------------------------------
    @staticmethod
    def addOrientation(active, diplomaOrient, department_id, progList_id):
        cursor = connection.cursor()
        
        var = "INSERT INTO tei_orientcourses (active, diplomaOrient, department_id)"
        var += " VALUES (" + active + ", " + diplomaOrient + ", " + department_id + ");"
        cursor.execute(var)
        transaction.commit_unless_managed()

        var = "INSERT INTO tei_orientcourses_has_proglist (orientCourses_id, progList_id) VALUES ((select max(idorientCourses) from tei_orientcourses), " + progList_id +");"
        cursor.execute(var)
        transaction.commit_unless_managed()

    @staticmethod
    def addOrientationTranslate(orientationName, language, orientcourses_id):
        isDefault = '0'
        if orientcourses_id == 'lastEntry':
            orientcourses_id = "(select max(idorientCourses) from tei_orientcourses)"
        if language == 'el_GR':
            isDefault = '1'

        var = "INSERT INTO tei_orientcourses_translate (orientationName, language, isDefault, orientcourses_id)"
        var += " VALUES ('" + orientationName +"', '" + language +"', " + isDefault +", " + orientcourses_id +");"
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()

    # courses
    # -------------------------------------
    @staticmethod
    def addCourse(idcourses, active, gradeScale, semester, scolarships, teachHours, cdm, ects, didasketai, status, department_id, professors_id, replacedBy_id, parentCourse_id, validationPeriod, orientcourses_id):
        if professors_id != "null":
            professors_id = "'"+professors_id+"'"
        if replacedBy_id != "null":
            replacedBy_id = "'"+replacedBy_id+"'"
        if parentCourse_id != "null":
            parentCourse_id = "'"+parentCourse_id+"'"
        cursor = connection.cursor()

        var = "INSERT INTO tei_courses (idcourses, active, gradeScale, semester, scolarships, teachHours, cdm, ects, didasketai, department_id, professors_id, replacedBy_id, parentCourse_id, validationPeriod)"
        var += " VALUES ('"+idcourses+"', "+active+", '"+gradeScale+"', "+semester+", "+scolarships+", "+teachHours+", '"+cdm+"', '"+ects+"', "+didasketai+", "+department_id+", "+professors_id+", "+replacedBy_id+", "+parentCourse_id+", '"+validationPeriod+"');"
        
        cursor.execute(var)
        transaction.commit_unless_managed()
        
        var = "INSERT INTO tei_orientcourses_has_courses (orientCourses_id, courses_id, status_id) VALUES (" + orientcourses_id + ", '" + idcourses + "', " + status + ");"
        cursor.execute(var)
        transaction.commit_unless_managed()

    @staticmethod
    def addCourseTranslate(idcourses, courseType, title1, title2, knownObject, teachPeriod, description, goals, language, selectionType, orientAndCourses_id):
        isDefault = '0'
        if orientAndCourses_id == 'lastEntry':
            orientAndCourses_id = "(select max(id) from tei_orientcourses_has_courses)"
        if language == 'el_GR':
            isDefault = '1'

        if knownObject != "null":
            knownObject = "'"+knownObject+"'"
        if goals != "null":
            goals = "'"+goals+"'"

        cursor = connection.cursor()
        
        var = "INSERT INTO tei_courses_translate (courseType, title1, title2, knownObject, teachPeriod, description, goals, language, isDefault, courses_id)"
        var += " VALUES ('"+courseType+"', '"+title1+"', '"+title2+"', "+knownObject+", '"+teachPeriod+"', '"+description+"', "+goals+", '"+language+"', "+isDefault+", '"+idcourses+"');"
        cursor.execute(var)
        transaction.commit_unless_managed()
        
        var = "INSERT INTO tei_orientcourses_has_courses_translate (selectionType, language, isDefault, orientAndCourses_id)"
        var += " VALUES ('"+selectionType+"', '"+language+"', "+isDefault+", "+orientAndCourses_id+");"
        cursor.execute(var)
        transaction.commit_unless_managed()
        

    # bibliography
    # -------------------------------------
    @staticmethod
    def addBibliography(author, title, editor, pubYear, course_id):
        var = "INSERT INTO tei_bibliography (author, bititle, editor, pubYear, course_id)"
        var += " VALUES ('" + author + "', '" + title + "', '" + editor + "', '" + pubYear + "', '" + course_id + "');"
        
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()

    # professors
    # -------------------------------------
    @staticmethod
    def addProfessor(teaches, email, hireDate, institution_id):
        var = "INSERT INTO tei_professors (idprofessors, teaches, email, hireDate, institution_id)"
        var += " VALUES (IFNULL((select max(idprofessors) from tei_professors), 0)+1, " + teaches + ", '" + email + "', '" + hireDate + "', " + institution_id + ");"
        print var
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()

    @staticmethod
    def addProfessorTranslate(title, name, lastName, fatherName, sex, state, language, professors_id):
        isDefault = '0'
        if professors_id == 'lastEntry':
            professors_id = "(select max(idprofessors) from tei_professors)"
        if language == 'el_GR':
            isDefault = '1'
        
        var = "INSERT INTO tei_professors_translate (id, title, name, lastName, sex, state, language, isDefault, Professors_id, fatherName)"
        var += " VALUES (IFNULL((select max(idprofessors) from tei_professors), 0)+1, '"+title+"', '"+name+"', '"+lastName+"', '"+sex+"', '"+state+"', '"+language+"', "+isDefault+", "+professors_id+", '"+fatherName+"');"
        print var
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()

    # classlist
    # -------------------------------------
    @staticmethod
    def addClasslist(idclassList, active, academicYear, weeklyHours, course_id, department_id, professors_id, totalStudents, maxStudents):
        var = "INSERT INTO tei_classlist (id, idclassList, active, academicYear, weeklyHours, courses_id, department_id, professors_id, totalStudents, maxStudents)"
        var += " VALUES (IFNULL((select max(id) from tei_classlist), 0)+1, '"+idclassList+"', "+active+", '"+academicYear+"', "+weeklyHours+", '"+course_id+"', "+department_id+", "+professors_id+", "+totalStudents+", "+maxStudents+");"
        
        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()

    @staticmethod
    def addClasslistTranslate(classPeriod, title, language, classlist_id, cstate):
        isDefault = '0'
        if classlist_id == 'lastEntry':
            classlist_id = "(select max(id) from tei_classlist)"
        if language == 'el_GR':
            isDefault = '1'

        var = "INSERT INTO tei_classlist_translate (id, classPeriod, title, language, isDefault, classlist_id, cstate)"
        var += " VALUES (IFNULL((select max(id) from tei_classlist_translate), 0)+1, '"+classPeriod+"', '"+title+"', '"+language+"', "+isDefault+", "+classlist_id+", '"+cstate+"');"

        cursor = connection.cursor()
        cursor.execute(var)
        transaction.commit_unless_managed()

    # exams
    # -------------------------------------
    @staticmethod
    def addExam(academicYear, examsPeriod, repeat, examDate, department_id, courses_id):
        cursor = connection.cursor()
        
        var = "INSERT INTO tei_exams (idexams, academicYear, examsPeriod, department_id)"
        var += " VALUES (IFNULL((select max(idexams) from tei_exams), 0)+1, '"+academicYear+"', '"+examsPeriod+"', "+department_id+");"
        cursor.execute(var)
        transaction.commit_unless_managed()

        var = "INSERT INTO tei_exams_has_courses (exams_id, courses_id, repeat, examDate)"
        var += " VALUES ((select max(idexams) from tei_exams), '"+courses_id+"', "+repeat+", '"+examDate+"');"
        cursor.execute(var)
        transaction.commit_unless_managed()





        
        