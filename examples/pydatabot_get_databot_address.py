from pathlib import Path
import sys

root_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(root_dir)

from databot.PyDatabot import PyDatabot


def main():
    print(PyDatabot.get_databot_address())


if __name__ == '__main__':
    main()
