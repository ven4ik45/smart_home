from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementsSerializer, DetailSensorSerializer


class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorId(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = DetailSensorSerializer


class Measurements(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
