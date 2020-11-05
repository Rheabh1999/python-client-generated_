from WiSun import WiSun
import json
import time

if __name__ == "__main__":
    WiSun = WiSun("./devices.json")

    # PC 1, Device 1 = BR
    # PC 1, Device 2 = Device A
    # PC 1, Device 3 = Device B

    for i in range(1, 4):
        # /config/phy
        print(WiSun.config_phy_put(PC=1, device=i, args=[{
          "modulation": 2,
          "modulationIndex": 1,
          "symbolRate": 50000
        }]))

        # /config/chanPlan/regOp
        print(WiSun.config_chan_plan_reg_op_put(PC=1, device=i, args=[
            {
                "opClass": 1,
                "regDomain": 1
            }
        ]))

        # ​/config​/chanPlan​/unicast
        print(WiSun.config_chan_plan_unicast_put(PC=1, device=i, args=[
            {
                "channelFunction": 2,
                "dwellInterval": 100,
                "excludedChannelMask": [
                    0
                ],
                "excludedChannelRange": [
                    1, 5, 10, 20
                ]
            }
        ]))

        # ​/config​/chanPlan​/unicast
        print(WiSun.config_chan_plan_bcast_put(PC=1, device=i, args=[
            {
                "bcastInterval": 5000,
                "bcastScheduleId": 1234,
                "channelFunction": 2,
                "dwellInterval": 100,
                "excludedChannelMask": [
                    0, 1, 2, 4
                ],
                "excludedChannelRange": [
                    0
                ]
            }
        ]))


    # Configure BR:
    # config/borderRouter
    print(WiSun.config_border_router_put(PC=1, device=1, args=[
        {
            "panId": 0xAABB,
            "panSize": 20,
            "useParentBcastSched": True,
            "routingMethod": 0,
            "networkName": "WISUN PAN",
            "sixLowpanMtu": 500
        }
    ]))

    # /config/borderRouter/gtks
    print(WiSun.config_border_router_gtks_put(PC=1, device=1, args=[
        {
            "gtk0": "BB0608572CE14D7BA2D155499CC8519B",
            "gtk1": "1849835A01684FC8ACA583F37040F74C ",
            "gtk2": "59EA58A4B8834938ADCB6BE388C26263",
            "gtk3": " E426B491BC054AF39B59F053EC128E5F "
        }
    ]))

    # /config​/borderRouter​/keyLifetimes
    print(WiSun.config_border_router_key_lifetimes_put(PC=1, device=1, args=[
        {
            "gtkLifetime": "30",
            "gtkNewActivationTime": 20,
            "pmkLifetime": "120",
            "ptkLifetime": "60",
            "revocationLifetimeReduction": 10
        }
    ]))

    # Device Specific Configuration
    # /config/router
    # br
    print(WiSun.config_router_put(PC=1, device=1, args=[
        {
            "networkName": "WiSUN PAN",
            "panSizeOffset": 0,
            "routingCostOffset": 0,
            "routingMethod": 0,
            "sixLowpanMtu": 500
        }
    ]))

    # device A
    print(WiSun.config_router_put(PC=1, device=2, args=[
        {
            "routingMethod": 0,
            "networkName": "WiSUN PAN",
            "panSizeOffset": 10,
            "routingCostOffset": 10,
            "sixLowpanMtu": 500
        }
    ]))

    # device B
    print(WiSun.config_router_put(PC=1, device=3, args=[
        {
            "routingMethod": 0,
            "networkName": "WiSUN PAN",
            "panSizeOffset": 10,
            "routingCostOffset": 20,
            "sixLowpanMtu": 500
        }
    ]))

    # /config/whitelist
    # br
    print(WiSun.config_whitelist_put(PC=1, device=1, args=[
        {
            "macAddressList": [
                "DEVA_EUI64"
            ]
        }
    ]))

    # device A
    print(WiSun.config_whitelist_put(PC=1, device=2, args=[
        {
          "macAddressList": [
            "BR_EUI64", "DEVB_EUI64"
          ]
        }
    ]))

    # device B
    print(WiSun.config_whitelist_put(PC=1, device=3, args=[
        {
            "macAddressList": [
                "DEVA_EUI64"
            ]
        }
    ]))

    # /subscription/frames
    # br
    print(WiSun.subscription_frames_put(PC=1, device=1, args=[
        {
            "fwdAddress": "IP_HOST_MACHINE",
            "fwdPort": 1,
            "subscriptionMode": "Start"
        }
    ]))

    # device B
    print(WiSun.subscription_frames_put(PC=1, device=3, args=[
        {
            "subscriptionMode": "Start",
            "fwdAddress": "IP_HOST_MACHINE",
            "fwdPort": 2
        }
    ]))


    # Start Test
    # /runMode/{mode}
    for i in range(1,4):
        print(WiSun.run_mode_mode_put(PC=1, device=i, args=[1]))

    time.sleep(5)

    # # Check if Device has joined
    # # /config/ipAddresses
    # Device A
    print("Device A - /config/ipAddresses:", WiSun.config_ip_addresses_get(PC=1, device=1))

    # Device B
    print("Device B - /config/ipAddresses:", WiSun.config_ip_addresses_get(PC=1, device=2))

    # /config/securityKeys
    # Device A
    print("Device A - /config/securityKeys:", json.loads(WiSun.config_security_keys_get(PC=1, device=2)))

    # Device B
    print("Device B - /config/securityKeys:", json.loads(WiSun.config_security_keys_get(PC=1, device=3)))

    # /config/dodagRoutes
    # br
    print("br - /config/dodagRoutes", "Output:", WiSun.config_dodag_routes_get(PC=1, device=1))

    # /config/preferredParent
    # Device A
    print("Device A - /config/preferredParent", "Output:", WiSun.config_preferred_parent_get(PC=1, device=2, args=[{
        "ipAddress": "192.168.43.168"
    }]))

    # Device B
    print("Device B - /config/preferredParent", "Output:", WiSun.config_preferred_parent_get(PC=1, device=3, args=[{
        "ipAddress": "192.168.43.168"
    }]))

    # /config/neighborTable
    # Device A
    print("Device A - /config/neighborTable", "Output:", WiSun.config_neighbor_table_get(PC=1, device=2))

    # Device B
    print("Device A - /config/neighborTable", "Output:", WiSun.config_neighbor_table_get(PC=1, device=3))


    # /transmitter/udp
    # br
    print("BR to Device A - /transmitter/udp", "Output:", WiSun.transmitter_udp_put(PC=1, device=1, args=[
        {
            "srcAddress": "IP_BR",
            "srcPort": 100,
            "destAddress": "IP_DEVB",
            "destPort": 100,
            "data": "0x123456789ABCDEF",
            "frameExchangePattern": 0
        }
    ]))

    # device B

    print("BR to Device A - /transmitter/udp", "Output:", WiSun.transmitter_udp_put(PC=1, device=3, args=[
        {
            "srcAddress": "IP_BR",
            "srcPort": 100,
            "destAddress": "IP_DEVB",
            "destPort": 100,
            "data": "0x123456789ABCDEF",
            "frameExchangePattern": 0
        }
    ]))


    # /transmitter/icmpv6Echo
    # br
    print("BR - /transmitter/icmpv6Echo.", "Output:", WiSun.transmitter_icmpv6_echo_put(PC=1, device=1, args=[
        {
            "srcAddress": "IP_BR",
            "destAddress": "IP_DEVB",
            "hopLimit": 2,
            "echoBody": "0x123456",
            "frameExchangePattern": 0,
            "identifier": 0x123,
            "sequenceNumber": 0x123
        }
    ]))