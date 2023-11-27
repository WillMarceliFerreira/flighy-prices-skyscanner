import requests
import json
import pandas as pd
import datetime
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Substitua pela sua chave de API
api_key = os.getenv('API_KEY')

def criar_pesquisa(origem, destino, data):
    url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"
    headers = {'x-api-key': api_key}
    ano, mes, dia = data.year, data.month, data.day
    data = {
        "query": {
            "market": "BR",
            "locale": "pt-BR",
            "currency": "BRL",
            "query_legs": [
                {
                    "origin_place_id": {"iata": origem},
                    "destination_place_id": {"iata": destino},
                    "date": {"year": ano, "month": mes, "day": dia}
                }
            ],
            "adults": 1,
            "cabin_class": "CABIN_CLASS_ECONOMY"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Falha na requisição", "status_code": response.status_code}

def tarefa_agendada():
    # Gere um intervalo de datas usando pandas
    start_date = datetime.datetime.now().date()
    end_date = '2024-04-30'
    datas = pd.date_range(start_date, end_date)

    aeroportos_sp = ['GRU', 'CGH', 'VCP']
    aeroportos_nz = ['AKL', 'WLG', 'CHC']

    dados_voos = []

    # Iterar sobre todas as datas e aeroportos
    for data in datas:
        for origem in aeroportos_sp:
            for destino in aeroportos_nz:
                resposta = criar_pesquisa(origem, destino, data)

                itinerarios = resposta.get('content', {}).get('results', {}).get('itineraries', {})
                for id, detalhes in itinerarios.items():
                    data_viagem = data.strftime('%Y-%m-%d')
                    horario = datetime.datetime.now().hour
                    dia_semana = datetime.date.today().weekday()
                    for opcao in detalhes.get('pricingOptions', []):
                        preco = int(opcao['price']['amount']) / 1000
                        deep_link = opcao['items'][0]['deepLink']
                        dados_voos.append([data_viagem, dia_semana, horario, origem, destino, preco, deep_link])

    # Criar DataFrame
    df_voos = pd.DataFrame(dados_voos, columns=['Data', 'Dia da Semana', 'Horário', 'Origem', 'Destino', 'Preço', 'Deep Link'])

    # Salvar o DataFrame em um arquivo CSV
    df_voos.to_csv(f'./bases/dados_voos_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv', index=False)

# Agendar a tarefa para rodar a cada hora
print(f'Rodando {datetime.datetime.now().hour}')
schedule.every(1).hours.do(tarefa_agendada)

while True:
    schedule.run_pending()
    time.sleep(1)