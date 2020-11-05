import json # Standard library

import swagger_client # Local module


class WiSun:
    """implements all APIs to talk to a DUT
    Atrributes:
    devices (str): contains all information for every device (such as ip address and port number) which it gets from devices.json
    PCs (str): contains all the ip addresses; each distinct ip address represents a different PC
    ports (str): contains all the port numbers; each port number represents a device on a specific PC
    """
    _devices = dict()
    _PCs = dict()
    _ports = dict()

    def __init__(self, jsonPath):
        with open(jsonPath) as f:
            devices = json.load(f)

        for device in devices:
            if device["ip"] not in self._PCs.values():
                self._PCs[len(self._PCs) + 1] = device["ip"]

            if device["port"] not in self._ports.values():
                self._ports[len(self._ports) + 1] = device["port"]

            if (device["ip"], device["port"]) not in self._devices:
                self._devices[(device["ip"], device["port"])] = self._create_device(device["ip"], device["port"])


    def _create_device(self, ip: str, port: str):
        """Creates an instance of the API class with the given ip address and port number
        Args:
        ip (str): ip address representing the PC
        port (str): port number representing the device on the PC
        Returns:
        api_instance: instance of the API class
        """
        WISUN_UI = f"http://{ip}:{port}/Wi-SUN/TBU/1.0.0"
        configuration = swagger_client.Configuration(WISUN_UI)

        # Create an instance of the API class (Device)
        api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

        print(f"Finish creating Device at {ip}:{port}")
        return api_instance


    def _print_device(self, PC, device):
        print(f"Calling Device{device} at PC{PC} {self._PCs[PC]}:{self._ports[device]}")


    ### Functions ###
    def config_border_router_gtks_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_border_router_gtks_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_border_router_key_lifetimes_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_border_router_key_lifetimes_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_border_router_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_border_router_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_border_router_revoke_keys_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_border_router_revoke_keys_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_chan_plan_bcast_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_chan_plan_bcast_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_chan_plan_explicit_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_chan_plan_explicit_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_chan_plan_fixed_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_chan_plan_fixed_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_chan_plan_reg_op_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_chan_plan_reg_op_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_chan_plan_unicast_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_chan_plan_unicast_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_dodag_routes_get(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_dodag_routes_get()
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_ip_addresses_get(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_ip_addresses_get()
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_neighbor_table_get(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_neighbor_table_get()
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_phy_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_phy_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_preferred_parent_get(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_preferred_parent_get(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_router_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_router_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_security_keys_get(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_security_keys_get()
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_whitelist_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.config_whitelist_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def run_mode_mode_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.run_mode_mode_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def subscription_frames_hash_get(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.subscription_frames_hash_get()
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def subscription_frames_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.subscription_frames_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def transmitter_icmpv6_echo_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.transmitter_icmpv6_echo_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def transmitter_udp_put(self, PC: int, device: int, args=None):
        device = self._devices[(self._PCs[PC], self._ports[device])]
        device.transmitter_udp_put(args[0])
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body
