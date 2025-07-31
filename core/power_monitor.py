import glob
import os

def read_powercap_energy():
    energy_data = []

    for zone_path in glob.glob("/sys/class/powercap/intel-rapl:*/energy_uj"):
        try:
            with open(zone_path) as f:
                energy_uj = int(f.read().strip())

            zone_name_path = zone_path.replace("energy_uj", "name")
            with open(zone_name_path) as f:
                name = f.read().strip()

            energy_data.append({
                "source": name,
                "energy_uj": energy_uj
            })
        except Exception:
            continue

    return energy_data

def read_hwmon_power():
    power_data = []

    for hwmon in glob.glob("/sys/class/hwmon/hwmon*"):
        try:
            with open(os.path.join(hwmon, "name")) as f:
                chip_name = f.read().strip()
        except FileNotFoundError:
            continue

        power_inputs = glob.glob(os.path.join(hwmon, "power*_input"))
        for path in power_inputs:
            try:
                with open(path) as f:
                    mwatts = int(f.read().strip()) / 1000.0
                label = os.path.basename(path).replace("_input", "")
                power_data.append({
                    "chip": chip_name,
                    "label": label,
                    "power_mw": mwatts
                })
            except Exception:
                continue

    return power_data
