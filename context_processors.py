# edw mporw na balw oti synartisi thelw kai na epistrefoun global metablites
# gia na doulepsei, tha prepei na dilwsw sto 'settings.py' tin synartisi ws eksis
#
# TEMPLATE_CONTEXT_PROCESSORS = ('diagoras.context_processors.onoma_synartisis',)

from diagoras.extras.models import Messages

def getUnreadCount(request):
    a = Messages.objects.filter(read='0').count()
    return { 'unreadMessages': a }