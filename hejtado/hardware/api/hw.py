from ..thermometer.thermometer import Thermometer
from hejtado.hardware.hardware import thermometers_section

hardware = {}
quido = {'id': 1,
         'name': 'quido',
         'status': 'ok',
         'relays': [{'id': 1,
                    'status': 'on',
                    'name': 'prodluzovacka',
                    'type': 'boolean'},
                   {'id': 2,
                    'status': 'on',
                    'name': 'ling-reset',
                    'type': 'boolean'},
                   {'id': 3,
                    'status': 'off',
                    'name': 'tepla-voda',
                    'type': 'timer'},
                   ],
         }


hardware[quido['id']] = quido

def get(hw):
    return list(hardware.values())

def get_hw():
    return list(hardware.values())

def get_quido(hwID):
    return quido

def get_thermometer(tmID):

    thermometer = Thermometer(tmID)
    temperature = thermometer.get_temperature()

    thermometer = {'id': tmID,
                    'name': thermometers_section[(tmID-1)]['name'],
                    'status': thermometers_section[(tmID-1)]['status'],
                    'temperature': temperature}

    return thermometer

def search():
    return list(hardware.values())

