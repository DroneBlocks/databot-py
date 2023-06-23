from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)

from databot.PyDatabot import PyDatabot, DatabotConfig, DatabotLEDConfig


def main():
    with open("./databot_address.txt", "r") as f:
        databot_address = f.read()

    c = DatabotConfig()
    c.ambLight = True

    c.led1 = DatabotLEDConfig(True, 255,0,0)
    c.led2 = DatabotLEDConfig(True, 0,255,0)
    c.led3 = DatabotLEDConfig(True, 0, 0, 255)

    c.address = databot_address
    db = PyDatabot(c)
    db.run()


if __name__ == '__main__':
    main()
