import swagger_client

class WiSun:
    devices = None
    PCs = None
    ports = None

    def _init_(self, json):
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
        # http://192.168.1.23:5550/Wi-SUN/TBU/1.0.0/ui/
        WISUN_UI = "http://" + ip + ":" + port + "/Wi-SUN/TBU/1.0.0/ui/"
        configuration = swagger_client.Configuration(WISUN_UI)

        # create an instance of the API class
        api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

        return api_instance