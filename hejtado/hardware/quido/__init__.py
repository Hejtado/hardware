from pysnmp.hlapi import *

class Quido:
    """Handle communication with Quido box"""

    def __init__(self, quido_id):
        self.quido_ip = '192.168.2.241'
        self.quido_id = quido_id

    def __create_data_structure(self):
        """Create datastructure to hold Quido values"""

        quido = {'id': self.quido_id,
                 'name': 'quido',
                 'status': False,
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


    def get_temperature(self, tmID):
        """Get the temperature of thermometer connected to the Quido"""
        temperature_obj = self.__snmp_get('1.3.6.1.4.1.18248.16.1.1.0')
        temperature = float(temperature_obj[1][1]) / 10
        # In case of negative temperature, please see Modbus and pyminimalmodbus documentation
        if temperature > 6000:
            temperature = temperature - 6553.6
        return temperature

    def get_relay(self, relayID):
        """Get the status of the realy"""
        print("SNMPGET returned {}".format(self.__snmp_get(relayID)))

    def set_relay(self, relayID, desired_state):
        """Set the status of the relay"""

        oid = "1.3.6.1.4.1.18248.16.3.1.1.1." + str(relayID)
        desired_state_value = 0

        if desired_state == 'on':
            desired_state_value = 1

        errorIndication, errorStatus, errorIndex, varBinds = next(
            setCmd(SnmpEngine(),
                   CommunityData('private', mpModel=0),
                   UdpTransportTarget((self.quido_ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid), Integer(int(desired_state_value))))
        )
        if errorIndication:
            return False
        else:
            return True

    def __snmp_get(self, oid):
        """Get Quido Relay information using SNMP"""
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData('private', mpModel=0),
                   UdpTransportTarget((self.quido_ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid)))
        )

        for varBind in varBinds:
            return (True, varBind)

    def __snmp_set(self):
        pass