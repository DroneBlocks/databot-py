import threading
import time

from databot.PyDatabot import PyDatabot, PyDatabotSaveToQueueDataCollector, DatabotConfig


def worker(pydb: PyDatabotSaveToQueueDataCollector, wait_time_in_sec:int):
    while True:
        item = pydb.get_item()
        print(f'Working on {item}')
        time.sleep(wait_time_in_sec)


def main():

    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto = True
    c.address = PyDatabot.get_databot_address()
    db = PyDatabotSaveToQueueDataCollector(c)

    threading.Thread(target=worker, args=(db,0.5), daemon=True).start()

    db.run()


if __name__ == '__main__':
    main()
