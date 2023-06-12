from databot.PyDatabot import PyDatabot, DatabotConfig, DatabotBLEConfig


class CustomPyDatabotConsumer(PyDatabot):

    async def run_queue_consumer(self):
        self.logger.info("Starting queue consumer")

        while True:
            # Use await asyncio.wait_for(queue.get(), timeout=1.0) if you want a timeout for getting data.
            epoch, data = await self.queue.get()
            if data is None:
                self.logger.info(
                    "Got message from client about disconnection. Exiting consumer loop..."
                )
                break
            else:
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
