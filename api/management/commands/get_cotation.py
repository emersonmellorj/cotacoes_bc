from django.core.management.base import BaseCommand, CommandError

from django.urls import reverse, reverse_lazy
from django.conf import settings
import datetime
import requests
from scripts.get_file import get_data_file

class Command(BaseCommand):
    help = 'Faz uma consulta no site do Banco Central sobre a moeda de melhor cotação frente ao dólar na data escolhida.'

    def handle(self, *args, **options):
        try:
            """Pegando a entrada do usuário para buscar a melhor cotação do dia frente ao U$"""
            date_param = int(input('\nDigite a data desejada (YYYYMMDD): '))
            print(f'\nData escolhida: {date_param}')

            if isinstance(date_param, int):
                response = requests.get(f'http://localhost:8000/api/v1/get_cotation/{date_param}')

                if b'dados nao encontrados' not in response.content:
                    symbol = response.json().get('symbol')
                    country = response.json().get('country')
                    buy_cot_dolar = response.json().get('cot_dolar_compra')
                    print(f"\nMenor cotação frente ao U$: {symbol}, {country}, {buy_cot_dolar}\n")
                else:
                    raise FileNotFoundError
            else:
                raise TypeError('a data não pode conter letras, apenas números!')

        except (UnicodeDecodeError, FileNotFoundError) as err:
            self.stdout.write(self.style.ERROR("\nMelhor cotação frente ao U$: x\n"))

        except ValueError:
            self.stdout.write(
                self.style.ERROR(
                    f"\nFalha na tentativa de consulta dos dados: a data não pode conter letras, apenas números!\n"
                )
            )

        except Exception as err:
            self.stdout.write(self.style.ERROR(f"\nFalha na tentativa de consulta dos dados: {err}!\n"))
            
        self.stdout.write(self.style.SUCCESS('A melhor cotação frente ao dólar foi obtida com sucesso!'))