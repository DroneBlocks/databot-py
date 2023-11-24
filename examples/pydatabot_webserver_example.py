import threading

from databot.PyDatabot import PyDatabot, PyDatabotSaveToQueueDataCollector, DatabotConfig

web_databot: PyDatabotSaveToQueueDataCollector = None

from bottle import route, run


@route('/')
def index():
    item = web_databot.get_item()
    return item


def worker(pydb: PyDatabotSaveToQueueDataCollector):
    global web_databot
    web_databot = pydb

    run(host='localhost', port="8321")


def main():
    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto = True
    c.ambLight = True
    c.co2 = True
    c.address = PyDatabot.get_databot_address()
    db = PyDatabotSaveToQueueDataCollector(c)

    threading.Thread(target=worker, args=(db,), daemon=True).start()

    db.run()


if __name__ == '__main__':
    main()
