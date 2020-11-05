from WiSun.API.default import Default
from Test_Case_UTD.constants import CONFIG_PHY_PUT_PARAM, CONFIG_CHAN_PLAN_REG_OP_PUT_PARAM, CONFIG_CHAN_PLAN_UNICAST_PUT_PARAM, \
                                    CONFIG_CHAN_PLAN_BCAST_PUT_PARAM, CONFIG_BORDER_ROUTER_PUT_PARAM, CONFIG_BORDER_ROUTER_GTKS_PUT_PARAM, \
                                    CONFIG_BORDER_ROUTER_KEY_LIFETIMES_PUT_PARAM, CONFIG_ROUTER_PUT_PARAMS, CONFIG_WHITELIST_PUT_PARAMS, \
                                    SUBSCRIPTION_FRAMES_PARAMS, PARENT_IP, TRANSMITTER_UDP_PUT_PARAMS, TRANSMITTER_ICMPV6ECHO_PARAM

import json
import time


def configure_devices(WiSun, PC, device):
    WiSun.config_phy_put(PC, device, args=[CONFIG_PHY_PUT_PARAM])

    WiSun.config_chan_plan_reg_op_put(PC, device, args=[CONFIG_CHAN_PLAN_REG_OP_PUT_PARAM])

    WiSun.config_chan_plan_unicast_put(PC, device, args=[CONFIG_CHAN_PLAN_UNICAST_PUT_PARAM])

    WiSun.config_chan_plan_bcast_put(PC, device, args=[CONFIG_CHAN_PLAN_BCAST_PUT_PARAM])


def configure_BR(WiSun, PC=1, device=1):
    WiSun.config_border_router_put(PC, device, args=[CONFIG_BORDER_ROUTER_PUT_PARAM])

    WiSun.config_border_router_gtks_put(PC, device, args=[CONFIG_BORDER_ROUTER_GTKS_PUT_PARAM])

    WiSun.config_border_router_key_lifetimes_put(PC, device, args=[CONFIG_BORDER_ROUTER_KEY_LIFETIMES_PUT_PARAM])


def configure_specific_device(WiSun, PC=1):
    for device in range(1,4):
        config_router(WiSun, PC, device)

    for device in range(1,4):
        config_whitelist(WiSun, PC, device)

    for device in [1, 3]:
        subscription_frames(WiSun, PC, device)


def config_router(WiSun, PC, device):
    WiSun.config_router_put(PC, device, args=[CONFIG_ROUTER_PUT_PARAMS[device]])


def config_whitelist(WiSun, PC, device):
    WiSun.config_whitelist_put(PC, device, args=[CONFIG_WHITELIST_PUT_PARAMS[device]])


def subscription_frames(WiSun, PC, device):
    WiSun.subscription_frames_put(PC, device, args=[SUBSCRIPTION_FRAMES_PARAMS[device]])


def start_test(WiSun, PC, device):
    WiSun.run_mode_mode_put(PC, device, args=[1])


def check_joined(WiSun, PC = 1):
    for device in [2,3]:
        config_ipaddr(WiSun, PC, device)

    for device in [2,3]:
        config_securityKeys(WiSun, PC, device)

    config_dodagRoutes(WiSun, PC, 1)

    for device in [2, 3]:
        config_preferredParent(WiSun, PC, device)

    for device in [2, 3]:
        config_neighborTable(WiSun, PC, device)


def config_ipaddr(WiSun, PC, device):
    print(f"Device {'A' if device == 2 else 'B'} - /config/ipAddresses:", WiSun.config_ip_addresses_get(PC, device))


def config_securityKeys(WiSun, PC, device):
    print(f"Device {'A' if device == 2 else 'B'} - /config/securityKeys:", json.loads(WiSun.config_security_keys_get(PC, device)))


def config_dodagRoutes(WiSun, PC, device):
    print("br - /config/dodagRoutes", "Output:", WiSun.config_dodag_routes_get(PC, device))


def config_preferredParent(WiSun, PC, device):
    print(f"Device {'A' if device == 2 else 'B'} - /config/preferredParent", "Output:", WiSun.config_preferred_parent_get(PC, device, args=[PARENT_IP]))


def config_neighborTable(WiSun, PC, device):
    print(f"Device {'A' if device == 2 else 'B'} - /config/neighborTable", "Output:", WiSun.config_neighbor_table_get(PC, device))


def transmitter_udp(WiSun, PC, device):
    print(f"{'BR to Device A ' if device == 1 else 'Device B to BR '} - /transmitter/udp", "Output:",
          WiSun.transmitter_udp_put(PC, device, args=[TRANSMITTER_UDP_PUT_PARAMS[device]
    ]))


def send_ping(WiSun, PC, device):
    print("BR - /transmitter/icmpv6Echo.", "Output:",
          WiSun.transmitter_icmpv6_echo_put(PC, device, args=[TRANSMITTER_ICMPV6ECHO_PARAM]))


if __name__ == "__main__":
    WiSun = Default("./devices.json")

    """
    PC 1, Device 1 : BR - 192.168.1.8:5000
    PC 1, Device 2 : Device A - 192.168.1.8:5002
    PC 1, Device 3 : Device B - 192.168.1.8:5003
    
    Client: 172.23.0.1
    """
    for device in range(1, 4):
        configure_devices(WiSun, 1, device)

    configure_BR(WiSun)

    configure_specific_device(WiSun)

    for device in range(1,4):
        start_test(WiSun, 1, device)

    time.sleep(5)

    check_joined(WiSun)

    for device in [1, 3]:
        transmitter_udp(WiSun, 1, device)

    send_ping(WiSun,1, 1)