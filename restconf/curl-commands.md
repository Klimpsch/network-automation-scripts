# RESTCONF curl cheat-sheet — IOS XE 17.18

All commands are **read-only GETs** — safe to run and repeat. Replace `192.168.122.110` and `admin:Cisco123` with your own. To not pass a password in plain text just use 'admin' and you will be prompted for password by curl without it being saved to history.

Common flags used throughout:
- `-s` silent, `-k` skip cert check (self-signed IOS cert), `-u` basic auth
- `-H "Accept: application/yang-data+json"` asks for JSON (use `+xml` if you prefer XML)
- Pipe to `| jq` for readable output (install `jq` if you haven't)

Set these once so the commands below stay short:

```bash
export DEV=
export AUTH=
export ACC='Accept: application/yang-data+json'
```

---



# Confirm Alive
curl -sk -u $AUTH "https://$DEV/restconf/" -H "$ACC" | jq

# List all yang modules
curl -sk -u $AUTH "https://$DEV/restconf/data/ietf-yang-library:modules-state" -H "$ACC" | jq '.["ietf-yang-library:modules-state"].module[].name'

# Show interface data
curl -sk -u $AUTH "https://$DEV/restconf/data/ietf-interfaces:interfaces" -H "$ACC" | jq
## Interface state
curl -sk -u $AUTH "https://$DEV/restconf/data/ietf-interfaces:interfaces-state" -H "$ACC" | jq
## Richer interface stats
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces" -H "$ACC" | jq


## Single interface
curl -sk -u $AUTH "https://$DEV/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1" -H "$ACC" | jq

## Trim the fiels to just what you want
curl -sk -u $AUTH "https://$DEV/restconf/data/ietf-interfaces:interfaces-state?fields=interface(name;oper-status;out-error-pkts;last-change)" -H "$ACC" | jq

# CPU
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage" -H "$ACC" | jq

# Rest API
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-memory-oper:memory-statistics" -H "$ACC" | jq

# Platform componenets
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-platform-oper:components" -H "$ACC" | jq


# RIB
curl -sk -u $AUTH "https://$DEV/restconf/data/ietf-routing:routing-state" -H "$ACC" | jq
# ARP
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-arp-oper:arp-data" -H "$ACC" | jq
# BGP
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-bgp-oper:bgp-state-data" -H "$ACC" | jq

# OSPF
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-ospf-oper:ospf-oper-data" -H "$ACC" | jq

# CDP
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-cdp-oper:cdp-neighbor-details" -H "$ACC" | jq

# Config
curl -sk -u $AUTH "https://$DEV/restconf/data/Cisco-IOS-XE-native:native" -H "$ACC" | jq
