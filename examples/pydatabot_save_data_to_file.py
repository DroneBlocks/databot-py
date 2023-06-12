import json
from pathlib import Path
import logging

from databot.PyDatabot import PyDatabot, DatabotConfig


class SaveToFileDatabotCollector(PyDatabot):

    def __init__(self, databot_config: DatabotConfig, log_level: int = logging.INFO):
        super().__init__(databot_config, log_level)
        self.file_name = "data/test_data.txt"
        self.file_path = Path(self.file_name)
        if self.file_path.exists():
            self.file_path.unlink(missing_ok=True)
        self.record_number = 0

    def process_databot_data(self, epoch, data):

        with self.file_path.open("a", encoding="utf-8") as f:
            data['timestamp'] = epoch
            f.write(json.dumps(data))
            f.write("\n")
            self.logger.info(f"wrote record[{self.record_number}]: {epoch}")
            self.record_number = self.record_number + 1



def main():
    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto = False
    c.address = "774B790E-35DE-4950-842D-81446C06240B"
    db = SaveToFileDatabotCollector(c)
    db.run()


if __name__ == '__main__':
    main()
