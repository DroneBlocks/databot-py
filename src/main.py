import asyncio
from databot import Config, Databot

async def main():
    config: Config = Config()
    config.enable_accelerometer(True)
    config.enable_gyroscope(True)
    config.enable_magnetometer(True)

    print(config.to_json())

    databot: Databot = Databot(config)
    await databot.connect()

asyncio.run(main())