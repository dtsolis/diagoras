from django.conf.urls.defaults import *

from diagoras.feeds.rss import *
from diagoras.feeds.views import *


urlpatterns = patterns('',
    (r'^rss/(?P<progList_id>\d+)/$', ProgListFeed()),
    (r'^rss/(?P<progList_id>\d+)/(?P<course_id>\w{0,30})/$', CourseDetailsFeed()),
    (r'^rss/(?P<progList_id>\d+)/(?P<course_id>\w{0,30})/html/$', CourseDetailsPage),
)
