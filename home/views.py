from django.urls import reverse_lazy
from django.views.generic import FormView
from home.forms import HomeForm


# Create your views here.

class HomeView(FormView):
    template_name = 'home/home.html'
    form_class = HomeForm
    success_url = reverse_lazy('home:home')
