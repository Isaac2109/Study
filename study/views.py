from django.urls import reverse
from django.shortcuts import render, HttpResponsePermanentRedirect
from api import consulta_api

def home(request):
    if request.method == 'POST':
        return HttpResponsePermanentRedirect(reverse(test))
    else:
        return render(request, 'study/home.html')
    
def test(request):
    
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

    qtd_questoes = request.POST.get('qtd_questoes')

    contexto = {
        'qtd_questoes': qtd_questoes,
        'n': range(1, int(qtd_questoes) + 1)
    }

    for num in range(1, int(qtd_questoes) + 1):
        resp_user = request.POST.get(f'alter_{num}')
        resposta = request.POST.get(f'resp{num}')

        contexto.update({f"resp_user{num}": resp_user})
        contexto.update({f"resposta{num}": resposta})



    return render(request, 'study/result.html', context=contexto)