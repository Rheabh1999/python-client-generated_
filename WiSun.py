import swagger_client
import json

class WiSun:
    devices = dict()
    PCs = dict()
    ports = dict()

    def __init__(self, jsonPath):
        with open(jsonPath) as f:
            devices = json.load(f)

        for device in devices:
            if device["ip"] not in self.PCs.values():
                self.PCs[len(self.PCs) + 1] = device["ip"]

            if device["port"] not in self.ports.values():
                self.ports[len(self.ports) + 1] = device["port"]

            if (device["ip"], device["port"]) not in self.devices:
                self.devices[(device["ip"], device["port"])] = self._create_device(device["ip"], device["port"])


    def _create_device(self, ip: str, port: str):
        # http://192.168.1.23:5550/Wi-SUN/TBU/1.0.0/ui/
        WISUN_UI = "http://" + ip + ":" + port + "/Wi-SUN/TBU/1.0.0"
        configuration = swagger_client.Configuration(WISUN_UI)

        # create an instance of the API class
        api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

        return api_instance

    def print_device(self, PC, device):
        print(self.PCs[PC], self.ports[device])

    def config_border_router_gtks_put(self, PC, device):
        self.print_device(PC, device)
        self.devices[(self.PCs[PC], self.ports[device])].post_api1("")
        response_body = self.devices[(self.PCs[PC], self.ports[device])].api_client.last_response.urllib3_response.data.decode('utf-8')

        return response_body