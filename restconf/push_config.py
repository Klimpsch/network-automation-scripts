#!/usr/bin/env python3
"""Push an interface config to a RESTCONF-enabled device."""

import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Connection parameters ---
HOST = "R1"                # replace with the device IP/hostname
PORT = 443
USERNAME = "admin"
PASSWORD = "admin"
VERIFY_TLS = False         # set True with a valid cert in production

INTERFACE = "GigabitEthernet2"

url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces/interface={INTERFACE}"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "link-to-R2",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.0.12.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

def main():
    resp = requests.put(
        url,
        json=payload,
        headers=headers,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        verify=VERIFY_TLS,
        timeout=10,
    )

    # 201 = created, 204 = updated/no content
    if resp.status_code in (200, 201, 204):
        print(f"Success ({resp.status_code}): {INTERFACE} configured on {HOST}")
    else:
        print(f"Failed ({resp.status_code}) on {HOST}")
        print(resp.text)
        resp.raise_for_status()

if __name__ == "__main__":
    main()



""" Minimal Way of writing
import requests, urllib3
urllib3.disable_warnings()
BASE = "https://192.168.0.172:443/restconf/data"
HDRS = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+json"}
AUTH = ("admin", "Cisco123")

payload = {"ietf-interfaces:interface": {
    "name": "GigabitEthernet2",
    "description": "link-to-R2",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": True,
    "ietf-ip:ipv4": {"address": [{"ip": "10.0.12.1", "netmask": "255.255.255.0"}]},
}}
r = requests.put(f"{BASE}/ietf-interfaces:interfaces/interface=GigabitEthernet2",
                 headers=HDRS, auth=AUTH, json=payload, verify=False)
print(r.status_code)  # 201 created, 204 updated
"""
