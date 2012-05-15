from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

from django.template import RequestContext
from django.contrib import auth

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from diagoras.extras.data import *


def is_user(user):
    return user.is_authenticated()

def is_user_superuser(user):
    return user.is_superuser

#---- @user_passes_test(...) ----
# Se kathe synartisi gia na empodizei kapoion "anonymo" na syndeetai se aytes tis selides

@user_passes_test(is_user_superuser, login_url="/login/")
def usersMain(request):
    return render_to_response('users/users.html', {}, context_instance = RequestContext(request))
    
@user_passes_test(is_user_superuser, login_url="/login/")
def messages(request):
    if request.method == "POST":
        chkbox = request.POST.getlist('checkbox')
        if chkbox:
            if request.POST['act']=='read':
                markMessageList(chkbox, True)
            elif request.POST['act']=='unread':
                markMessageList(chkbox, False)
            elif request.POST['act']=='del':
                deleteManyMessages(chkbox)
                
    list = getMessageList()
    return render_to_response('users/messages.html', {'list':list}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def messageDetails(request, message_id):
    # lista me tis leptomeries gia to minima
    list = getMessageDetails(message_id)
    
    # markarisma minimatos ws anagnwsmeno
    markMessage(message_id, 1)
    return render_to_response('users/messages.html', {'details':list, 'state':'details'}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def forwardMessages(request): 
    if request.method == "POST":
        # lista me tis eggrafes gia proothisi
        if 'state' not in request.POST:
            chkbox = request.POST.getlist('checkbox')
            if chkbox:
                if request.POST['act']=='enable':
                    enableDisableForward(chkbox, True)
                elif request.POST['act']=='disable':
                    enableDisableForward(chkbox, False)
                elif request.POST['act']=='del':
                    deleteForwardList(chkbox)
        # Prosthiki neas eggrafis
        elif request.POST['state'] == 'add':
            fTo = request.POST['to']
            fFrom = request.POST['from']
            pFrom = request.POST['password']
            smtp = request.POST['server']
            port = request.POST['port']
            enableForwd = 1
            if 'checkbox' not in request.POST:
                enableForwd = 0
            addForwardMessage(fTo, fFrom, pFrom, smtp, port, enableForwd)
        # Allagi eggrafis
        elif request.POST['state'] == 'update':
            id = request.POST['id']
            fto = request.POST['to']
            ffrom = request.POST['from']
            passfrom = request.POST['password']
            smtp = request.POST['server']
            port = request.POST['port']
            enable = 1
            if 'checkbox' not in request.POST:
                enable = 0
            updateForward(id, fto, ffrom, passfrom, smtp, port, enable)
                 
    list = getForwardList()
    return render_to_response('users/forward.html', {'list':list}, context_instance = RequestContext(request))


@user_passes_test(is_user_superuser, login_url="/login/")
def editForward(request, forward_id):  
    details = getForwardDetails(forward_id)
    return render_to_response('users/forward.html', {'details':details, 'state':'details'}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def addForward(request):  
    return render_to_response('users/forward.html', {'details':list, 'state':'add'}, context_instance = RequestContext(request))


@user_passes_test(is_user_superuser, login_url="/login/")
def manage(request):
    return render_to_response('users/manage.html', {}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def profile(request):
    return render_to_response('users/profile.html', {}, context_instance = RequestContext(request))

@user_passes_test(is_user_superuser, login_url="/login/")
def add_user(request):
    #return render_to_response('users/manage.html', {'sub':'add user'}, context_instance = RequestContext(request))
    redirect_to = "/admin/auth/user/add/"
    return HttpResponseRedirect(redirect_to) 

@user_passes_test(is_user_superuser, login_url="/login/")
def edit_user(request):
    #return render_to_response('users/manage.html', {'sub':'edit user'}, context_instance = RequestContext(request))
    redirect_to = "/admin/auth/user/"
    return HttpResponseRedirect(redirect_to) 