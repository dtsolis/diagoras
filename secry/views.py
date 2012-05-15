from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.contrib import auth

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from diagoras.extras.data import *
from diagoras.tei.data import getProgramListActiveOrNot, getProgramListActiveOrNot
from diagoras.secry.secryData import *
import urllib


def is_user(user):
    return user.is_authenticated()

def is_user_superuser(user):
    return user.is_superuser

#---- @user_passes_test(...) ----
# Se kathe synartisi gia na empodizei kapoion "anonymo" na syndeetai se aytes tis selides
# 
# mode:
#    sProgList --> main page programmatos grammateias
#    spCourses --> mathimata ana programma spoudwn
#    sCourses  --> mathimata ana tmima
#    sClasses  --> takseis ana tmima
#    sExams    --> eksetaseis ana tmima

@user_passes_test(is_user_superuser, login_url="/login/")
def viewSecryProgram(request):
    mode = "sProgList"
    d = getProgramListActiveOrNot()
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def coursesForProglist(request, proglist_id):
    mode = "spCourses"
    d = getProgramListActiveOrNot()
    tableData = getSecryProgList_Courses(proglist_id)
    
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'tableData':tableData, 'proglist_id':proglist_id}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def secryCourses(request, department_id):
    mode = "sCourses"
    d = getProgramListActiveOrNot()
    tableData = getSecryCourses(department_id)
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def secryClasses(request, department_id):
    mode = "sClasses"
    d = getProgramListActiveOrNot()
    tableData = getSecryClasses(department_id)
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def secryExams(request, department_id):
    mode = "sExams"
    d = getProgramListActiveOrNot()
    tableData = getSecryExams(department_id)
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def secryProfessors(request):
    mode = "sProfessors"
    d = getProgramListActiveOrNot()
    tableData = getSecryProfessors()
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))


