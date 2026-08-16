#!/usr/bin/env python3
# restore_restconf.py
import requests, urllib3, sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROUTER = "172.16.40.1"
USER   = "admin"
PASS   = "Cisco123!"
SOURCE = "flash:/working-config"

url = f"https://{ROUTER}/restconf/operations/cisco-ia:copy"
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept":       "application/yang-data+json",
}
body = {
    "cisco-ia:input": {
        "source":      SOURCE,
        "destination": "running-config",
    }
}

r = requests.post(url, auth=(USER, PASS), headers=headers, json=body, verify=False, timeout=60)
print(f"HTTP {r.status_code}")
print(r.text)
r.raise_for_status()
print("Restore issued OK.")
