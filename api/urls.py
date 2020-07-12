from .views import get_cotation, get_cotations_data
from django.urls import path

urlpatterns = [
    path('', get_cotations_data, name='cotations_list'),
    path('get_cotation/<str:date_param>', get_cotation, name='get_cotation')
]


