import xmltodict
import json

# path to xml data
output = "interface_data.xml"


with open(output, "r") as xml_file:
    # xmltodict.parse needs a string, so we use .read()
    raw_xml = xml_file.read()
    data_dict = xmltodict.parse(raw_xml)



gigabit = data_dict['rpc-reply']['data']['native']['interface'].get('GigabitEthernet', [])


for intf in gigabit:
    name = intf.get('name', 'Unknown')
    status = "DOWN" if 'shutdown' in intf else "UP"

    primary_ip = intf.get('ip', {}).get('address', {}).get('primary', {})

    ip_addr = primary_ip.get('address', 'Unassigned')
    netmask = primary_ip.get('mask', 'N/A')

    print(f"GigabitEthernet{name:<5} | {status:<5} | {ip_addr:<15} | {netmask:<15}")

