from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import MeuForm

def home(request):
    form = MeuForm
    return render(request, 'study/home.html', {'form': form})