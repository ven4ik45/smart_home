from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementsSerializer, DetailSensorSerializer, \
    SensorUpdateSerializer

# class Sensors(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer

# class SensorCreate(CreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer


class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer


class SensorId(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = DetailSensorSerializer


class Measurements(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
