thonpython
import json
import csv
import logging
from pathlib import Path

class Exporter:
    @staticmethod
    def export_json(data, path: Path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logging.error(f"JSON export failed: {e}")
            raise

    @staticmethod
    def export_csv(data, path: Path):
        try:
            if not data:
                return
            keys = sorted({k for item in data for k in item.keys()})
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                for item in data:
                    writer.writerow(item)
        except Exception as e:
            logging.error(f"CSV export failed: {e}")
            raise