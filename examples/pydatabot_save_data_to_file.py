import json
from pathlib import Path

from databot.PyDatabot import PyDatabot, DatabotConfig


class SaveToFileDatabotCollector(PyDatabot):

    async def run_queue_consumer(self):
        self.logger.info("Starting queue consumer")
        file_name = "data/test_data.txt"
        file_path = Path(file_name)
        if file_path.exists():
            file_path.unlink(missing_ok=True)

        with file_path.open("w", encoding="utf-8") as f:

            for i in range(0, 30):
                # Use await asyncio.wait_for(queue.get(), timeout=1.0) if you want a timeout for getting data.
                epoch, data = await self.queue.get()
                if data is None:
                    self.logger.info(
                        "Got message from client about disconnection. Exiting consumer loop..."
                    )
                    break
                else:
                    data['timestamp'] = epoch
                    f.write(json.dumps(data))
                    f.write("\n")
                    self.logger.info(f"wrote record[{i}]: {epoch}")
            print("Done collecting data.  Safe to exit program")


def main():
    c = DatabotConfig()
    c.accl = True
    c.Laccl = True
    c.gyro = True
    c.magneto = False
    c.address = "774B790E-35DE-4950-842D-81446C06240B"
    db = SaveToFileDatabotCollector(c)
    db.run()


if __name__ == '__main__':
    main()
