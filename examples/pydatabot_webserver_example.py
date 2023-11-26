from databot.PyDatabot import start_databot_webserver, PyDatabot, PyDatabotSaveToQueueDataCollector, DatabotConfig

def main():
    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto = True
    c.ambLight = True
    c.co2 = True
    c.hum = True
    c.pressure = True
    c.Etemp1 = True
    c.refresh = 1000
    c.address = PyDatabot.get_databot_address()
    db = PyDatabotSaveToQueueDataCollector(c)

    t =start_databot_webserver(queue_data_collector=db, host="localhost", port=8321)
    db.run()


if __name__ == '__main__':
    main()
