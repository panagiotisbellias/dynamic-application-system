from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
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

# class DetailView(generic.DetailView):
#     model = Application
#     template_name = 'applications/detail.html'

def approve(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    return HttpResponse("You're approving application %s." % application_id)

def decline(request, application_id):
    return HttpResponse("You're declining application %s." % application_id)

def delete(request, application_id):
    return HttpResponse("You're deleting application %s." % application_id)

def gen_id(entity_type):
    id = 1
    if entity_type == "Application":
        application_set = Application.objects.all()
        for application in application_set.iterator():
            temp_id = application.id
            if id != temp_id:
                return id
        return temp_id + 1
    else:
        id = -1
    return id

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
            content = form.cleaned_data['content']
            
            c_id = gen_id("Citizen")
            a_id = gen_id("Application")
            if c_id != -1 and a_id != -1:
                citizen = Citizen(c_id, your_name, your_job)
                citizen.save()
                application = Application(a_id, datetime.datetime.now(), headline, content, citizen)
                application.save()
            # redirect to a new URL:
            return render(request, 'applications/index.html')

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
