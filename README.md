# README: Script de Busca de Voos

## Descrição
Este script Python automatiza a busca de voos usando a API do Skyscanner. Ele agenda e executa tarefas diárias de busca, coletando informações sobre itinerários e preços, e armazena os dados em um arquivo CSV.

## Requisitos
- Python 3
- Bibliotecas: requests, json, pandas, datetime, schedule, time, python-dotenv
- Chave de API do Skyscanner

## Configuração
1. Instale as dependências necessárias usando pip:
   pip install requests pandas python-dotenv schedule
2. Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Skyscanner:
   API_KEY='SuaChaveAPIAqui'

## Uso
Para executar o script, use o comando no terminal:
python nome_do_script.py
O script irá agendar e executar a tarefa de busca de voos a cada hora, salvando os resultados em um arquivo CSV na pasta bases.

## Estrutura do Script
- criar_pesquisa(): Realiza a requisição à API do Skyscanner para buscar voos.
- tarefa_agendada(): Gera datas de busca, itera sobre diferentes combinações de aeroportos e executa a busca de voos.

## Notas Adicionais
- Substitua nome_do_script.py pelo nome real do seu arquivo de script.
- O script usa a biblioteca schedule para agendar tarefas. Ajuste a frequência conforme necessário.
- A chave de API do Skyscanner deve ser obtida através do cadastro no portal de desenvolvedores do Skyscanner.