from django.core.mail import send_mail
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.base import View
from .models import Application, Citizen
from .forms import ApplicationForm

import datetime

# Panagiotis Bellias
def home(request):
    return render(request, 'applications/home.html')

class IndexView(generic.ListView):
    template_name = 'applications/index.html'
    context_object_name = 'latest_applications_list'

    def get_queryset(self):
        """Return the last five published applications."""
        return Application.objects.order_by('-pub_date')[:5]

def detail(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    return render(request, 'applications/detail.html', {'application': application})

def approve(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    # Approve Logic
    '''
    send_mail(
        'Your application is approved!',
        'Dear user, your application has been approved\nThank you for using this service\nHave a great day!',
        'belliaspanagiotis@gmail.com',
        ['belliaspan@gmail.com'], # Testing
        auth_password='password',
        fail_silently=False,
    )'''
    return HttpResponse("You're approving application %s." % application_id)

def decline(request, application_id):
    return HttpResponse("You're declining application %s." % application_id)

def delete(request, application_id):
    return HttpResponse("You're deleting application %s." % application_id)

def gen_id(entity_type):
    id = 1
    if entity_type == "Application":
        application_set = Application.objects.all()
        print(application_set)
        print(application_set.iterator())
        for application in application_set.iterator():
            temp_id = application.id
            if id != temp_id:
                return id
        return temp_id + 1
    else:
        citizen_set = Citizen.objects.all()
        print(citizen_set)
        print(citizen_set.iterator())
        for citizen in citizen_set.iterator():
            temp_id = citizen.id
            if id != temp_id:
                return id
        return temp_id + 1

def new_application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            your_name = form.cleaned_data['your_name']
            your_job = form.cleaned_data['your_job']
            headline = form.cleaned_data['headline']

            for content_field in form.get_content_fields():
                print(content_field.get_value())

            print(f"ATTENTION! {your_name},{your_job},{headline},{content}")
            
            c_id = gen_id("Citizen")
            print(c_id)
            a_id = gen_id("Application")
            print(a_id)
            if c_id != -1 and a_id != -1:
                citizen = Citizen(c_id, your_name, your_job)
                citizen.is_active = True
                citizen.save()
                application = Application(a_id, datetime.datetime.now(), headline, content, citizen)
                application.is_active = True
                application.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('applications:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationForm()

    return render(request, 'applications/new_application.html', {'form': form})

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
