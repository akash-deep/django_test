from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testapp(request):
    name = "testapp"
    html = "<html><body> Hi %s, this worked...!!</body></html>" % name
    return HttpResponse(html)
