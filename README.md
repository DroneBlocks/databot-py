# databot-py
A simple bluetooth interface for databot sensors

## Install

TBD Add instructions here to describe how to install the package into a project

e.g.
`pip install databot-py`

## Run Locally

### Install Local Requirements

Recommended steps to install locally

* `pip install pip-tools` or `python -m pip install pip-tools`
* `pip-compile --resolver=backtracking`
* `pip-sync`

## Examples

### Locate the Databot BlueTooth address

With the databot turned on, run the file:

`examples/databot_discovery.py`

If the Databot BLE device address can be found it will be printed in the terminal.  You will need this address when configuring the PyDatabot instance.

Specifically in the examples.

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
