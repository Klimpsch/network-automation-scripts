#!/usr/bin/env python3
# restore_netconf.py
from ncclient import manager

ROUTER = "172.16.40.1"
USER   = "admin"
PASS   = "Cisco123!"
SOURCE_URL = "flash:///working-config"   # NETCONF wants a URL form

COPY_RPC = f"""
<copy-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <target><running/></target>
  <source>
    <url xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">{SOURCE_URL}</url>
  </source>
</copy-config>
"""

with manager.connect(
    host=ROUTER, port=830,
    username=USER, password=PASS,
    hostkey_verify=False,
    device_params={"name": "iosxe"},
    timeout=60,
) as m:
    print("Connected. Capabilities:", len(m.server_capabilities))
    reply = m.dispatch(COPY_RPC)
    print(reply.xml)
    print("Restore issued OK.")
