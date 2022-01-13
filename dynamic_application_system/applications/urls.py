from django.urls import path

from . import views

app_name = 'applications'
urlpatterns = [
    path('', views.home, name='home'),

    path('applications/', views.IndexView.as_view(), name='index'),
    path('applications/specifics/<int:application_id>/', views.detail, name='detail'),
    path('applications/<int:application_id>/approve/', views.approve, name='approve'),
    path('applications/<int:application_id>/decline/', views.decline, name='decline'),
    path('applications/<int:application_id>/delete/', views.delete, name='delete'),    
    path('applications/new/', views.new_application, name='new_application'),
    path('applications/statistics/', views.application_stats, name='statistics'),
    path('applications/approved/', views.approved_applications, name='approved_applications'), # Personnel Department

    path('carriers/', views.choose_carrier, name='choose_carrier'), # Citizen
    path('carriers/new/', views.new_carrier, name='new_carrier'), # Manager
    
    path('about/', views.about, name='about'),
]