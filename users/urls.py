from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path(r'reg/', views.RegisterView.as_view(), name='reg'),
    path(r'log/', views.LoginView.as_view(), name='log'),
]