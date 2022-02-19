from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def  date_time_view(request):
    time=datetime.datetime.now()
    s = '<h1> Hello Current Date and Time:'+str(time)+'</h1>'
    return HttpResponse(s)
