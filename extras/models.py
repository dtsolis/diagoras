from django.db import models

# Create your models here.

class Messages(models.Model):
    idmessage = models.IntegerField(primary_key=True)
    sndrName = models.CharField(max_length=45, blank=True, null=True)
    sndrEmail = models.CharField(max_length=45, blank=True, null=True)
    subject = models.CharField(max_length=45, blank=True, null=True)
    message = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    read = models.NullBooleanField()
    send = models.NullBooleanField()
    
class Forward_Message(models.Model):
    idforward = models.IntegerField(primary_key=True)
    forwardTo = models.CharField(max_length=75, blank=True, null=True)
    forwardFrom = models.CharField(max_length=75, blank=True, null=True)
    passwordFrom = models.CharField(max_length=75, blank=True, null=True)
    smtpServer = models.CharField(max_length=75, blank=True, null=True)
    smtpPort = models.IntegerField(blank=True, null=True)
    enableForward = models.NullBooleanField()
    
    