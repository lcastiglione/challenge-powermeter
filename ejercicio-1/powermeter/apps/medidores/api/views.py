from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import action
from django.http import JsonResponse
from ..models import Measurer, Measurement
from .serializers import MeasurerSerializer, MeasurementSerializer


class MeasurerViewSet(
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):# GenericViewSet
    queryset=Measurer.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=MeasurerSerializer

    # mixins.CreateModelMixin genera el endpoint para crear un nuevo medidor

    @action(detail=True,methods=['get'], url_path='min-consumption', url_name='min_consumption')
    def min_consumption(self, *args, **kwargs):
        return MeasurerViewSet.get_response(self.get_object(),'min_consumption')

    # Se definen los endpoints para obtener los valores de consumo
    @action(detail=True,methods=['get'], url_path='max-consumption', url_name='max_consumption')
    def max_consumption(self, *args, **kwargs):
        return MeasurerViewSet.get_response(self.get_object(),'max_consumption')

    @action(detail=True,methods=['get'], url_path='total-consumption', url_name='total_consumption')
    def total_consumption(self, *args, **kwargs):
        return MeasurerViewSet.get_response(self.get_object(),'total_consumption')

    @action(detail=True,methods=['get'], url_path='average-consumption', url_name='average_consumption')
    def average_consumption(self, *args, **kwargs):
        return MeasurerViewSet.get_response(self.get_object(),'average_consumption')

    @staticmethod
    def get_response(obj, name):
        # Se agrupan las respuestas en una sola función para reducir código, nada más.
        return JsonResponse({name: getattr(obj,name)}, safe=False,status=status.HTTP_200_OK)


class MeasurementViewSet(
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # mixins.CreateModelMixin genera el endpoint para crear una nueva medidición