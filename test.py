from WiSun import WiSun

if __name__ == "__main__":
    WiSun = WiSun("./devices.json")

    print(WiSun.config_border_router_gtks_put(1, 1))