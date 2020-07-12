
from django.urls import reverse, reverse_lazy
from django.conf import settings
import datetime
import requests
from get_file import get_data_file
import os
from django.core.wsgi import get_wsgi_application

try: 
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cotacoes_bc.settings')
    """Pegando a entrada do usuário para buscar a melhor cotação do dia frente ao U$"""
    date_param = input('\nDigite a data desejada (YYYYMMDD): ')
    print(f'\nData escolhida: {date_param}')
    
    requests.get(reverse_lazy('api:get_cotation', date_param))

except UnicodeDecodeError as err:
    print("\nMelhor cotação: x\n")

except Exception as err:
    print(f"\nFalha na tentativa de consulta dos dados {err}!\n")