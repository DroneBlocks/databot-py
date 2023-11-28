from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)

from databot.PyDatabot import PyDatabot, DatabotConfig


def main():
    c = DatabotConfig()
    c.humTemp = True
    c.refresh = 2000 # change the refresh rate to every 2 seconds
    c.timeDec = 1 # change the decimals for the time to 1
    c.decimal = 3 # have the humidity temp use 3 decimal plces
    c.address = PyDatabot.get_databot_address()
    db = PyDatabot(c)
    db.run()


if __name__ == '__main__':
    main()
