#!/usr/bin/env python3
# Get running and pending (post-update) BIOS version from Dell iDRAC via Redfish. 

import requests
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_bios_versions(host, user, password):
    auth = (user, password)
    base = f"https://{host}/redfish/v1"

    # Running BIOS version
    sys_resp = requests.get(
        f"{base}/Systems/System.Embedded.1", auth=auth, verify=False, timeout=15
    )
    sys_resp.raise_for_status()
    running = sys_resp.json().get("BiosVersion", "Unknown")

    # Firmware inventory - find BIOS entries (Installed + Previous/Pending)
    inv_resp = requests.get(
        f"{base}/UpdateService/FirmwareInventory", auth=auth, verify=False, timeout=15
    )
    inv_resp.raise_for_status()
    members = inv_resp.json().get("Members", [])

    installed = None
    pending = None
    for m in members:
        oid = m["@odata.id"]
        if "BIOS" not in oid.upper():
            continue
        fw = requests.get(f"{base}{oid.split('/redfish/v1')[-1] and oid}",
                          auth=auth, verify=False, timeout=15)
        # simpler: fetch full URL
        fw = requests.get(f"https://{host}{oid}", auth=auth, verify=False, timeout=15)
        fw.raise_for_status()
        data = fw.json()
        ver = data.get("Version", "Unknown")
        if oid.startswith("/redfish/v1/UpdateService/FirmwareInventory/Installed"):
            installed = ver
        elif oid.startswith("/redfish/v1/UpdateService/FirmwareInventory/Previous"):
            pending = ver

    return running, installed, pending


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get iDRAC running + pending BIOS version")
    parser.add_argument("--host", required=True)
    parser.add_argument("--user", default="root")
    parser.add_argument("--password", required=True)
    args = parser.parse_args()

    running, installed, pending = get_bios_versions(args.host, args.user, args.password)
    print(f"{args.host}")
    print(f"  Running BIOS:   {running}")
    print(f"  Installed FW:   {installed}")
    print(f"  Previous FW:    {pending}")
