from ..models import Room, Building, Sensor
from django.db import models


def add_room(diccionario):
    room = Room()
    room.floor = diccionario['floor']
    room.code = diccionario['code']
    building_name = diccionario['code'].split("-")[0]
    room.building = Building.objects.get(name=building_name)
    room.save()


def find_room_by_code(p_code):
    return Room.objects.get(code=p_code)
