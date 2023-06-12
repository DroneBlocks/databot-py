from databot.PyDatabot import PyDatabot, DatabotConfig, DatabotBLEConfig


class CustomPyDatabotConsumer(PyDatabot):

    def process_databot_data(self, epoch, data):
        self.logger.info(f"{data}")
        self.logger.info(f"Linear Acceleration: {data['linear_acceleration_x']}, {data['linear_acceleration_y']}, {data['linear_acceleration_z']}")


def main():
    c = DatabotConfig()
    c.Laccl = True
    c.address = "774B790E-35DE-4950-842D-81446C06240B"
    db = CustomPyDatabotConsumer(c)
    db.run()


if __name__ == '__main__':
    main()
