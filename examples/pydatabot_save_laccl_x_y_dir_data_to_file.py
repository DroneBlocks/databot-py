from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)

import json
from pathlib import Path
import logging

from databot.PyDatabot import PyDatabot, DatabotConfig


class SaveToFileDatabotCollector(PyDatabot):

    def __init__(self, databot_config: DatabotConfig, log_level: int = logging.INFO):
        super().__init__(databot_config, log_level)
        self.file_name = "data/linear_x_y_accl_data.txt"
        self.file_path = Path(self.file_name)
        if self.file_path.exists():
            self.file_path.unlink(missing_ok=True)
        self.record_number = 0

    def process_databot_data(self, epoch, data):
        with self.file_path.open("a", encoding="utf-8") as f:
            print(data)
            data_to_store = {
                'time': data['time'],
                'linear_acceleration_x': data['linear_acceleration_x'],
                'linear_acceleration_y': data['linear_acceleration_y']
            }

            f.write(json.dumps(data_to_store))
            f.write("\n")
            self.logger.info(f"wrote record[{self.record_number}]: {epoch}")
            self.record_number = self.record_number + 1


def main():
    with open("./databot_address.txt", "r") as f:
        databot_address = f.read()

    c = DatabotConfig()
    c.Laccl = True
    c.refresh=100
    c.address = databot_address
    db = SaveToFileDatabotCollector(c)
    db.run()


if __name__ == '__main__':
    main()
