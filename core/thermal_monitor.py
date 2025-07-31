import os
import glob

def read_temperature_sensors():
    sensors = []

    for hwmon in glob.glob("/sys/class/hwmon/hwmon*"):
        try:
            with open(os.path.join(hwmon, "name")) as f:
                name = f.read().strip()
        except FileNotFoundError:
            continue

        temp_files = glob.glob(os.path.join(hwmon, "temp*_input"))
        for temp_file in temp_files:
            label_file = temp_file.replace("_input", "_label")
            try:
                with open(label_file) as lf:
                    label = lf.read().strip()
            except FileNotFoundError:
                label = os.path.basename(temp_file).replace("_input", "")

            try:
                with open(temp_file) as tf:
                    value = int(tf.read().strip()) / 1000.0
                sensors.append({
                    "chip": name,
                    "label": label,
                    "temperature_c": value
                })
            except Exception:
                continue

    return sensors
