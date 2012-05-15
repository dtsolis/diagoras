from diagoras.extras.models import *
from diagoras.settings import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
from datetime import datetime
from django.db import connection, transaction
from django.core import mail
from smtplib import SMTP
from email.MIMEText import MIMEText

# inserting...
def saveMessage(name, email, subj, msg):
    message = ""
    try:
        m = Messages(sndrName=name, sndrEmail=email, subject=subj, message=msg, date=datetime.now(), read=0, send=0)
        m.save()
    except:
        message = "error occured....."
    return message

def addForwardMessage(fTo, fFrom, pFrom, smtp, port, enable):
    message = ""
    try:
        f = Forward_Message(forwardTo=fTo, forwardFrom=fFrom, passwordFrom=pFrom, smtpServer=smtp, smtpPort=port, enableForward=enable)

        f.save()
    except:
        message = "error occured..."


# deleting...
def deleteMessage(message_id):
    message = ""
    try:
        m = Messages.objects.get(pk=message_id)
        m.delete()
    except e:
        message = e
    return message

def deleteManyMessages(id_list):
    message = ""
    try:
        Messages.objects.filter(pk__in=id_list).delete()
    except e:
        message = e
    return message

def deleteForwardEntry(forward_id):
    message = ""
    try:
        m = Forward_Message.objects.get(pk=forward_id)
        m.delete()
    except e:
        message = e
    return message

def deleteForwardList(id_list):
    message = ""
    try:
        Forward_Message.objects.filter(pk__in=id_list).delete()
    except e:
        message = e
    return message


# updating...
def markMessage(message_id, read):
    message = ""
    try:
        m = Messages.objects.get(pk=message_id)
        m.read = read
        m.save()
    except e:
        message = e
    return message

def markMessageList(id_list, rd):
    message = ""
    try:
        Messages.objects.filter(pk__in=id_list).update(read=rd)
    except e:
        message = e
    return message

def enableDisableForward(id_list, enable):
    message = ""
    try:
        Forward_Message.objects.filter(pk__in=id_list).update(enableForward=enable)
    except e:
        message = e
    return message
    
def updateForward(id, fto, ffrom, passfrom, smtp, port, enable):
    message = ""
    try:
        u =  Forward_Message.objects.get(pk=id)
        u.forwardTo = fto
        u.forwardFrom = ffrom
        u.passwordFrom = passfrom
        u.smtpServer = smtp
        u.smtpPort = port
        u.enableForward = enable
        u.save()
    except e:
        message = e
    return message

# getting...
def getMessageList():
    return Messages.objects.values('idmessage', 'sndrName', 'subject', 'date', 'read').order_by('-date')

def getMessageDetails(idmessage):
    return Messages.objects.get(pk=idmessage)

def getForwardList():
    return Forward_Message.objects.all()

def getForwardDetails(idforward):
    return Forward_Message.objects.get(pk=idforward)



# other...
def sendEmail():
    msg = ""
    m = Messages.objects.filter(send=0)
    e = Forward_Message.objects.filter(enableForward=1)
    for forward in e:
        body = ''
        for message in m:
            body += message.sndrName + ' left a message on ' + message.date.strftime("%A, %d %B %Y, %I:%M%p") + '\nSubject: ' + message.subject +'\n\n'
            
        
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = 'Diagoras - New message(s)'
        
        try:
            s = SMTP()
            s.connect(forward.smtpServer)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(forward.forwardFrom,forward.passwordFrom)
            s.sendmail(forward.forwardFrom, forward.forwardTo, msg.as_string())
            s.quit()
        except Exception:
            msg = Exception;
            
    # mark all messages as send
    Messages.objects.filter(send=0).update(send=1)
        
    return msg