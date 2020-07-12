from django.test import TestCase, Client
from django.http import JsonResponse 

class GetCotationTestCase(TestCase):
    """Testando o retorno da solicitação da melhor cotação em determinada data"""
    def setUp(self):
        self.date_param = '20200710'
        self.client = Client()

    def test_get_cotation(self):
        response = self.client.get(f'/get_cotation/{self.date_param}')
        self.assertEquals(b'{"symbol": "P", "country": "Botswana", "cot_dolar_compra": "0,08610000"}', response.content)

    def test_get_cotation_error(self):
        response = self.client.get(f'/get_cotation/2020')
        self.assertEquals(b'{"error": "dados nao encontrados."}', response.content)


class GetCotationsDataTestCase(TestCase):
    """Testando o retorno da solicitação em um endpoint não desenvolvido"""
    def setUp(self):
        self.client = Client()

    def test_get_cotations(self):
        response = self.client.get('/')
        self.assertEquals(b'Este endpoint n\xc3\xa3o foi desenvolvido.', response.content)