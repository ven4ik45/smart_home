from django.urls import path, include
from rest_framework import routers

from measurement.views import Sensors, SensorId, SensorUpdate, Measurements

router = routers.DefaultRouter()

urlpatterns = [
    path('sensors/', Sensors.as_view()),
    # path('sensor_create/', SensorCreate.as_view()),
    path('sensors/<pk>/', SensorId.as_view()),
    path('sensor_update/<pk>/', SensorUpdate.as_view()),
    path('measurements/', Measurements.as_view()),
]
