from genie.testbed import load

testbed = load('testbed.yaml')          # parse YAML into objects
device = testbed.devices['RTR02']    # grab the device object


device.connect(log_stdout=False)        # open the SSH session

parsed = device.parse('show ip interface brief') # Parse a command with Genie


# Assert: GigabitEthernet1 must be up
gig1 = parsed['interface']['GigabitEthernet1']
assert gig1['status'] == 'up', f"Gig1 is {gig1['status']}, expected up!"
assert gig1['protocol'] == 'up', f"Gig1 protocol is {gig1['protocol']}!"

print("PASS: GigabitEthernet1 is up/up")
