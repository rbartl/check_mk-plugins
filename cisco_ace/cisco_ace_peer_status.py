#!/usr/bin/env python

# Monitoring the HA status of a pair of Cisco ACE load balancers.
# Herward Cooper <coops@fawk.eu> - 2012

# We take the response 'OK - Peer is compatible' to mean HA is healthy
# Used OID .1.3.6.1.4.1.9.9.650.1.1.2.1.1.1

def inventory_cisco_ace_peer_status(checkname, info):
    inventory=[]
    status = int(info[0][0])
    if status < 11:
        inventory.append( (None, None) )
    return inventory


def check_cisco_ace_peer_status(item, params, info):
    state = int(info[0][0])
    if state == 8:
        return (0, "OK - Peer is compatible")
    else:
        return (2, "CRITICAL - Peer is not compatible!")
    return (3, "UNKNOWN - unhandled problem")

check_info["cisco_ace_peer_status"] = (check_cisco_ace_peer_status, "Cisco ACE Peer Status", 0, inventory_cisco_ace_peer_status)

snmp_info["cisco_ace_peer_status"] = ( ".1.3.6.1.4.1.9.9.650.1.1.2.1.1", [ "1" ] )