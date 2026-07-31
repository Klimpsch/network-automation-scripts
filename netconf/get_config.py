from ncclient import manager
import sys
import xmltodict
import json
from datetime import datetime 



# router object
router = {
    "host": "172.16.40.1",
    "port": 830,
    "username": "admin",
    "password": "Cisco123",
    "hostkey_verify": False}

def get_router_config():
    try:
        with manager.connect(**router) as m:
            response = m.get_config(source='running')
            config_xml = response.xml
            config_dict = xmltodict.parse(config_xml)

            return config_dict

    except Exception as e:
        print(f"Error: {e}")

# get xml assign the variable
conf_xml = get_router_config()

#c convert xml to json
conf_json = json.dumps(conf_xml, indent=4)


today = datetime.now().strftime("%Y-%m-%d")
filename = (f"{filename}-Conf.json")
with open(filename, "w") as f:
    f.write(conf_json)

print(f"File {filename} has been created")



