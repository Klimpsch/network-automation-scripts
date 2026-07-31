from netmiko import ConnectHandler
import ipaddress

# Device credentials
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password123',
    'secret': 'enable_secret',
}


def get_wildcard(subnet_mask):
    """Convert subnet mask to wildcard mask."""
    return str(ipaddress.IPv4Address(
        int(ipaddress.IPv4Address(subnet_mask)) ^ 0xFFFFFFFF
    ))


def get_ospf_inputs():
    """Gather OSPF network details from user input."""
    print("\n--- OSPF Network Configuration ---")

    network = input("Enter network address (e.g. 192.168.10.0): ").strip()
    subnet_mask = input("Enter subnet mask (e.g. 255.255.255.0): ").strip()
    area = input("Enter OSPF area (e.g. 0): ").strip()
    process_id = input("Enter OSPF process ID (e.g. 1): ").strip()

    # Validate network address
    try:
        ipaddress.IPv4Address(network)
    except ValueError:
        print(f"Invalid network address: {network}")
        return None

    # Validate subnet mask and convert to wildcard
    try:
        wildcard = get_wildcard(subnet_mask)
    except ValueError:
        print(f"Invalid subnet mask: {subnet_mask}")
        return None

    return {
        'network': network,
        'wildcard': wildcard,
        'area': area,
        'process_id': process_id,
    }


def add_ospf_network(device, ospf_params):
    """Connect to device and push OSPF config."""
    commands = [
        f"router ospf {ospf_params['process_id']}",
        f"network {ospf_params['network']} {ospf_params['wildcard']} area {ospf_params['area']}",
    ]

    print(f"\nCommands to be pushed:")
    for cmd in commands:
        print(f"  {cmd}")

    confirm = input("\nProceed? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Aborted.")
        return

    try:
        print(f"\nConnecting to {device['host']}...")
        connection = ConnectHandler(**device)

        connection.enable()
        print("Entered enable mode")

        print("Pushing OSPF configuration...")
        output = connection.send_config_set(commands)
        print(output)

        save_output = connection.save_config()
        print("Configuration saved")

        verify = connection.send_command('show running-config | section ospf')
        print("\nVerification - OSPF config on device:")
        print(verify)

        connection.disconnect()
        print("Disconnected successfully")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    ospf_params = get_ospf_inputs()
    if ospf_params:
        add_ospf_network(device, ospf_params)

