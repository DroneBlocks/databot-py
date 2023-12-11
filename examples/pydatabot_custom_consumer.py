from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)

from databot.PyDatabot import PyDatabot, DatabotConfig


class CustomPyDatabotConsumer(PyDatabot):

    def process_databot_data(self, epoch, data):
        self.logger.info(f"{data}")
        self.logger.info(f"Linear Acceleration: {data['linear_acceleration_x']}, {data['linear_acceleration_y']}, {data['linear_acceleration_z']}")


def main():
    c = DatabotConfig()
    c.Laccl = True
    c.address = PyDatabot.get_databot_address()
    db = CustomPyDatabotConsumer(c)
    db.run()


if __name__ == '__main__':
    main()
