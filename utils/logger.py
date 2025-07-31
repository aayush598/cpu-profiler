import json
import os
from datetime import datetime

def save_report(data: dict, filename: str = None):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.json"

    filepath = os.path.join("reports", filename)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Report saved to {filepath}")
