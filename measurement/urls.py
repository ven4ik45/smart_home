from django.urls import path, include
from rest_framework import routers

from measurement.views import Sensors, SensorId, Measurements

router = routers.DefaultRouter()

urlpatterns = [
    path('sensors/', Sensors.as_view()), # получение, добавление датчиков: GET, POST
    path('sensors/<pk>/', SensorId.as_view()), # конкретный ид сенсора GET, PATH
    path('measurements/', Measurements.as_view()), # добавление измерения для датчика: POST
]
