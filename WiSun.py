import swagger_client

class WiSun:
    """implements apis in PC's of each devices
    Atrributes:
    devices (str): contains all information for every device (such as ip address and port number) which it gets from devices.json
    PCs (int): contains all the ip addresses; each distinct ip address represents a different PC
    ports (int): contains all the port numbers; each port number represents a device on a specific PC
    """
    devices = None
    PCs = None
    ports = None

    def _init_(self, json):
        """Initializes devices with devices.json,
        PCs with the ip addresses in devices.json, and
        ports with the port numbers in devices.json
        Args:
        json (str): path to devices.json file
        Raises:
        //
        """
        with open('./devices.json') as f:
            devices = json.load(f)

        for device in devices:
            if device["ip"] not in self.PCs.values():
                self.PCs[len(self.PCs) + 1] = device["ip"]

            if device["port"] not in self.ports.values():
                self.PCs[len(self.PCs) + 1] = device["port"]

            if (device["ip"], device["port"]) not in self.devices:
                self.devices[(device["ip"], device["port"])] = self._create_device(device["ip"], device["port"])


    def _create_device(self, ip: str, port: str):
        """Creates an instance of the API class with the given ip address and port number
        Args:
        ip (str): ip address representing the PC
        port (str): port number representing the device on the PC
        Returns:
        api_instance: instance of the API class
        Raises:
        //
        """
        # http://192.168.1.23:5550/Wi-SUN/TBU/1.0.0/ui/
        WISUN_UI = "http://" + ip + ":" + port + "/Wi-SUN/TBU/1.0.0/ui/"
        configuration = swagger_client.Configuration(WISUN_UI)

        # create an instance of the API class
        api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

        return api_instance