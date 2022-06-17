from django.shortcuts import redirect, render, reverse
from django.views import generic
from .forms import Registration


class Home(generic.TemplateView):
    template_name = 'index.html'
    

class Register(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = Registration
    
    def get_success_url(self):
        return reverse('django:home')