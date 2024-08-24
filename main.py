from wifi_connect import DeviceNetwork

device_network = DeviceNetwork()
networks = device_network.scan_networks()
print(networks)