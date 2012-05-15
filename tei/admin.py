from diagoras.tei.models import *
from django.contrib import admin


class SchoolAdmin(admin.ModelAdmin):
	list_display = ('idschool', 'institution')

class School_TranslateAdmin(admin.ModelAdmin):
	list_display = ('title', 'language')

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('iddepartment', 'email')

class Department_TranslateAdmin(admin.ModelAdmin):
	list_display = ('depTitle', 'director', 'studyLevel')

class CoursesAdmin(admin.ModelAdmin):
	list_display = ('idcourses', 'active')

class Courses_TranslateAdmin(admin.ModelAdmin):
	list_display = ('courseType','title1')

class ProgListAdmin(admin.ModelAdmin):
	list_display = ('idprogList', 'active')

class ProgList_TranslateAdmin(admin.ModelAdmin):
	list_display = ('progTitle', 'studyLevel', 'diplomaTitle')


admin.site.register(Institution)
admin.site.register(School, SchoolAdmin)
admin.site.register(School_Translate, School_TranslateAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Department_Translate, Department_TranslateAdmin)
admin.site.register(Professors)
admin.site.register(Professors_Translate)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Courses_Translate, Courses_TranslateAdmin)
admin.site.register(Course_Settings_Translate)
admin.site.register(ProgList, ProgListAdmin)
admin.site.register(ProgList_Translate, ProgList_TranslateAdmin)
admin.site.register(ClassList)
admin.site.register(ClassList_Translate)
admin.site.register(Exams)
admin.site.register(OrientCourses)
admin.site.register(OrientCourses_Translate)
admin.site.register(Exams_Has_Courses)
admin.site.register(OrientCourses_Has_ProgList)
admin.site.register(Professors_Has_Department)
admin.site.register(OrientCourses_Has_Courses)

