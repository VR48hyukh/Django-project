from django.contrib.auth import get_user_model
from django.db import models

class Sensor(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
class Temperature(models.Model):
    id=models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature=models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    date=models.DateTimeField(auto_now=True, verbose_name='Дата')
