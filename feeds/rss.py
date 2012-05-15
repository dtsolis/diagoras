# -*- coding: utf-8 -*-

from django.contrib.syndication.views import FeedDoesNotExist, Feed
from django.shortcuts import get_object_or_404

from datetime import datetime
from django.contrib.sites.models import Site
from diagoras.feeds.data import *

class ProgListFeed(Feed):
    # RSS variables
    author_name = 'Tsolis Dimitris-Sotiris'
    feed_copyright = 'Copyright (c) 20011, Tsolis Dimitris-Sotiris'
    item_pubdate = datetime.today()
    
    # My variables
    progid = ""
    
    
    def get_object(self, request, progList_id):
        self.progid = progList_id
        preferedLanguage = 'el_GR'
        return ProgList_Translate.objects.values('proglist', 'progTitle').get(proglist=progList_id, language=preferedLanguage)
    
    def title(self, obj):
        return obj['progTitle']
    
    def link(self, obj):
        return "/feeds/rss/" + str(obj['proglist']) + "/"
    
    def description(self, obj):
        return "description"
    
    def items(self, obj):
        return getRssCourseWithLanguage(obj['proglist'], 'el_GR')
    
    def item_link(self, item):
        url = "/feeds/rss/" + self.progid + "/" + item['idcourses'] + "/html/"
        return url
    
    def item_title(self, item):
        sem = unicode("(Εξ. ", "utf-8")
        return sem + str(item['semester']) + ") " + item['title1']
    
    def item_description(self, item):
        id = "Not found"
        if item['idcourses']:
            id = item['idcourses']
        title = "Not found"
        if item['title1']:
            title = item['title1']
        Status = "Not found"
        if item.has_key('status') and item['status']:
            Status = item['status']
        theoryh = "0"
        if item.has_key('theoryHours') and item['theoryHours']:
            HpW = item['theoryHours']
        tuth = "0"
        if item.has_key('theoryHours') and item['theoryHours']:
            HpW = item['theoryHours']
        labh = "0"
        if item.has_key('theoryHours') and item['theoryHours']:
            HpW = item['theoryHours']
        dm = "Not found"
        if item.has_key('cdm') and item['cdm']:
            dm = item['cdm']
        semester = "Not found"
        if item.has_key('semester') and item['semester']:
            semester = item['semester']
        goals = "Not found"
        if item['goals']:
            goals =  item['goals']
        d = "Not found"
        if item['description']:
            d =  item['description']
        
        tcode = unicode("Κωδικός", "utf-8")
        ttitle = unicode("Τίτλος", "utf-8")
        tStatus = unicode("Χαρακτηρισμός", "utf-8")
        tHoursPerWeek = unicode("Ω/Εβδ", "utf-8")
        tDM = unicode("ΔΜ", "utf-8")
        tSemester = unicode("Εξάμηνο", "utf-8")
        tgoals = unicode("Στόχοι", "utf-8")
        tDescription = unicode("Περιγραφή", "utf-8")
        tBiblio = unicode("Βιβλιογραφία", "utf-8")
        
        desc = tcode + ":<br />" + id
        desc += "<br /><br />"+ttitle+":<br />" + title
        desc += "<br /><br />"+tStatus+":<br />" + Status
        desc += "<br /><br />"+tHoursPerWeek+":<br />" + theoryh +" Theory + " + tuth + " Tutorial + " + labh + " Lab "
        desc += "<br /><br />"+tDM+":<br />" + str(dm)
        desc += "<br /><br />"+tSemester+":<br />" + str(semester) 
        desc += "<br /><br />"+tgoals+":<br />" +  goals
        desc += "<br /><br />"+tDescription+":<br />" + d 
        desc += "<br /><br />"+tBiblio+":<br />"+ item['bibliography']
        
        return desc
        
        
    
    
class CourseDetailsFeed(Feed):
    progid = "" 
    
    def get_object(self, request, progList_id, course_id):
        self.progid = progList_id
        
        obj = getProgCoursesWithLanguage(progList_id, 'el_GR')
        return obj
    
    def title(self, obj):
        return 'obj.'
    
    def link(self, obj):
        return "obj.get_absolute_url()"
    
    def description(self, obj):
        return "description"
    
    def items(self, obj):
        return obj
    
    def item_link(self, item):
        url = "lskjdf"
        return url