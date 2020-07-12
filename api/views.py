from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from scripts.get_file import get_data_file

def get_cotation(request, date_param):
    """
    Chamando o script que irá fazer todo o trabalho em background;
    O script irá acessar o site do Banco Central e baixar o arquivo de dados de cotaçõs baseado na data solicitada
    Irá fazer todo o tratamento na informação e retornará a resposta para quem solicitou
    """
    response = get_data_file(date_param)

    if 'error' not in response:
        return JsonResponse(response)
    return JsonResponse(response)

    