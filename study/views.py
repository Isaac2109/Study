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
            qtd_questoes = form.cleaned_data['number']

            consulta = consulta_api(dificuldade, assunto, qtd_questoes)  

            for num in range(int(qtd_questoes)):
                contexto = {
                    f'questao{num}': consulta[f'Questão{num}'],
                    'qtd_questoes': qtd_questoes
                }
                

            return render(request, 'study/test.html', context=contexto)

    else:
        form = MeuForm()
        return render(request, 'study/home.html', {'form': form})
