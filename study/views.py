from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from .forms import MeuForm
from api import consulta_api

def home(request):
    if request.method == 'POST':
        form = MeuForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['subject']
            dificuldade = form.cleaned_data['difficulty']

            consulta_api(dificuldade, assunto)

            return HttpResponseRedirect(reverse('test'))

    else:
        form = MeuForm()
        return render(request, 'study/home.html', {'form': form})

def test(request):
    return render(request, 'study/test.html')