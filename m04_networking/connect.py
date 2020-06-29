from netmiko import Netmiko


def connect(device_type):

    cisco_sandbox_device = {
        "csr": {
            "hostname": "ios-xe-mgmt-latest.cisco.com",
            "port": 8181,
            "username": "developer",
            "password": "C1sco12345",
            "device_type": "cisco_ios",
        },
        "nexus": {
            "hostname": "sbx-nxos-mgmt.cisco.com",
            "port": 8181,
            "username": "admin",
            "password": "Admin_1234!",
            "device_type": "cisco_nxos",
        },
    }

    print(
        f"Connecting to {cisco_sandbox_device[device_type]['hostname']}:{cisco_sandbox_device[device_type]['port']}"
    )
    print("... this may take a little while.")

    connection = Netmiko(
        cisco_sandbox_device[device_type]["hostname"],
        port=cisco_sandbox_device[device_type]["port"],
        username=cisco_sandbox_device[device_type]["username"],
        password=cisco_sandbox_device[device_type]["password"],
        device_type=cisco_sandbox_device[device_type]["device_type"],
    )

    return connection