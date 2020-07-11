from django.shortcuts import render
from rest_framework import viewsets

from scripts.get_file import get_data_file

# Create your views here.
def get_cotations(request, date_param):
    
    """Primeiramente irei buscar o arquivo mais novo no site do Banco Central"""
    get_data_file(date_param)
    queryset = Cotation.objects.filter()
    