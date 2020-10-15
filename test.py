from WiSun import WiSun


if __name__ == "__main__":
    WiSun = WiSun("./devices.json")

    print("\nRunning \"config_border_router_gtks_put\" on all Devices on PC1: 192.168.1.53")

    for i in range(1,5):
        print(WiSun.config_border_router_gtks_put(PC=1, device=i))

    print("\nRunning \"config_border_router_gtks_put\" on all Devices on PC1: 192.168.1.54")
    for i in range(1, 5):
        print(WiSun.config_border_router_gtks_put(PC=2, device=i))