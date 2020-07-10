import datetime
import requests
"""Utilizando a biblioteca pandas para trabalhar com os dados"""
import pandas as pd
from lookup_tables import lookup_table_coin

"""
    Analisar a possibilidade de ter uma API onde os dados serão coletados à partir da entrada do usuário
    Existiria um script separado que, de tempos em tempos, baixaria o arquivo e filtraria a melhor cotação
    Ou a consulta pode ser feita em tempo real
"""

def get_best_cotation(file):
    """Funcao responsável por criar o DataFrame, ordenar os dados e obter a melhor cotação do dia"""
    # Criando o DataFrame para ordenar os dados
    df = pd.read_csv(dir_file, sep=";")
    # Apagar a ultima linha dos dados
    df.drop(df.tail(1).index,inplace=True)
    # Ordenando os dados do dataframe
    df1 = df.sort_values(by='cot_dolar_compra', ascending=True)
    # Filtrando apenas a primeira linha dos dados
    return df1.head(1)



try: 
    """Pegando a entrada do usuário para buscar a melhor cotação do dia frente ao U$"""
    date_param = input('\nDigite a data desejada (YYYYMMDD): ')
    print(f'\nData escolhida: {date_param}')
    url_get_file = f"https://www4.bcb.gov.br/Download/fechamento/{date_param}.csv"

    if len(date_param) == 8: 
        request_file = requests.get(url_get_file)
        http_response = request_file.status_code
        request_content = request_file.content.decode(encoding="utf8")
        title = "data;cod;tipo;moeda;cot_real_compra;cot_real_venda;cot_dolar_compra;cot_dolar_venda"
        dir_file = f"../files/file_{date_param}.csv"

        with open(dir_file, 'w+') as file:
            file.write(f'{title}\n')
            file.write(request_content)
        best_cotation = get_best_cotation(dir_file)
        print(f'\n{best_cotation}')
        # Separando os valores que iremos utilizar
        coin = best_cotation.values[0][3]
        cot_dolar_compra = best_cotation.values[0][6]
        # Pegando o símbolo e país da moeda
        result = lookup_table_coin(coin)[0]
        symbol = result[1]
        country = result[3]

        print(f"\Menor cotação frente ao U$: {symbol}, {country}, {cot_dolar_compra}\n")
    
    else:
        print(f"\nFormato de data inválido, por favor digite a data no formato YYYYMMDD\n")

except UnicodeDecodeError as err:
    print("\nMelhor cotação: x\n")

except Exception as err:
    print("\nFalha na tentativa de consulta dos dados!\n")