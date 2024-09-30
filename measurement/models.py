from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor_id = models.ForeignKey(Sensor,
                                  on_delete=models.CASCADE,
                                  related_name='measurements',
                                  null=True)
