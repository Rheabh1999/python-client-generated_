from .. WiSun import WiSun


class Default(WiSun):
    """ Default APIs from swagger.io
        Inherited WiSun Class
    """
    def __init__(self, JSON):
        super(Default, self).__init__(JSON)


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