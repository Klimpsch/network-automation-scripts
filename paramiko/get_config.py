import paramiko
import time



def get_cisco_config(hostname, username, password):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

        print(f"Connecting to {hostname}...")

        client.connect(hostname, username=username, password=password, look_for_keys=False)

        connection = client.invoke_shell()

        time.sleep(1)

        connection.send("term len 0\n")
        time.sleep(1)

        connection.send("show config\n")
        time.sleep(5)

        output = connection.recv(65535).decode('utf-8')

        print("config retriieved success")

        return output

    except Exception as e:
        return f"Error: {e}"

    finally:
        client.close()


if __name__ == "__main__":
    device_ip = "172.16.40.1"
    user = "admin"
    secret = "Cisco123"

    config_data = get_cisco_config(device_ip, user, secret)

    with open(f"{device_ip}_config.text", "w") as f:
        f.write(config_data)



