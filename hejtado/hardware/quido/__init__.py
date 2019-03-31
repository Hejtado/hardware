from pysnmp.hlapi import *

class Quido:
    """Handle communication with Quido box"""

    def __init__(self, quido_id):
        self.quido_ip = '192.168.2.241'

    def get_temperature(self, tmID):
        """Get the temperature of thermometer connected to the Quido"""
        temperature_obj = self.__snmp_get('1.3.6.1.4.1.18248.16.1.1.0')
        return (float(temperature_obj[1][1]) / 10)

    def get_relay(self, relayID):
        """Get the status of the realy"""
        pass

    def set_relay(self, relayID):
        """Set the status of the relay"""
        return {}

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