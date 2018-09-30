from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
	html = "<html><body><h1>This is my home page</h1></body></html>"
	return HttpResponse(html)