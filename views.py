

from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.contrib import auth

from django.utils.translation import check_for_language, activate, deactivate, to_locale, get_language, ugettext as _
from django.contrib.sessions.middleware import SessionMiddleware

from diagoras.tei.data import *
from diagoras.extras.data import *
from diagoras.feeds.data import *

   
def index(request):
	return render_to_response('index.html', {}, context_instance = RequestContext(request))
    
def logout(request):
	language = request.LANGUAGE_CODE
	redirect_to = request.REQUEST.get('next', '/')
	auth.logout(request)


	return HttpResponseRedirect(redirect_to) 

def login(request):
	# An den yparxei parametros 'next' tha pigainei stin arxiki selida
	redirect_to = request.REQUEST.get('next', '/')
	
	if request.method == "POST":
		post = request.POST.copy()
		if post.has_key('username') and post.has_key('password'):
			usr = post['username']
			pwd = post['password']
			remember = post.has_key('remember')
			user = auth.authenticate(username=usr, password=pwd)
			if user is not None and user.is_active:
				auth.login(request, user)
				if remember==False:
					request.session.set_expiry(0)
				# Redirect to previous page 
				return HttpResponseRedirect(redirect_to) 
                else:
                    return render_to_response('login.html', {'error':_("lathos eisagogi stoixeiwn")}, context_instance = RequestContext(request))		
	return render_to_response('login.html', {}, context_instance = RequestContext(request))

def extraLinks(request):
    return render_to_response('usefulLinks.html', {}, context_instance = RequestContext(request))

def contact(request):
	return render_to_response('contact.html', {}, context_instance = RequestContext(request))
    
def sendMessage(request):
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('name') and post.has_key('subject') and post.has_key('msg'):
            name = post['name'].strip()
            email = post['email'].strip()
            subject = post['subject'].strip()
            message = post['msg'].strip()
            
            if name=="" or subject=="" or message=="":
                return  render_to_response('contact.html', {'error':_("den symplirothikan ola ta stoixeia")}, context_instance = RequestContext(request))
            # save message to db
            saveMessage(name, email, subject, message)
            # send email to admin if asked
            sendEmail()
            
            return HttpResponseRedirect('/contact/') 
        
    return render_to_response('contact.html', {'message':text}, context_instance = RequestContext(request))

def viewProgram(request):
    d = getProgramList()
    var = _("test string to translate")
    return render_to_response('programma.html', {'progList':d}, context_instance = RequestContext(request))

def progDetails(request, idprogList):
	p1 = getProgInfo(idprogList)
	p2 = getProgCourses(idprogList)
	return render_to_response('programma.html', {'progInfo':p1, 'progCourses':p2, 'details':'prog'}, context_instance = RequestContext(request))

def courseDetails(request, idprogList, idcourse):
    n = getProgListName(idprogList)
    c = getCourseDetails(idcourse)
    select = getCourseSelectionType(idcourse)
    prof = getCourseProffesors(idcourse)
    a = getChildrenCourse(idcourse)
    parent = getParentCourse(idcourse)

    return render_to_response('programma.html', {'courseDetails':c, 'type':select, 'professor':prof, 'details':'course', 'prev':idprogList, 'progListName':n, 'childrenCourse':a, 'parentCourse':parent}, context_instance = RequestContext(request))

def quickProgram(request):
    d = getProgramList()
    return render_to_response('quick.html', {'progList':d, 'mode':'prog'}, context_instance = RequestContext(request))

def quickCourses(request, idprogList):
    p2 = getRssCourseWithLanguage(idprogList, getLanguageLocale())
    return render_to_response('quick.html', {'progCourses':p2, 'mode':'courses', 'idprogList':idprogList}, context_instance = RequestContext(request))

