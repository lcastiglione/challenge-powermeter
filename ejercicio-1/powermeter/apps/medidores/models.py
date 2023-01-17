from django.core.validators import MinValueValidator
from django.db.models import CheckConstraint, Q
from django.db import models
from django.db.models import Avg, Max, Min, Sum


class Measurer(models.Model):
    key=models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=20)

    @property
    def min_consumption(self):
        return self.measurement_set.aggregate(Min('consumption_kwh'))['consumption_kwh__min'] or 0.0

    @property
    def max_consumption(self):
        return self.measurement_set.aggregate(Max('consumption_kwh'))['consumption_kwh__max'] or 0.0

    @property
    def total_consumption(self):
        return self.measurement_set.aggregate(Sum('consumption_kwh'))['consumption_kwh__sum'] or 0.0

    @property
    def average_consumption(self):
        return self.measurement_set.aggregate(Avg('consumption_kwh'))['consumption_kwh__avg'] or 0.0

    def __str__(self):
        return self.name

class Measurement(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    consumption_kwh=models.FloatField(validators=[MinValueValidator(0.0)])
    measurer=models.ForeignKey(Measurer, on_delete=models.CASCADE)

    class Meta:
        #Limita a valores flotantes mayores a 0
        constraints = (CheckConstraint(check=Q(consumption_kwh__gte=0.0),name='min_consumption_kwh'),)

    def __str__(self):
        return f"Consumo '{self.measurer}': {self.consumption_kwh}kwh"