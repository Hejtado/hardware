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
thermometer1 = {'id': 1,
                'name': 'ground_floor',
                'status': 'ok',
                'temperature': 23.0}

hardware[quido['id']] = quido

def get(hw):
    return list(hardware.values())

def get_hw():
    return list(hardware.values())

def get_quido(hwID):
    return quido

def get_thermometer(tmID):
    return thermometer1

def search():
    return list(hardware.values())

