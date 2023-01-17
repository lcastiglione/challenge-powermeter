from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Measurer, Measurement
from datetime import date
import json


# Lista de errores recibidos por la base de datos
error_messages = {
    'repat_measurer': {'key': ['measurer with this key already exists.']},
    'invalid_measurer': {'measurer': ['Invalid pk "med2" - object does not exist.']},
    'negative_kwh': {'consumption_kwh': ['Ensure this value is greater than or equal to 0.0.']},
}


# Lista de potencias para realizar cálculos
list_kwh = [10, 20, 30]


class MeasurerTestCase(TestCase):
    def setUp(self):
        # Medidor usado para verificar cálculos de potencias
        measurer = Measurer(key='med1',name='Medidor 1')
        measurer.save()
        [Measurement(consumption_kwh=a,measurer=measurer).save() for a in list_kwh]

    def test_create_measurer(self):
        client = APIClient()
        data = {
            "key": "med2",
            "name": "Medidor 2"
        }
        response = client.post('/api/measurer/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), data)

    def test_create_repeat_measurer(self):
        client = APIClient()
        data = {
            "key": "med1",
            "name": "Medidor 1"
        }
        response = client.post('/api/measurer/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content),
                         error_messages['repat_measurer'])

    def test_get_min_consumption(self):
        client = APIClient()
        response = client.get('/api/measurer/med1/min-consumption/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
                         "min_consumption": min(list_kwh)})

    def test_get_max_consumption(self):
        client = APIClient()
        response = client.get('/api/measurer/med1/max-consumption/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
                         "max_consumption": max(list_kwh)})

    def test_get_total_consumption(self):
        client = APIClient()
        response = client.get('/api/measurer/med1/total-consumption/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
                         "total_consumption": sum(list_kwh)})

    def test_get_average_consumption(self):
        client = APIClient()
        response = client.get('/api/measurer/med1/average-consumption/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
                         "average_consumption": sum(list_kwh)/len(list_kwh)})


class MeasurementTestCase(TestCase):
    def setUp(self):
        # Crear medidor para cargar mediciones
        measurer = Measurer(key='med1',name='Medidor 1')
        measurer.save()

    def test_create_measurerement(self):
        client = APIClient()
        data = {
            "consumption_kwh": 10.5,
            "measurer": "med1"
        }
        response = client.post('/api/measurement/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content)
        self.assertEqual(result['created_at'].split('T')[0], f"{date.today()}")
        del result['created_at']
        self.assertEqual(result, data)

    def test_create_measurement_bad_measurer(self):
        client = APIClient()
        data = {
            "consumption_kwh": 10.5,
            "measurer": "med2"
        }
        response = client.post('/api/measurement/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content),
                         error_messages['invalid_measurer'])

    def test_create_measurement_negative_kwh(self):
        client = APIClient()
        data = {
            "consumption_kwh": -2,
            "measurer": "med1"
        }
        response = client.post('/api/measurement/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content),
                         error_messages['negative_kwh'])
