from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Application
from .forms import ApplicationForm


class ApplicationsView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return self.request.user.user_applications.all()


class CreateApplicationsView(LoginRequiredMixin, CreateView):
    queryset = Application.objects.all()
    form_class = ApplicationForm
    template_name = 'create_app.html'
    success_url = reverse_lazy('applications:index')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)