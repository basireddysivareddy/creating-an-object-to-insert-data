from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='Cricket')
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    LWO=Webpage.objects.filter(name__startswith='s')
    LWO=Webpage.objects.filter(name__endswith='d')
    LWO=Webpage.objects.filter(name__contains='s')
    LWO=Webpage.objects.filter(name__in=('REDDY','MSD'))
    LWO=Webpage.objects.filter(name__regex='^R\w{4}')
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='m'))
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(topic_name='Foot Ball') | Q(url__endswith='in'))





    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date='1999-12-06')
    LAO=AccessRecords.objects.filter(date__year='1999')
    LAO=AccessRecords.objects.filter(date__month='10')
    LAO=AccessRecords.objects.filter(date__day='10')
    LAO=AccessRecords.objects.filter(date__gt='1999-12-06')
    LAO=AccessRecords.objects.filter(date__gte='1999-12-06')
    LAO=AccessRecords.objects.filter(date__lt='1999-12-06')
    LAO=AccessRecords.objects.filter(date__lte='1999-12-06')




    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)
