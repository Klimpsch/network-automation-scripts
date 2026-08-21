import requests, urllib3
urllib3.disable_warnings()  # silence self-signed cert warnings (lab only)

url = ""
BASE = f"https://{url}:443/restconf/data"
HDRS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}
AUTH = ("", "")

# READ
r = requests.get(
    f"{BASE}/ietf-interfaces:interfaces/interface=GigabitEthernet2",
    headers=HDRS, auth=AUTH, verify=False,
)
print(r.status_code, r.json())

# PATCH — change ONLY the description, everything else preserved
payload = {"ietf-interfaces:interface":
           {"name": "GigabitEthernet2", "description": "uplink-to-core"}
           }

r = requests.patch(
    f"{BASE}/ietf-interfaces:interfaces/interface=GigabitEthernet2",
    headers=HDRS, auth=AUTH, json=payload, verify=False,
)
print(r.status_code)  # expect 204 No Content
