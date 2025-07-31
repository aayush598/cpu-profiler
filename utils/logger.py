import json
import os
from datetime import datetime

def save_report(data: dict, filename: str = None):
    if filename is None:
        if not os.path.exists("reports"):
            os.makedirs("reports")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join("reports", f"report_{timestamp}.json")
    else:
        filename = os.path.expanduser(filename)  # support ~/
        dir_name = os.path.dirname(filename)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Report saved to {filename}")
