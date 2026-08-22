# Network Automation - CISCO IOS-XE - CML Labs

 
Python-based network automation scripts for Cisco IOS-XE using Netmiko, Paramiko, RESTCONF, and NETCONF.
 



## Prerequisites
 
**Python 3.9+** and the following on your IOS-XE devices:
 
```
! Enable SSH
ip domain-name lab.local
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
 transport input ssh
 login local
 
! Enable RESTCONF
restconf
 
! Enable NETCONF
netconf-yang
 
! Create local user
username admin privilege 15 secret 0 yourpassword
```

## Repo Structure
```
network-automation/
├── netmiko/              # CLI automation via SSH (Netmiko)
├── paramiko/             # Raw SSH automation (Paramiko)
├── restconf/             # REST API automation (RESTCONF + YANG)
├── netconf/              # NETCONF/YANG automation (ncclient)
└── README.md
```


 
## Installation
 
```bash
git clone git@github.com:you/network-automation.git
cd network-automation
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


**requirements.txt**
```
netmiko>=4.3.0
paramiko>=3.4.0
ncclient>=0.6.15
requests>=2.31.0
pyyaml>=6.0
xmltodict>=0.13.0
rich>=13.0.0
```
