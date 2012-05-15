from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.contrib import auth

from diagoras.feeds.data import *

def CourseDetailsPage(request, progList_id, course_id):
    c = getSingleRssCourse(progList_id, course_id)
    
    return render_to_response('feeds/course-details.html', {'course':c}, context_instance = RequestContext(request))