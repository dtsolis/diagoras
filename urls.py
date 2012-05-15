from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from diagoras.views import *
from diagoras.users.views import *
from diagoras.secry.views import *
from diagoras.feeds.rss import *


urlpatterns = patterns('',
    # Example:
    # (r'^diagoras/', include('diagoras.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^admin/', include(admin.site.urls)),
    (r'^users/', include('diagoras.users.urls')),
    
    (r'^feeds/', include('diagoras.feeds.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    
    (r'^login/$', login),
    (r'^logout/$', logout),
    
    (r'^programma/$', viewProgram),
    (r'^programma/(\d+)/$', progDetails),
    (r'^programma/(\d+)/(\w{0,30})/$', courseDetails),
    (r'^programma/quick-view$', quickProgram),
    (r'^programma/quick-view/(\d+)/$', quickCourses),
    (r'^extraLinks/$', extraLinks),
    (r'^contact/$', contact),
    (r'^contact/send/$', sendMessage),
    
    
    (r'^$', index),
)
