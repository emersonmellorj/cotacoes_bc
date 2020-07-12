from django.db import models

class Cotations(models.Model):
    cod = models.IntegerField(default=0)
    type_coin = models.CharField(max_length=5, null=False, blank=False)
    coin_name = models.CharField(max_length=50, null=False, blank=False)
    buy_real_cotation = models.FloatField(name="buy_real_cotation")
    sale_real_cotation = models.FloatField(name="sale_real_cotation")
    buy_dolar_cotation = models.FloatField(name="buy_dolar_cotation")
    sale_dolar_cotation = models.FloatField(name="sale_dolar_cotation")
    insert_date = models.DateTimeField(name="insert_date", auto_now_add=True)
    updated_date = models.DateTimeField(name="updated_date", auto_now=True)

    def __str__(self):
        return f'{self.coin_name}'


class BetterCotation(models.Model):

    name = models.CharField(name='name', max_length=50, null=False, blank=False)
    symbol = models.CharField(name='symbol', max_length=5, null=False, blank=False)
    country = models.CharField(name='country', max_length=50, null=False, blank=False)
    cotation = models.FloatField(name='cotation')
    insert_date = models.DateTimeField(name="insert_date", auto_now_add=True)
    updated_date = models.DateTimeField(name="updated_date", auto_now=True)

    def __str__(self):
        return f'{self.name}'