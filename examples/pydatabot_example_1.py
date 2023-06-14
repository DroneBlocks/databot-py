from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)
from databot.PyDatabot import PyDatabot, DatabotConfig


def main():
    with open("./databot_address.txt", "r") as f:
        databot_address = f.read()

    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto =True
    c.address = databot_address
    db = PyDatabot(c)
    db.run()


if __name__ == '__main__':
    main()