# ----------------------
# edit functions
# ----------------------
@user_passes_test(is_user_superuser, login_url="/login/")
def editCoursesForProglist(request, proglist_id, courses_id):
    mode = "spCourses"
    d = getProgramListActiveOrNot()
    tableData = getSingleSecryProgList_Courses(proglist_id, courses_id)
    
    return render_to_response('secry/secry_edit.html', {'progList':d, 'editMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def editSecryCourses(request, department_id, courses_id):
    mode = "sCourses"
    d = getProgramListActiveOrNot()
    tableData = getSingleSecryCourses(department_id, courses_id)
    return render_to_response('secry/secry_edit.html', {'progList':d, 'editMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def editSecryClasses(request, department_id, classlist_id):
    mode = "aClasses"
    edit = True
    departments = getDepartmentList()
    classInf = getClassInfo(classlist_id)
    print classInf
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments, 'performEdit':edit, 'classInfo':classInf}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def editSecryExams(request, department_id, exams_id):
    mode = "sExams"
    d = getProgramListActiveOrNot()
    tableData = getSingleSecryExams(department_id, exams_id)
    return render_to_response('secry/secry_edit.html', {'progList':d, 'editMode':mode, 'tableData':tableData}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def editSecryProfessors(request, professor_id):
    mode = "sProfessor"
    d = getProgramListActiveOrNot()
    return render_to_response('secry/secry_edit.html', {'progList':d, 'editMode':mode}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def editProglist(request, proglist_id):
    mode = "aProglist"
    edit = True
    departments = getDepartmentList()
    info = getProglistInfo(proglist_id)
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments, 'performEdit':edit, 'currInfo':info}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def editOrientation(request, orient_id):
    mode = "aOrientation"
    edit = True
    departments = getDepartmentList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments, 'performEdit':edit}, context_instance = RequestContext(request))


# ----------------------
# add functions
# ----------------------
@user_passes_test(is_user_superuser, login_url="/login/")
def addSecrySchool(request):
    mode = "aSchool"
    return render_to_response('secry/secry_add.html', {'addMode':mode}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryDepartment(request):
    mode = "aDepartment"
    schools = getSchoolList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'schools':schools}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryProglist(request):
    mode = "aProglist"
    departments = getDepartmentList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryOrientation(request):
    mode = "aOrientation"
    departments = getDepartmentList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryCourses(request):
    mode = "aCourses"
    departments = getDepartmentList()
    prof = getProfessorsList()
    statuses = getCourseStatusList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments, 'professors':prof, 'statuslist':statuses}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryBibliography(request):
    mode = "aBibliography"
    departments = getDepartmentList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryProfessor(request):
    mode = "aProfessor"
    return render_to_response('secry/secry_add.html', {'addMode':mode}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryClasses(request):
    mode = "aClasses"
    departments = getDepartmentList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addSecryExams(request):
    mode = "aExams"
    departments = getDepartmentList()
    return render_to_response('secry/secry_add.html', {'addMode':mode, 'departments':departments}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def performUpdate(request):
    if request.method == "POST":
        if 'addMode' not in request.POST:
            return
        elif request.POST['addMode'] == 'aProglist':
            active = '0'
            fee = '0'
            if 'active' in request.POST:
                active = '1'
            if 'fee' in request.POST:
                fee = '1'
            
            SecryDataController.updateProglist(request.POST['curriculmID'], active, fee, request.POST['semesters'], request.POST['department_id'], request.POST['studyLevel_gr'], request.POST['title_gr'], request.POST['diplomaTitle_gr'], request.POST['studyLevel_en'], request.POST['title_en'], request.POST['diplomaTitle_en'])    
            print 'update proglist'
        elif request.POST['addMode'] == 'aOrientation':
            print 'update orient'
            
            
    mode = "sProgList"
    message = "success!"
    d = getProgramListActiveOrNot()
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'okmessage':message}, context_instance = RequestContext(request))


@user_passes_test(is_user_superuser, login_url="/login/")
def performAdd(request):
    if request.method == "POST":
        if 'addMode' not in request.POST:
            return
        elif request.POST['addMode'] == 'aSchool':
            SecryDataController.addSchool('1')
            SecryDataController.addSchoolTranslate(request.POST['title_gr'], 'el_GR', 'lastEntry')
            SecryDataController.addSchoolTranslate(request.POST['title_en'], 'en_US', 'lastEntry')
            
        elif request.POST['addMode'] == 'aDepartment':
            SecryDataController.addDepartment(request.POST['email'], request.POST['website'], request.POST['school_id'])
            SecryDataController.addDepartmentTranslate(request.POST['title_gr'], request.POST['director_gr'], request.POST['studyLevel_gr'], 'el_GR', 'lastEntry')
            SecryDataController.addDepartmentTranslate(request.POST['title_en'], request.POST['director_en'], request.POST['studyLevel_en'], 'en_US', 'lastEntry')
        
        elif request.POST['addMode'] == 'aProglist':
            active = '0'
            fee = '0'
            if 'active' in request.POST:
                active = '1'
            if 'fee' in request.POST:
                fee = '1'
            SecryDataController.addProglist(active, fee, request.POST['semesters'], request.POST['department_id'])
            SecryDataController.addProglistTranslate(request.POST['studyLevel_gr'], request.POST['title_gr'], request.POST['diplomaTitle_gr'], 'el_GR', 'lastEntry')
            SecryDataController.addProglistTranslate(request.POST['studyLevel_en'], request.POST['title_en'], request.POST['diplomaTitle_en'], 'en_US', 'lastEntry')
            
        elif request.POST['addMode'] == 'aOrientation':
            active = '0'
            diplomaOrient = '0'
            if 'active' in request.POST:
                active = '1'
            if 'diplomaOrient' in request.POST:
                diplomaOrient = '1'
            orientationName_gr = request.POST['title_gr']
            orientationName_en = request.POST['title_en']
            SecryDataController.addOrientation(active, diplomaOrient, request.POST['department_id'], request.POST['proglist_id'])
            SecryDataController.addOrientationTranslate(orientationName_gr, 'el_GR', 'lastEntry')
            SecryDataController.addOrientationTranslate(orientationName_en, 'en_US', 'lastEntry')
                
        elif request.POST['addMode'] == 'aCourses':
            active = '0'
            didasketai = '0'
            scolarships = '0'
            professors_id = 'null'
            replacedBy_id = 'null'
            parentCourse_id = 'null'
            if 'active' in request.POST:
                active = '1'
            if 'didasketai' in request.POST:
                didasketai = '1'
            if 'scolarships' in request.POST:
                scolarships = '1'
            if 'professors_id' in request.POST:
                professors_id = request.POST['professors_id']
            if 'replacedBy_id' in request.POST:
                replacedBy_id = request.POST['replacedBy_id']
            if 'parentCourse_id' in request.POST:
                parentCourse_id = request.POST['parentCourse_id']
            SecryDataController.addCourse(request.POST['idcourses'], active, request.POST['gradeScale'], request.POST['semester'], scolarships, request.POST['teachHours'], request.POST['cdm'], request.POST['ects'], didasketai, request.POST['status_id'], request.POST['department_id'], professors_id, replacedBy_id, parentCourse_id, request.POST['validationPeriod'], request.POST['orientcourses_id'])

            SecryDataController.addCourseTranslate(request.POST['idcourses'], request.POST['courseType_gr'], request.POST['title1_gr'], request.POST['title2_gr'], request.POST['knownObject_gr'], request.POST['teachPeriod_gr'], request.POST['description_gr'], request.POST['goals_gr'], 'el_GR', request.POST['selectionType_gr'], 'lastEntry')

            SecryDataController.addCourseTranslate(request.POST['idcourses'], request.POST['courseType_en'], request.POST['title1_en'], request.POST['title2_en'], request.POST['knownObject_en'], request.POST['teachPeriod_en'], request.POST['description_en'], request.POST['goals_en'], 'en_US', request.POST['selectionType_en'], 'lastEntry')
            
        elif request.POST['addMode'] == 'aBibliography':
            SecryDataController.addBibliography(request.POST['author'], request.POST['title'], request.POST['editor'], request.POST['pubYear'] + "-1-1", request.POST['course_id'])

        elif request.POST['addMode'] == 'aProfessor':
            teaches  = '0'
            if 'teaches' in request.POST:
                teaches = '1'
            print "profs"
            SecryDataController.addProfessor(teaches, request.POST['email'], request.POST['hireDate'], '1')
            SecryDataController.addProfessorTranslate(request.POST['title_gr'], request.POST['name_gr'], request.POST['lastname_gr'], request.POST['fatherName_gr'], request.POST['sex_gr'], request.POST['state_gr'], 'el_GR', 'lastEntry')
            SecryDataController.addProfessorTranslate(request.POST['title_en'], request.POST['name_en'], request.POST['lastname_en'], request.POST['fatherName_en'], request.POST['sex_en'], request.POST['state_en'], 'en_US', 'lastEntry')

        elif request.POST['addMode'] == 'aClasses':
            active = '0'
            professors_id = "'null'"
            if 'active' in request.POST:
                active = '1'
            if 'professors_id' in request.POST:
                professors_id = request.POST['professors_id']
            SecryDataController.addClasslist(request.POST['idclassList'], active, request.POST['academicYear'], request.POST['weeklyHours'], request.POST['course_id'], request.POST['department_id'], professors_id, request.POST['totalStudents'], request.POST['maxStudents'])
            SecryDataController.addClasslistTranslate(request.POST['classPeriod_gr'], request.POST['title_gr'], 'el_GR', 'lastEntry', request.POST['cstate_gr'])

            SecryDataController.addClasslistTranslate(request.POST['classPeriod_en'], request.POST['title_en'], 'en_US', 'lastEntry', request.POST['cstate_en'])

        elif request.POST['addMode'] == 'aExams':
            repeat = '0'
            if 'repeat' in request.POST:
                repeat = '1'
            SecryDataController.addExam(request.POST['academicYear'], request.POST['examsPeriod'], repeat, request.POST['examDate'], request.POST['department_id'], request.POST['course_id'])
        
        
    mode = "sProgList"
    message = "success!"
    d = getProgramListActiveOrNot()
    return render_to_response('secry/secry.html', {'progList':d, 'tableDataMode':mode, 'okmessage':message}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxCurriculum(request, department_id):
    list = getCurriculumList(department_id)
    var = "<option value=\"-1\">Select</option>"
    for i in xrange(len(list)):
        var += "<option value=\"" + str(list[i]['idprogList']) + "\">" + list[i]['progTitle'] + "</option>"
    print var
    return render_to_response('secry/pureHTMLString.html', {'htmlString':var}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxOrientation(request, proglist_id):
    print "ajax"
    list = getOrientcoursesList(proglist_id)
    var = "<option value=\"-1\">Select</option>"
    for i in xrange(len(list)):
        var += "<option value=\"" + str(list[i]['orientcourses_id']) + "\">" + list[i]['orientationName'] + "</option>"
    print var
    return render_to_response('secry/pureHTMLString.html', {'htmlString':var}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxCourses(request, department_id):
    list = getCourseListFromDepartment(department_id)
    var = "<option value=\"-1\">Select</option>"
    for i in xrange(len(list)):
        var += "<option value=\"" + list[i]['idcourses'] + "\">" + list[i]['title1'] + "</option>"
    
    return render_to_response('secry/pureHTMLString.html', {'htmlString':var}, context_instance = RequestContext(request))


@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxParentCourses(request, orientation_id):
    list = getParentCourseList(orientation_id)
    var = "<option value=\"null\">Select</option>"
    for i in xrange(len(list)):
        var += "<option value=\"" + list[i]['courses_id'] + "\">" + list[i]['title1'] + "</option>"
    
    return render_to_response('secry/pureHTMLString.html', {'htmlString':var}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxCourseAvailability(request, course_id):
    msg = "<i></i>"
    print "mpika"
    if not courseIdAvailable(course_id):
        msg = "<i><strong>...Not available...</strong></i>"
        print "not avail"
    
    return render_to_response('secry/pureHTMLString.html', {'htmlString':msg}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxAddAndRefresh(request):
    cStatus = ""
    if request.method == "GET":
        if 'cstatus' not in request.GET:
            return
        else:
            cStatus = request.GET['cstatus']

    s = Course_Settings_Translate(status=cStatus, language='el_GR', isDefault=1)
    s.save()
    
    list = getCourseStatusList()
    var = ""
    for i in xrange(len(list)):
        var += "<option value=\"" + str(list[i]['id']) + "\">" + list[i]['status'] + "</option>"
    
    return render_to_response('secry/pureHTMLString.html', {'htmlString':var}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def ajaxRemoveAndRefresh(request):
    cStatus = ""
    if request.method == "GET":
        if 'cstatus' not in request.GET:
            return
        else:
            cStatus = request.GET['cstatus']            
    
    print cStatus
    #remove status and connection with other tables
    obj = Course_Settings_Translate.objects.get(pk=cStatus)
    status_id = obj.id
    obj.delete()
    for item in OrientCourses_Has_Courses.objects.filter(status=status_id):
        item_id = item.id
        item.delete()
        
        for item2 in OrientCourses_Has_Courses_Translate.objects.filter(orientAndCourses=item_id):
            item2.delete()
    
    
    list = getCourseStatusList()
    var = ""
    for i in xrange(len(list)):
        var += "<option value=\"" + str(list[i]['id']) + "\">" + list[i]['status'] + "</option>"
    print var
    return render_to_response('secry/pureHTMLString.html', {'htmlString':var}, context_instance = RequestContext(request))


