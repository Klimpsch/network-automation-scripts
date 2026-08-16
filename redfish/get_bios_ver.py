#!/usr/bin/env python3
# Get BIOS version from Dell iDRAC via Redfish API.

import requests
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_bios_version(host, user, password):
    url = f"https://{host}/redfish/v1/Systems/System.Embedded.1"
    resp = requests.get(url, auth=(user, password), verify=False, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data.get("BiosVersion", "Unknown")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get iDRAC BIOS version")
    parser.add_argument("--host", required=True, help="iDRAC IP/hostname")
    parser.add_argument("--user", default="root", help="iDRAC username")
    parser.add_argument("--password", required=True, help="iDRAC password")
    args = parser.parse_args()

    version = get_bios_version(args.host, args.user, args.password)
    print(f"{args.host} BIOS Version: {version}")
