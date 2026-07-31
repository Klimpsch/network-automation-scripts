from ncclient import manager

device = {
    "host": "172.16.40.1",
    "port": 830,
    "username": "admin",
    "password": "Cisco123",
    "hostkey_verify": False,
    "device_params": {'name': 'csr'}
}

with manager.connect(**device) as m:
    # Iterate through all capabilities sent by the router during the Hello exchange
    for capability in m.server_capabilities:
        # Filter for Cisco-specific or IETF models
        if "ietf-ip" in capability or "Cisco-IOS-XE" in capability:
            print(capability)
