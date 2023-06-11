from databot.PyDatabot import PyDatabot, DatabotConfig


def main():
    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto =True
    c.address = "774B790E-35DE-4950-842D-81446C06240B"
    db = PyDatabot(c)
    db.run()


if __name__ == '__main__':
    main()
