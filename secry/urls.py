from django.conf.urls.defaults import *

from diagoras.secry.views import *



urlpatterns = patterns('',
    (r'^$', viewSecryProgram),
    (r'^(\d+)/courses/$', secryCourses),
    (r'^(\d+)/proglist_courses/$', coursesForProglist),
    (r'^(\d+)/classes/$', secryClasses),
    (r'^(\d+)/exams/$', secryExams),
    (r'^professors/$', secryProfessors),
    
    (r'^(\d+)/(\w+)/edit_courses/$', editSecryCourses),
    (r'^(\d+)/(\w+)/edit_proglist_courses/$', editCoursesForProglist),
    (r'^(\d+)/(\w+\-\w+)/edit_classes/$', editSecryClasses),
    (r'^(\d+)/(\d+)/edit_exams/$', editSecryExams),
    (r'^(\d+)/edit_professors/$', editSecryProfessors),
    (r'^(\d+)/edit_curriculum/$', editProglist),
    (r'^(\d+)/edit_orientation/$', editOrientation),
    
    (r'^add_school/$', addSecrySchool),
    (r'^add_department/$', addSecryDepartment),
    (r'^add_proglist/$', addSecryProglist),
    (r'^add_orientation/$', addSecryOrientation),
    (r'^add_courses/$', addSecryCourses),
    (r'^add_bibliography/$', addSecryBibliography),
    (r'^add_professor/$', addSecryProfessor),
    (r'^add_classes/$', addSecryClasses),
    (r'^add_exams/$', addSecryExams),
    
    (r'^perform/add/$', performAdd),
    (r'^perform/update/$', performUpdate),
    
    (r'^dynamic/curriculumOption/(\d+)/$', ajaxCurriculum),
    (r'^dynamic/orientationOption/(\d+)/$', ajaxOrientation),
    (r'^dynamic/courseOption/(\d+)/$', ajaxCourses),
    (r'^dynamic/parentCourseOption/(\d+)/$', ajaxParentCourses),
    (r'^dynamic/courseID_Availability/(\w+)/$', ajaxCourseAvailability),
    (r'^dynamic/addAndRefresh/$', ajaxAddAndRefresh),
    (r'^dynamic/removeAndRefresh/$', ajaxRemoveAndRefresh),
    
)
