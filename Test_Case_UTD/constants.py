CONFIG_PHY_PUT_PARAM = {
    "modulation": 2,
    "modulationIndex": 1,
    "symbolRate": 50000
}

CONFIG_CHAN_PLAN_REG_OP_PUT_PARAM = {
    "opClass": 1,
    "regDomain": 1
}

CONFIG_CHAN_PLAN_UNICAST_PUT_PARAM = {
    "channelFunction": 2,
    "dwellInterval": 100,
    "excludedChannelMask": [
        0
    ],
    "excludedChannelRange": [
        1, 5, 10, 20
    ]
}

CONFIG_CHAN_PLAN_BCAST_PUT_PARAM = {
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

CONFIG_BORDER_ROUTER_PUT_PARAM = {
    "panId": 0xAABB,
    "panSize": 20,
    "useParentBcastSched": True,
    "routingMethod": 0,
    "networkName": "WISUN PAN",
    "sixLowpanMtu": 500
}

CONFIG_BORDER_ROUTER_GTKS_PUT_PARAM = {
    "gtk0": "BB0608572CE14D7BA2D155499CC8519B",
    "gtk1": "1849835A01684FC8ACA583F37040F74C ",
    "gtk2": "59EA58A4B8834938ADCB6BE388C26263",
    "gtk3": " E426B491BC054AF39B59F053EC128E5F "
}

CONFIG_BORDER_ROUTER_KEY_LIFETIMES_PUT_PARAM = {
    "gtkLifetime": "30",
    "gtkNewActivationTime": 20,
    "pmkLifetime": "120",
    "ptkLifetime": "60",
    "revocationLifetimeReduction": 10
}

CONFIG_ROUTER_PUT_PARAMS = {
    1: {
        "networkName": "WiSUN PAN",
        "panSizeOffset": 0,
        "routingCostOffset": 0,
        "routingMethod": 0,
        "sixLowpanMtu": 500
    },
    2: {
        "routingMethod": 0,
        "networkName": "WiSUN PAN",
        "panSizeOffset": 10,
        "routingCostOffset": 10,
        "sixLowpanMtu": 500
    },
    3: {
        "routingMethod": 0,
        "networkName": "WiSUN PAN",
        "panSizeOffset": 10,
        "routingCostOffset": 20,
        "sixLowpanMtu": 500
    }
}

CONFIG_WHITELIST_PUT_PARAMS = {
    1: {
        "macAddressList": [
            "DEVA_EUI64"
        ]
    },
    2: {
        "macAddressList": [
            "BR_EUI64", "DEVB_EUI64"
        ]
    },
    3: {
        "macAddressList": [
            "DEVA_EUI64"
        ]
    }
}

SUBSCRIPTION_FRAMES_PARAMS = {
    1: {
        "fwdAddress": "IP_HOST_MACHINE",
        "fwdPort": 1,
        "subscriptionMode": "Start"
    },
    3: {
        "subscriptionMode": "Start",
        "fwdAddress": "IP_HOST_MACHINE",
        "fwdPort": 2
    }
}

PARENT_IP = {
    "ipAddress": "192.168.1.8"
}

TRANSMITTER_UDP_PUT_PARAMS = {
    1: {
        "srcAddress": "IP_BR",
        "srcPort": 100,
        "destAddress": "IP_DEVB",
        "destPort": 100,
        "data": "0x123456789ABCDEF",
        "frameExchangePattern": 0
    },
    3: {
        "srcAddress": "IP_BR",
        "srcPort": 100,
        "destAddress": "IP_DEVB",
        "destPort": 100,
        "data": "0x123456789ABCDEF",
        "frameExchangePattern": 0
    }
}

TRANSMITTER_ICMPV6ECHO_PARAM = {
    "srcAddress": "IP_BR",
    "destAddress": "IP_DEVB",
    "hopLimit": 2,
    "echoBody": "0x123456",
    "frameExchangePattern": 0,
    "identifier": 0x123,
    "sequenceNumber": 0x123
}