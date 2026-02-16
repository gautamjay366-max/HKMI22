from django.urls import path
from .views import *


urlpatterns = [
    path('', events_home, name='events'),
]