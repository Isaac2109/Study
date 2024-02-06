from senha import API_KEY
import requests
import json

def consulta_api(dificuldade, assunto):
    headers = {"authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        'model': id_modelo,
        'messages': [
            {'role': 'user','content': f"""Faça uma questão {dificuldade} 
            sobre {assunto} com 4 alternativas de resposta, 
            com o cabeçalho da questão salvo em uma variável python 
            por nome cabeçalho e as alternativas salvas cada uma em uma variável python 
            e uma variável python por nome resposta contendo a questão correta """}
        ]
    }

    body_mensagem = json.dumps(body_mensagem)

    requisição = requests.post(link, headers=headers, data=body_mensagem)
    print(requisição)
    print(requisição.text)

