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

            contexto = {
                'qtd_questoes': qtd_questoes
            }

            for num in range(1, int(qtd_questoes) + 1):
                contexto.update({f"cabecalho_{num}": consulta[f"{num}"]["cabeçalho"]})
                contexto.update({f"alter_a_{num}": consulta[f"{num}"]["alternativa_a"]})
                contexto.update({f"alter_b_{num}": consulta[f"{num}"]["alternativa_b"]})
                contexto.update({f"alter_c_{num}": consulta[f"{num}"]["alternativa_c"]})
                contexto.update({f"alter_d_{num}": consulta[f"{num}"]["alternativa_d"]})
                contexto.update({f"resp{num}": consulta[f"{num}"]["resposta"]})

                

            return render(request, 'study/test.html', context=contexto)

    else:
        form = MeuForm()
        return render(request, 'study/home.html', {'form': form})
    
def result(request):
    pass
