from WiSun import WiSun


if __name__ == "__main__":
    WiSun = WiSun("./devices.json")

    WiSun.config_border_router_gtks_put(PC=1, device=1)