# databot-py
A simple bluetooth interface for databot sensors

## Install

It is recommended that you use a package manager like `pip-tools` or `poetry` and do not rely on a existing requirements.txt

The reason is that operating system dependent libraries need to be installed to support bluetooth.

Basic installation, just pip install the `databot-py` package from PyPI.

e.g.
`pip install databot-py`

If using pip-tools in your project then 

* pip install pip-tools
* create a file called `requirements.in`
* add:  `databot-py`
* pip-compile
* pip-sync

This will install all of the OS specific versions of libraries.

## Classes
![classes](./media/classes.png)

### PyDatabot

This class is the base class implementation for interacting with the databot over bluetooth.

This class can be used directly and will print the data read from the databot.

However, this class is really meant to be inherited from and the derived class should override the method `process_databot_data`.

The `process_databot_data` method will be called for each data record from the databot and the derived class can then process the data in a specific way.

### PyDatabotSaveToFileDataCollector

This class extends the `PyDatabot` class and overrides the `process_databot_data` method to save values to a file.

This class is used primarily to easily read values from the databot and save them to a file for future processing.

### PyDatabotSaveToQueueDataCollector

This class extends the `PyDatabot` class and overrides the `process_databot_data` method to save values to an internal queue.

This class is used primarily with the databot webserver to provide the latest readings from the databot.

## Local WebServer Interface

A local web service interface is available to get data values from the databot.

Create an instance of the `PyDatabotSaveToQueueDataCollector` class with the desired sensors configured.  

Then call the function `start_databot_webserver` in the PyDatabot module passing a reference to the `PyDatabotSaveToQueueDataCollector`

See the example in:

`examples/pydatabot_webserver_example.py`

## Run Locally

### Install Local Requirements

Recommended steps to install locally

* `pip install pip-tools` or `python -m pip install pip-tools`
* `pip-compile`
* `pip-sync`

## Examples

### Locate the Databot BlueTooth address

Every databot has a bluetooth address.  The find the address use the static method:

`PyDatabot.get_databot_address()`

and it is used in the configration like:

```python
    c = DatabotConfig()
    c.address = PyDatabot.get_databot_address()

```


### Simple Databot interfacing to print data values

This example will show you how to connect to the `databot` and display the selected data values.

### Custom Databot consumer

The PyDatabot class performs all of the necessary steps to interface with the databot and collect data from the databot.  However, the PyDatabot class does not do anything with the collected data excepti to print it.

For any custom processing of the databot data, a custom databot consumer is needed.

For an example and test of how to do this see:

`examples/pydatabot_custom_consumer.py`

### Save databot data to file

This example shows how to write the collected values to a file for later processing

`examples/pydatabot_save_data_to_file.py`

### View Ambient Light Sensor Values

This example shows how to read ambient light sensor values.  Start the example and then cover the sensor with your hand.

Notice the light level values goes down.

`examples/pydatabot_light_level_example.py`

### Breath Detector

This example shows how to read co2 level.  Start the example and then breath on the databot.
Watch the co2 values go up. 

`examples/pydatabot_light_level_example.py`

### Databot WebServer Access

This example shows how to start a simple webserver interface to get the current values from the databot.

`examples/pydatabot_webserver_example.py`

You can then open a browser and navigate to:
`http://localhost:8321`

And the sensor values will be displayed as a JSON string.
