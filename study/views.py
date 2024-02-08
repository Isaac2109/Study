from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from api import consulta_api

def home(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse(test))
    else:
        return render(request, 'study/home.html')
    
def test(request):

    if request.method == 'POST':
        return HttpResponseRedirect(reverse(result))
    
    else:
    
        assunto = request.POST.get('assunto')
        dificuldade = request.POST.get('dificuldade')
        qtd_questoes = request.POST.get('qtd_questoes')
    
        consulta = consulta_api(dificuldade, assunto, qtd_questoes)  
    
        contexto = {
                'qtd_questoes': qtd_questoes,
                'n': range(1, int(qtd_questoes) + 1)
            }
        for num in range(1, int(qtd_questoes) + 1):
            contexto.update({f"cabecalho_{num}": consulta[f"{num}"]["cabeçalho"]})
            contexto.update({f"alter_a_{num}": consulta[f"{num}"]["alternativa_a"]})
            contexto.update({f"alter_b_{num}": consulta[f"{num}"]["alternativa_b"]})
            contexto.update({f"alter_c_{num}": consulta[f"{num}"]["alternativa_c"]})
            contexto.update({f"alter_d_{num}": consulta[f"{num}"]["alternativa_d"]})
            contexto.update({f"resp{num}": consulta[f"{num}"]["resposta"]})
    
        return render(request, 'study/test.html', context=contexto)


def result(request):
    return render(request, 'study/result.html')