import json # Standard library

import swagger_client # Local module




class WiSun:
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
        WISUN_UI = f"http://{ip}:{port}/Wi-SUN/TBU/1.0.0"
        configuration = swagger_client.Configuration(WISUN_UI)

        # Create an instance of the API class (Device)
        api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

        print(f"Finish creating Device at {ip}:{port}")
        return api_instance


    def _print_device(self, PC, device) -> str:
        print(f"Calling Device{device} at PC{PC} {self._PCs[PC]}:{self._ports[device]}")


    ### Functions ###
    def config_border_router_gtks_put(self, PC: int, device: int) -> str:
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        body = swagger_client.GroupTransientKeys()
        device.config_border_router_gtks_put(body)
        response_body = device.api_client.last_response.urllib3_response.data.decode('utf-8')
        return response_body


    def config_border_router_key_lifetimes_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_border_router_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_border_router_revoke_keys_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_chan_plan_bcast_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_chan_plan_explicit_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_chan_plan_fixed_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_chan_plan_reg_op_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_chan_plan_unicast_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_dodag_routes_get(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_ip_addresses_get(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_neighbor_table_get(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_phy_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_preferred_parent_get(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_router_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_security_keys_get(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def config_whitelist_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def run_mode_mode_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def subscription_frames_hash_get(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def subscription_frames_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def transmitter_icmpv6_echo_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass


    def transmitter_udp_put(self, PC: int, device: int, args=None):
        self._print_device(PC, device)
        device = self._devices[(self._PCs[PC], self._ports[device])]
        print(device)
        pass
