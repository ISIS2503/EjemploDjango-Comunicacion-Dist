from django.http import HttpResponse
import json
from ..logic.logic_measurements import add_measurement, get_measurement_by_id, find_sensor_mesurements
from django.core import serializers
import requests


def post_measurement(request):
    data = request.body.decode('utf-8')
    diccionario = json.loads(data)
    rpta = 'The measurement was added correctly'
    try:
        add_measurement(diccionario)
    except Exception as e:
        rpta = e
    return HttpResponse(rpta)


def get_sensor_measurements(request, sensor_code):
    URL = "http://localhost:4000/places/sensors/"+sensor_code
    httpRes = requests.get(url=URL)
    response = ''
    try:
        sensor = httpRes.json()
        measurements = find_sensor_mesurements(sensor_code)
        response = serializers.serialize('json', measurements)
    except Exception as e:
        response = 'The sensor does not exists'
    return HttpResponse(response)
