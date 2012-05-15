# synartiseis gia na trabaw dedomena apo tin basi dedomenwn

from diagoras.tei.models import *
from django.db import connection, transaction
from django.utils import translation

	
def getLanguageLocale():
	lang = translation.get_language()
	
	if "el" in lang and "gr" in lang:
		lang = "el_GR"
	else:
		lang = "en_US"
	
	return lang
	
def dictfetchall(cursor):
	"Returns all rows from cursor as a dict"
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]
	
def getProgramList():
	cursor = connection.cursor()
	
	tmplang = getLanguageLocale()
	cursor.execute("select tei_department.iddepartment, tei_progList.idprogList, tei_department_translate.depTitle, tei_progList_translate.progTitle from tei_department, tei_department_translate, tei_progList, tei_progList_translate, tei_institution, tei_school where idinstitution=institution_id and idschool=school_id and tei_department.iddepartment=tei_progList.department_id and tei_progList.active=1 and tei_institution.idinstitution=1 and tei_department_translate.department_id = tei_department.iddepartment and tei_progList_translate.proglist_id = tei_progList.idprogList and tei_department_translate.language='%s' and tei_progList_translate.language='%s' order by depTitle, progTitle" % (tmplang, tmplang))
	rows = dictfetchall(cursor)
	
	return rows

def getProgramListActiveOrNot():
	cursor = connection.cursor()
	
	tmplang = getLanguageLocale()
	cursor.execute("select tei_department.iddepartment, tei_progList.idprogList, tei_department_translate.depTitle, tei_progList_translate.progTitle from tei_department, tei_department_translate, tei_progList, tei_progList_translate, tei_institution, tei_school where idinstitution=institution_id and idschool=school_id and tei_department.iddepartment=tei_progList.department_id and tei_institution.idinstitution=1 and tei_department_translate.department_id = tei_department.iddepartment and tei_progList_translate.proglist_id = tei_progList.idprogList and tei_department_translate.language='%s' and tei_progList_translate.language='%s' order by depTitle, progTitle" % (tmplang, tmplang))
	rows = dictfetchall(cursor)
	
	return rows

def getProgListName(idprogList):
	a = ProgList_Translate.objects.values('progTitle').filter(proglist=idprogList, language=getLanguageLocale())

	return a[0]['progTitle']

def getProgCourses(idprogList):
	cursor = connection.cursor()
	
	tmplang = getLanguageLocale()
	cursor.execute("select tei_courses.semester, tei_courses_translate.courseType, tei_courses.idcourses, tei_courses_translate.title1, tei_orientcourses_translate.orientationName, tei_orientcourses_has_courses_translate.selectionType, tei_courses.cdm from tei_courses, tei_courses_translate, tei_orientcourses, tei_orientcourses_translate, tei_orientcourses_has_courses, tei_orientcourses_has_courses_translate, tei_orientcourses_has_proglist where tei_orientcourses_has_courses.courses_id=tei_courses.idcourses and tei_orientcourses_has_courses.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.progList_id='%s' and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s' and tei_orientcourses.idorientCourses=tei_orientcourses_translate.orientCourses_id and tei_orientcourses_translate.language='%s' and tei_orientcourses_has_courses.id=tei_orientcourses_has_courses_translate.orientAndCourses_id and tei_orientcourses_has_courses_translate.language='%s' order by tei_courses.semester, tei_orientcourses_translate.orientationName, tei_courses_translate.title1" % (idprogList, tmplang, tmplang, tmplang))
	rows = dictfetchall(cursor)
	
	return rows

def getProgCoursesWithLanguage(idprogList, tmplang):
	cursor = connection.cursor()
	
	cursor.execute("select tei_courses.semester, tei_courses_translate.courseType, tei_courses.idcourses, tei_courses_translate.title1, tei_orientcourses_translate.orientationName, tei_orientcourses_has_courses_translate.selectionType, tei_courses.cdm from tei_courses, tei_courses_translate, tei_orientcourses, tei_orientcourses_translate, tei_orientcourses_has_courses, tei_orientcourses_has_courses_translate, tei_orientcourses_has_proglist where tei_orientcourses_has_courses.courses_id=tei_courses.idcourses and tei_orientcourses_has_courses.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.progList_id='%s' and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s' and tei_orientcourses.idorientCourses=tei_orientcourses_translate.orientCourses_id and tei_orientcourses_translate.language='%s' and tei_orientcourses_has_courses.id=tei_orientcourses_has_courses_translate.orientAndCourses_id and tei_orientcourses_has_courses_translate.language='%s' order by tei_courses.semester, tei_orientcourses_translate.orientationName, tei_courses_translate.title1" % (idprogList, tmplang, tmplang, tmplang))
	rows = dictfetchall(cursor)
	
	return rows

