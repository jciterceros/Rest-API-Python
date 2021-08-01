import requests


link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
requisicao = requests.get(link)

print(requisicao.json())

""" Resultado
{'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '5.228', 'low': '5.0758', 'varBid': '0.1305', 'pctChange': '2.57', 'bid': '5.2103', 'ask': '5.213', 'timestamp': '1627678795', 'create_date': '2021-07-30 21:00:01'}, 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '6.2013', 'low': '6.0331', 'varBid': '0.149', 'pctChange': '2.47', 'bid': '6.1859', 'ask': '6.1912', 'timestamp': '1627678797', 'create_date': '2021-07-30 21:00:01'}, 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '219.501', 'low': '200.567', 'varBid': '12604', 'pctChange': '6.24', 'bid': '214.55', 'ask': '214.6', 'timestamp': '1627742358', 'create_date': '2021-07-31 11:39:18'}}
"""

print()
lista = []
dados = requisicao.json()
lista.append(dados)
for cotacao in lista:
    for k,v in cotacao.items():
        print(k + " : "+str(v))

""" Resultado
USDBRL : {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '5.228', 'low': '5.0758', 'varBid': '0.1305', 'pctChange': '2.57', 'bid': '5.2103', 'ask': '5.213', 'timestamp': '1627678795', 'create_date': '2021-07-30 21:00:01'}
EURBRL : {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '6.2013', 'low': '6.0331', 'varBid': '0.149', 'pctChange': '2.47', 'bid': '6.1859', 'ask': '6.1912', 'timestamp': '1627678797', 'create_date': '2021-07-30 21:00:01'}
BTCBRL : {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '219.501', 'low': '200.567', 'varBid': '12604', 'pctChange': '6.24', 'bid': '214.55', 'ask': '214.6', 'timestamp': '1627742358', 'create_date': '2021-07-31 11:39:18'}
"""


from flask import Flask

app = Flask(__name__)

import pandas as pd

with pd.ExcelFile("Vendas2.xlsx") as xls:
    df1 = pd.read_excel(xls, sheet_name = 'Vendas')
    df2 = pd.read_excel(xls, sheet_name = 'Cadastro')
print(df1.head())
print(df2.head())

@app.route("/")
def faturamento():
    calculo_faturamentoTotal = float(df1["Valor Final"].sum())
    return {"Faturamento": calculo_faturamentoTotal}

app.run(debug=True)
