from django.db import models

# Create your models here.

class Institution(models.Model):
    idinstitution = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=45, blank=True, null=True)
    
    def __unicode__(self):
        return self.website

class School(models.Model):
    idschool = models.IntegerField(primary_key=True)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    
class School_Translate(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    school = models.ForeignKey(School, blank=True, null=True)
    
class Department(models.Model):
    iddepartment = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=45, blank=True, null=True)
    school = models.ForeignKey(School, blank=True, null=True)
    
class Department_Translate(models.Model):
    depTitle = models.CharField(max_length=45, blank=True, null=True)
    director = models.CharField(max_length=45, blank=True, null=True)
    studyLevel = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    department = models.ForeignKey(Department, blank=True, null=True)

class Professors(models.Model):
    idprofessors = models.IntegerField(primary_key=True)
    teaches = models.NullBooleanField()
    email = models.CharField(max_length=5, blank=True, null=True)
    hireDate = models.DateTimeField(blank=True, null=True)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    
class Professors_Translate(models.Model):
    title = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    lastName = models.CharField(max_length=45, blank=True, null=True)
    fatherName = models.CharField(max_length=45, blank=True, null=True) #
    sex = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    Professors = models.ForeignKey(Professors, blank=True, null=True)

class Courses(models.Model):
    idcourses = models.CharField(max_length=30, primary_key=True)
    active = models.NullBooleanField()
    gradeScale = models.CharField(max_length=5, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    scolarships = models.NullBooleanField()
    teachHours = models.IntegerField(blank=True, null=True)
    theoryHours = models.IntegerField(blank=True, null=True)                #
    tutHours = models.IntegerField(blank=True, null=True)                   #
    labHours = models.IntegerField(blank=True, null=True)                   #
    cdm = models.FloatField(blank=True, null=True)
    ects = models.FloatField(blank=True, null=True)                         #
    didasketai = models.NullBooleanField()
    validationPeriod = models.CharField(max_length=10, blank=True, null=True) # eg. 2005-2006
    department = models.ForeignKey(Department, blank=True, null=True)
    professors = models.ForeignKey(Professors, blank=True, null=True, on_delete=models.SET_NULL)
    replacedBy = models.ForeignKey("self", related_name="replaced", blank=True, null=True)           # an antikatastathike, apo poio
    parentCourse = models.ForeignKey("self", blank=True, null=True)

class Courses_Translate(models.Model):
    courseType = models.CharField(max_length=30, blank=True, null=True)
    title1 = models.CharField(max_length=45, blank=True, null=True)
    title2 = models.CharField(max_length=45, blank=True, null=True)
    knownObject = models.CharField(max_length=45, blank=True, null=True)    #
    teachPeriod = models.CharField(max_length=10, blank=True, null=True)   # an didasketai XEIM EAR h OLES tis periodous
    description = models.TextField(blank=True, null=True)
    goals = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    courses = models.ForeignKey(Courses, blank=True, null=True)
    
class Bibliography(models.Model):                                           #
    idbiblio = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    bititle = models.CharField(max_length=70, blank=True, null=True)
    editor = models.CharField(max_length=70, blank=True, null=True)
    pubYear = models.DateField(blank=True, null=True)
    course = models.ForeignKey(Courses, blank=True, null=True)

class ProgList(models.Model):
    idprogList = models.IntegerField(primary_key=True)
    active = models.NullBooleanField()
    fee = models.NullBooleanField()
    semestersNum = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True)
    
class ProgList_Translate(models.Model):
    studyLevel = models.CharField(max_length=20, blank=True, null=True)
    progTitle = models.CharField(max_length=45, blank=True, null=True)
    diplomaTitle = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    proglist = models.ForeignKey(ProgList, blank=True, null=True)
    

class ClassList(models.Model):
    idclassList = models.CharField(max_length=20, blank=True, null=True)
    active = models.NullBooleanField()
    academicYear = models.CharField(max_length=10, blank=True, null=True)
    weeklyHours = models.IntegerField(max_length=11, blank=True, null=True)
    totalStudents = models.IntegerField(max_length=11, blank=True, null=True)
    maxStudents = models.IntegerField(max_length=11, blank=True, null=True)
    courses = models.ForeignKey(Courses)
    department = models.ForeignKey(Department)
    professors = models.ForeignKey(Professors, blank=True, null=True, on_delete=models.SET_NULL)
    
class ClassList_Translate(models.Model):
    classPeriod = models.CharField(max_length=5, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    cstate = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    classlist = models.ForeignKey(ClassList, blank=True, null=True)

class GroupList(models.Model):
    idgroupList = models.IntegerField(primary_key=True)
    active = models.NullBooleanField()
    startTime = models.TimeField(blank=True, null=True)
    endTime = models.TimeField(blank=True, null=True)
    dayOfWeek = models.CharField(max_length=20, blank=True, null=True)
    classlist = models.ForeignKey(ClassList)

class Exams(models.Model):
    idexams = models.IntegerField(primary_key=True)
    academicYear = models.CharField(max_length=15, blank=True, null=True)
    examsPeriod = models.CharField(max_length=5, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True)

class OrientCourses(models.Model):
    idorientCourses = models.IntegerField(max_length=11, primary_key=True)
    active = models.NullBooleanField()
    diplomaOrient = models.NullBooleanField()   #1 an h katey8insi 8a fainetai sto ptyxio
    department = models.ForeignKey(Department, blank=True, null=True)   #
    
class OrientCourses_Translate(models.Model):
    orientationName = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    orientcourses = models.ForeignKey(OrientCourses, blank=True, null=True)

class Exams_Has_Courses(models.Model):
    exams = models.ForeignKey(Exams)
    courses = models.ForeignKey(Courses)
    repeat = models.NullBooleanField()
    examDate = models.DateTimeField(blank=True, null=True)
    class Meta:
        unique_together = ('exams','courses')

class OrientCourses_Has_ProgList(models.Model):
    orientCourses = models.ForeignKey(OrientCourses)
    progList = models.ForeignKey(ProgList)
    class Meta:
        unique_together = ('orientCourses', 'progList')

class Professors_Has_Department(models.Model):
    professors = models.ForeignKey(Professors)
    department = models.ForeignKey(Department)
    class Meta:
        unique_together = ('professors', 'department')

class Course_Settings_Translate(models.Model):                     #
    status = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    

class OrientCourses_Has_Courses(models.Model):
    orientCourses = models.ForeignKey(OrientCourses)
    courses = models.ForeignKey(Courses)
    status = models.ForeignKey(Course_Settings_Translate, blank=True, null=True)
    class Meta:
        unique_together = ('orientCourses', 'courses')
        
class OrientCourses_Has_Courses_Translate(models.Model):
    selectionType = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    isDefault = models.NullBooleanField()
    orientAndCourses = models.ForeignKey(OrientCourses_Has_Courses, blank=True, null=True)


