from decouple import config
import requests
import json

def consulta_api(dificuldade, assunto, qtd_questoes):
    API_KEY = config("API_KEY")
    headers = {"authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        'model': id_modelo,
        'messages': [
            {'role': 'user','content': f"""Faça exatamente {qtd_questoes} questão {dificuldade} 
            sobre {assunto} com 4 alternativas de resposta, 
            me retorne um json com seis chaves, 
            a primeira chave se chama cabeçalho 
            e o valor dela é o cabeçalho da questão, 
            os valores da segunda, terceira, quarta e quinta chave 
            que terão respectivamente o nome de 
            alternativa_a, alternativa_b, 
            alternativa_c e alternativa_d  
            serão as alternativas e o valor da sexta chave 
            que terá o nome de resposta 
            será o valor completo da questão correta, 
            esse json vai estar dentro de outro 
            com o número de cada questão, 
            não quero um código python"""}
        ]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisição = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisição.json()
    print(resposta["choices"][0]["message"]["content"])
    return json.loads(resposta["choices"][0]["message"]["content"])

