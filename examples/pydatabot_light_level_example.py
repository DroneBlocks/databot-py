from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)

from databot.PyDatabot import PyDatabot, DatabotConfig


def main():
    c = DatabotConfig()
    c.ambLight = True
    c.address = "774B790E-35DE-4950-842D-81446C06240B"
    db = PyDatabot(c)
    db.run()


if __name__ == '__main__':
    main()
