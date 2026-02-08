# Standard Cisco Netconf config
**Configure SSH**
```
conf t
hostname R1
ip domain-name lab.local
crypto key generate rsa general-keys modulus 2048
```
**Enable NETCONF (Uses port 830 by default)**

```netconf-yang```

**Create Priv 15 account**

```username admin privilege 15 secret Cisco123```

**Verify Netconf Process**

``show platform software yang-management process``





# Testing Netconf Connection on host
**Linux:**

```nc -zv 172.16.40.1 830```

**Windows:**

```Test-NetConnection -ComputerName 172.16.40.1 830 -Port 830```

**Test protocol**

```ssh admin@172.16.40.1 -p 830 -s netconf```