def getProgInfo(idprogList):
	cursor = connection.cursor()
	
	tmplang = getLanguageLocale()
	cursor.execute("select tei_proglist.idprogList, tei_proglist_translate.progTitle, tei_proglist_translate.studyLevel, tei_proglist_translate.diplomaTitle, tei_proglist.fee, tei_proglist.semestersNum, tei_department_translate.depTitle, tei_school_translate.title from tei_proglist, tei_proglist_translate, tei_department, tei_department_translate, tei_school, tei_school_translate where tei_proglist.department_id=tei_department.iddepartment and tei_department.school_id=tei_school.idschool and tei_proglist.idprogList=%s and tei_department.iddepartment = tei_department_translate.department_id and tei_department_translate.language = '%s' and tei_proglist.idprogList = tei_proglist_translate.proglist_id and tei_proglist_translate.language = '%s' and tei_school.idschool = tei_school_translate.school_id and tei_school_translate.language = '%s'" % (idprogList, tmplang, tmplang, tmplang))
	rows = dictfetchall(cursor)
	
	return rows

def getCourseDetails(idcourse):
	cursor = connection.cursor()
	
	tmplang = getLanguageLocale()
	cursor.execute("select tei_courses.idcourses, tei_courses_translate.courseType, tei_department_translate.depTitle,tei_courses_translate.teachPeriod, tei_courses_translate.title1, tei_courses.semester, tei_courses.cdm, tei_courses.didasketai, tei_courses_translate.description from tei_courses, tei_courses_translate, tei_department, tei_department_translate where tei_courses.department_id=tei_department.iddepartment and tei_courses.idcourses='%s' and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s' and tei_department.iddepartment=tei_department_translate.department_id and tei_department_translate.language='%s'" % (idcourse, tmplang, tmplang))
	rows = dictfetchall(cursor)
	
	return rows

def getCourseSelectionType(idcourse):
	cursor = connection.cursor()
	
	cursor.execute("select distinct tei_orientcourses_has_courses_translate.selectionType from tei_orientcourses_has_courses, tei_orientcourses_has_courses_translate where tei_orientcourses_has_courses.courses_id='%s' and tei_orientcourses_has_courses.id=tei_orientcourses_has_courses_translate.orientAndCourses_id and tei_orientcourses_has_courses_translate.language='%s'" % (idcourse, getLanguageLocale()) )
	rows = dictfetchall(cursor)
	
	return rows

def getCourseProffesors(idcourse):
	cursor = connection.cursor()
	
	cursor.execute("select tei_professors_translate.title, tei_professors_translate.lastName, tei_professors_translate.name, tei_professors.email from tei_courses, tei_professors, tei_professors_translate where tei_courses.professors_id=tei_professors.idprofessors and tei_courses.idcourses='%s' and tei_professors.idprofessors=tei_professors_translate.professors_id and tei_professors_translate.language='%s'" % (idcourse, getLanguageLocale()))
	rows = dictfetchall(cursor)
	
	return rows

def getChildrenCourse(idparent):
	cursor = connection.cursor()
	
	cursor.execute("select tei_courses.idcourses, tei_courses_translate.title1 from tei_courses, tei_courses_translate where tei_courses.parentCourse_id='%s' and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s'" % (idparent, getLanguageLocale()))
	rows = dictfetchall(cursor)
	
	return rows

def getParentCourse(course_id):
	cursor = connection.cursor()
	
	cursor.execute("select tei_courses.idcourses, tei_courses_translate.title1 from tei_courses, tei_courses_translate where tei_courses.idcourses=(select tei_courses.parentCourse_id	from tei_courses where tei_courses.idcourses = '%s') and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s'" % (course_id, getLanguageLocale()))
	rows = dictfetchall(cursor)
	
	return rows

