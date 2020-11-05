# Local module
import swagger_client
from WiSun import utils


class WiSun:
    """ Initialize PCs and Devices from the given JSON file
        JSON Example:
            [
              {
                "ip":"192.168.43.168",
                "port":"5000"
              },
              {
                "ip":"192.168.43.168",
                "port":"5002"
              },
              {
                "ip":"192.168.43.168",
                "port":"5003"
              }
            ]

    Atrributes:
    devices (str):  contains all information for every device (such as ip address and port number) which it gets from devices.json
    PCs (str):      contains all the ip addresses; each distinct ip address represents a different PC
    ports (str):    contains all the port numbers; each port number represents a device on a specific PC
    """
    def __init__(self, JSON):
        self._devices = {}
        self._PCs = {}
        self._ports = {}

        devices = utils.read_JSON(JSON)

        for device in devices:
            self._add_PC(device)
            self._add_port(device)
            self._add_device(device)


    def _add_PC(self, device):
        if device["ip"] not in self._PCs.values():
            self._PCs[len(self._PCs) + 1] = device["ip"]


    def _add_port(self, device):
        if device["port"] not in self._ports.values():
            self._ports[len(self._ports) + 1] = device["port"]


    def _add_device(self, device):
        if (device["ip"], device["port"]) not in self._devices:
            self._devices[(device["ip"], device["port"])] = self._create_api_instance(device["ip"], device["port"])


    def _create_api_instance(self, ip: str, port: str):
        """ Creates an instance of the API class with the given ip address and port number

        Args:
        ip (str):       ip address representing the PC
        port (str):     port number representing the device on the PC

        Returns:
        api_instance:   instance of the API class
        """
        WISUN_UI = f"http://{ip}:{port}/Wi-SUN/TBU/1.0.0"
        configuration = swagger_client.Configuration(WISUN_UI)

        # Create an instance of the API class (Device)
        api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

        print(f"Finish creating Device at {ip}:{port}")
        return api_instance


    def print_device(self, PC, device):
        """ Print Device with its IP_ADDRESS:PORT

        Args:
        PC (int):       ip address representing the PC
        device (int):   port number representing the device on the PC
        """
        print(f"Calling Device{device} at PC{PC} {self._PCs[PC]}:{self._ports[device]}")