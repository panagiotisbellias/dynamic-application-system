from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic
from django.views.generic.base import View
from .models import Application

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
