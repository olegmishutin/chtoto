from django.urls import path
from . import views

app_name = 'applications'
urlpatterns = [
    path(r'', views.ApplicationsView.as_view(), name='index'),
    path(r'create-app/', views.CreateApplicationsView.as_view(), name='create-app')
]