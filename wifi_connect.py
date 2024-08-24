import network
import time


class DeviceNetwork:
    def __init__(self) -> None:
        self.name = "Default Network"
        self.client = network.WLAN(network.STA_IF)
        
        #Activate the network
        self.client.active(True)

    def scan_networks(self):
        networks = self.client.scan()
        

        try:
            if len(networks)>0:
                
                return networks
            if len(networks) == 0:
                print("No Wifi network found..")
        except Exception as e:
            print(f"An error occured during Wifi Scan: ",{e})

    