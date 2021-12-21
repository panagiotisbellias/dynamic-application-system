from django.shortcuts import render
from django.http import HttpResponse
from .models import Application

# Panagiotis Bellias
def home(request):
    return render(request, 'applications/home.html')

def index(request):
    latest_applications_list = Application.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.content for a in latest_applications_list])
    return HttpResponse(output)

def detail(request, application_id):
    return HttpResponse("You're looking at application %s." % application_id)

def approve(request, application_id):
    return HttpResponse("You're approving application %s." % application_id)

def decline(request, application_id):
    return HttpResponse("You're declining application %s." % application_id)

def delete(request, application_id):
    return HttpResponse("You're deleting application %s." % application_id)

def new_application(request):
    return HttpResponse("Hello, world. You're at the applications new_application.")

def application_stats(request):
    return HttpResponse("Hello, world. You're at the applications application_stats.")

def approved_applications(request):
    return HttpResponse("Hello, world. You're at the applications approved_applications.")

def choose_carrier(request):
    return HttpResponse("Hello, world. You're at the applications choose_carrier.")

def new_carrier(request):
    return HttpResponse("Hello, world. You're at the applications new_carrier.")

def about(request):
    return HttpResponse("Hello, world. You're at the applications about.")
