from django.test import TestCase
from ..models import Cotations, BetterCotation
from model_mommy import mommy

class CotationTestCase(TestCase):
    """Testando o model Cotations"""
    def setUp(self):
        cotation = mommy.make('Cotations', coin_name='Dólar')

    def test_new_cotation(self):
        get_cotation = Cotations.objects.first()
        self.assertEquals('Dólar', str(get_cotation))

class CotationsTestCase(TestCase):
    """Testando o model BetterCotation"""
    def setUp(self):
        new_cotation = mommy.make('BetterCotation', name='Real', symbol='R$')

    def test_get_new_cotation(self):
        get_new_cotation = BetterCotation.objects.first()
        self.assertEquals('Real', str(get_new_cotation))
        self.assertEquals('R$', get_new_cotation.symbol)
