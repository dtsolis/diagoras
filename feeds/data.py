from diagoras.tei.data import * 
from diagoras.tei.models import *

def getRssCourseWithLanguage(progList_id, tmplang):
    cursor = connection.cursor()
    
    cursor.execute("select tei_courses.semester, tei_courses.idcourses, tei_courses_translate.courseType, tei_courses_translate.title1, tei_courses_translate.description, tei_courses_translate.goals, tei_orientcourses_translate.orientationName, tei_orientcourses_has_courses_translate.selectionType, tei_course_settings_translate.status, tei_courses.cdm, tei_courses.theoryHours, tei_courses.tutHours, tei_courses.labHours from tei_courses, tei_courses_translate, tei_orientcourses, tei_orientcourses_translate, tei_orientcourses_has_courses, tei_orientcourses_has_courses_translate, tei_orientcourses_has_proglist, tei_course_settings_translate where tei_orientcourses_has_courses.courses_id=tei_courses.idcourses and tei_orientcourses_has_courses.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.progList_id='%s' and (tei_courses.parentCourse_id is null or tei_courses.parentCourse_id='') and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s' and tei_orientcourses.idorientCourses=tei_orientcourses_translate.orientCourses_id and tei_orientcourses_translate.language='%s' and tei_orientcourses_has_courses.id=tei_orientcourses_has_courses_translate.orientAndCourses_id and tei_orientcourses_has_courses_translate.language='%s' and tei_course_settings_translate.id=tei_orientcourses_has_courses.status_id order by tei_courses.semester, tei_orientcourses_translate.orientationName, tei_courses_translate.title1" % (progList_id, tmplang, tmplang, tmplang))
    
    rows = dictfetchall(cursor)
    

    # An den epestrepse tipota
    if not rows:
        dict1 = dict(idcourses="", title1="", status="", theoryHours="", cdm="", semester="", goals="", description="", bibliography="")
        rows = [dict1]
    else:
        # Prosthiki bibliografias se kathe mathima
        i = 0
        for r in rows:
            biblio = Bibliography.objects.filter(course=r['idcourses'])
            # Dhmiourgia enos string me ola ta biblia poy efere to erwtima
            b = ""
            for var in biblio:
                b += "~ "+var.author+', '+var.bititle+', '+var.editor+', '+str(var.pubYear.year)+'.<br />'
            
            # Prosthiki tou sting se neo 'key' apo to kathe Dictionary
            rows[i]['bibliography'] = b
            i += 1
    
    return rows

def getSingleRssCourse(progList_id, idcourses):
    cursor = connection.cursor()
    
    tmplang = getLanguageLocale()
    cursor.execute("select tei_courses.semester, tei_courses.idcourses, tei_courses_translate.courseType, tei_courses_translate.title1, tei_courses_translate.description, tei_courses_translate.goals, tei_orientcourses_translate.orientationName, tei_orientcourses_has_courses_translate.selectionType, tei_course_settings_translate.status, tei_courses.cdm, tei_courses.theoryHours, tei_courses.tutHours, tei_courses.labHours from tei_courses, tei_courses_translate, tei_orientcourses, tei_orientcourses_translate, tei_orientcourses_has_courses, tei_orientcourses_has_courses_translate, tei_orientcourses_has_proglist, tei_course_settings_translate where tei_orientcourses_has_courses.courses_id=tei_courses.idcourses and tei_orientcourses_has_courses.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.orientCourses_id=tei_orientcourses.idorientCourses and tei_orientcourses_has_proglist.progList_id='%s' and tei_courses.idcourses='%s' and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s' and tei_orientcourses.idorientCourses=tei_orientcourses_translate.orientCourses_id and tei_orientcourses_translate.language='%s' and tei_orientcourses_has_courses.id=tei_orientcourses_has_courses_translate.orientAndCourses_id and tei_orientcourses_has_courses_translate.language='%s' and tei_course_settings_translate.id=tei_orientcourses_has_courses.status_id order by tei_courses.semester, tei_orientcourses_translate.orientationName, tei_courses_translate.title1" % (progList_id, idcourses, tmplang, tmplang, tmplang))
    
    rows = dictfetchall(cursor)
    
    # An den epestrepse tipota
    if not rows:
        dict1 = dict(idcourses="", title1="", status="", theoryHours="", cdm="", semester="", goals="", description="", bibliography="")
        rows = [dict1]
    else:
        biblio = Bibliography.objects.filter(course=rows[0]['idcourses'])
        # Dhmiourgia enos string me ola ta biblia poy efere to erwtima
        b = ""
        for var in biblio:
            b += "~ "+var.author+', '+var.bititle+', '+var.editor+', '+str(var.pubYear.year)+'.<br />'
            
        # Prosthiki tou sting se neo 'key' apo to kathe Dictionary
        rows[0]['bibliography'] = b
    
    return rows

def getCourse(course_id):
    cursor = connection.cursor()
    
    cursor.execute("select tei_courses.*, tei_courses_translate.* from tei_courses, tei_courses_translate where tei_courses.idcourses='%s' and tei_courses.idcourses=tei_courses_translate.courses_id and tei_courses_translate.language='%s'" % (course_id, getLanguageLocale()))
    rows = dictfetchall(cursor)
    
    return rows