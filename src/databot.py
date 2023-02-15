import asyncio
import logging
from bleak import BleakClient, BleakScanner, BLEDevice
from json import JSONEncoder

class LED:
    def __init__(self, state: bool, R: int, Y: int, B: int):
        self.state: bool = state
        self.R: int = R
        self.Y: int = Y
        self.B: int = B

class Config:

    def __init__(self):
        self.refresh: int = 500
        self.decimal: int = 2
        self.timeFactor: int = 500
        self.timeDec: int = 2
        self.accl: bool = False
        self.laccl: bool = False
        self.gyro: bool = False
        self.magneto: bool = False
        self.IMUTemp: bool = False
        self.Etemp1: bool = False
        self.Etemp2: bool = False
        self.pressure: bool = False
        self.alti: bool = False
        self.ambLight: bool = False
        self.rgbLight: bool = False
        self.UV: bool = False
        self.co2: bool = False
        self.voc: bool = False
        self.hum: bool = False
        self.Sdist: bool = False
        self.Ldist: bool = False
        self.noise: bool = False
        self.gesture: bool = False
        self.sysCheck: bool = False
        self.usbCheck: bool = False
        self.altCalib: bool = False
        self.humCalib: bool = False
        self.DtmpCal: bool = False
        self.led1: LED = LED(True, 255, 0, 0)
        self.led2: LED = LED(True, 0, 255, 0)
        self.led3: LED = LED(True, 0, 0, 255)

    def enable_accelerometer(self, enabled: bool):
        self.accl = enabled

    def enable_l_accelerometer(self, enabled: bool):
        self.laccl = enabled

    def enable_gyroscope(self, enabled: bool):
        self.gyro = enabled

    def enable_magnetometer(self, enabled: bool):
        self.magneto = enabled

    def to_json(self):
        return ConfigEncoder().encode(self)

class ConfigEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Databot:

    def __init__(self, config: Config):
        self.device: BLEDevice
        self.config: Config = config
        self.address: str = "94:3C:C6:99:AA:82"
        self.service_uuid: str = "0000ffe0-0000-1000-8000-00805f9b34fb"
        self.read_uuid: str = "0000ffe1-0000-1000-8000-00805f9b34fb"
        self.write_uuid: str = "0000ffe2-0000-1000-8000-00805f9b34fb"
        self.logger: logging  = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    
    async def connect(self):
        self.logger.info("connecting")
        self.device = await BleakScanner(None, [self.service_uuid]).find_device_by_address(self.address)
        async with BleakClient(self.device) as client:
            service = client.services.get_service(self.service_uuid)

            write_char = service.get_characteristic(self.write_uuid)
            await client.write_gatt_char(write_char, bytearray(self.config.to_json(), 'utf-8'), True)
            await asyncio.sleep(2)
            await client.write_gatt_char(write_char, bytearray('1.0', 'utf-8'), True)

            read_char = service.get_characteristic(self.read_uuid)
            await client.start_notify(read_char, self.process_sensor_data)
            await asyncio.sleep(15)
            await client.stop_notify(read_char)

    def get_encoded_config(self):
        return ConfigEncoder().encode(self.config)


    def process_sensor_data(self, characteristic: str, data: bytearray):
        self.logger.info(data.decode())