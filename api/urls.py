from .views import get_cotation
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('get_cotation/<str:date_param>', get_cotation, name='get_cotation')
]


