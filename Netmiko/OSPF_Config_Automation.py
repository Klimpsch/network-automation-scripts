from netmiko import ConnectHandler

import ipaddress

ospf_network = ipaddress.IPv4Network('10.0.0.0/24')


ospf_routers = {
    'R1': '192.168.122.117',
    'R2': '192.168.122.213',
    'R3': '192.168.122.168',
    'R4': '192.168.122.25',
}

network = ipaddress.IPv4Network('10.0.0.0/24')
subnets = list(network.subnets(new_prefix=30))[:3]


links = [
    ('R1', 'R2'),
    ('R2', 'R3'),
    ('R3', 'R4'),
]

interfaces = [
        ('int g0/1', 'int g0/1'),
        ('int g0/2', 'int g0/2'),
        ('int g0/1', 'int g0/1'),
        ]

# Build link data
link_data = []
for (r_a, r_b), subnet, (int_a, int_b) in zip(links, subnets, interfaces):
    hosts = list(subnet.hosts())
    link_data.append({
        'r_a': r_a, 'r_b': r_b,
        'r_a_ip': str(hosts[0]), 'r_b_ip': str(hosts[1]),
        'mask': str(subnet.netmask),
        'int_a': int_a, 'int_b': int_b,
    })


# Push config
for link in link_data:
    for router, ip, intf in [
        (link['r_a'], link['r_a_ip'], link['int_a']),
        (link['r_b'], link['r_b_ip'], link['int_b']),
    ]:
        commands = [
            f"{intf}",
            f"ip address {ip} {link['mask']}",
            f"no shutdown",
            f"ip ospf 1 area 0",
        ]
        print(f"Pushing to {router} ({ospf_routers[router]}) -> {intf} {ip}")
        with ConnectHandler(
            device_type='cisco_ios',
            host=ospf_routers[router],
            username='admin',
            password='secret',
        ) as conn:
            conn.send_config_set(commands)
