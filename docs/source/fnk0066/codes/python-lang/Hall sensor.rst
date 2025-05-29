################################################################
Chapter Hall sensor 
################################################################

In this chapter, we will learn how to use Hall sensor.

Project Hall sensor and LED
****************************************************************

This project uses hall sensor to control the state of LED.

Component List
================================================================

.. table:: 
    :align: center
    :width: 80%

    +-----------------------------------------------+------------------+
    |1. Raspberry Pi (with 40 GPIO) x1              |                  |     
    |                                               | Jumper Wires x6  |       
    |2. GPIO Extension Board & Ribbon Cable x1      |                  |       
    |                                               |  |jumper-wire|   |                                                            
    |3. Breadboard x1                               |                  |                                                                 
    +-----------------------------------------------+------------------+
    | Hall sensor x1                                | LED x1           |
    |                                               |                  |
    |  |Hall_Sensor| :xx-large:`or` |Hall_Sensor_1| |  |red-led|       |                           
    +-----------------------------------------------+------------------+
    | Speaker x1                                    | Resistor 220Ω x1 |
    |                                               |                  |
    |  |Speaker|                                    |  |res-220R|      |                           
    +-----------------------------------------------+------------------+

.. |jumper-wire| image:: ../_static/imgs/jumper-wire.png
.. |Hall_Sensor| image:: ../_static/imgs/Hall_Sensor.png
    :width: 30%
.. |Hall_Sensor_1| image:: ../_static/imgs/Hall_Sensor_1.png
    :width: 40%
.. |red-led| image:: ../_static/imgs/red-led.png
    :width: 20%
.. |res-220R| image:: ../_static/imgs/res-220R.png
    :width: 10%
.. |Speaker| image:: ../_static/imgs/Speaker.png
    :width: 40%

Component knowledge
================================================================

Hall sensor
----------------------------------------------------------------

Hall sensor is a magnetic field sensor made according to the Hall effect. Based on the Hall effect, Hall voltage varies with magnetic field strength. Hall sensors can be divided into linear (analog) Hall sensors and switching Hall sensors. Linear Hall sensors have two outputs: analog output (AO), digital output (DO). Switching Hall sensors only have digital output (DO) and the analog output (AO) output has no effect. In this project, the switch Hall sensor is used. Its use is very simple. 

This module has 4 pins: digital output (DO), analog output (AO), power supply positive pin and power supply negative pin. When the positive and negative pins of the module are connected to a suitable power supply, the module starts to work. Only one pin on the development board is needed to read the digital output (DO) signal of the module. In the project, the speaker is used as the magnetic field source, when you put the sensor close to the magnetic field (speaker), the DO outputs low level, and if the sensor does not sense the magnetic field (speaker), the DO outputs high level.

Below is the pinout of the Hall sensor.

**Pin description:**

.. list-table::
   :align: center
   :header-rows: 1
   :class: product-table

   * - symbol
     - Function

   * - VCC
     - Power supply pin, +3.3V~5.5V  

   * - DO
     - Output control signal

   * - AO
     - Output invalid

   * - GND
     - GND
    
:red:`Please do not use voltage beyond the power supply range to avoid damage to the Hall sensor.`

:red:`For the above two hall sensors, their difference is only the pin sequence is different, please get the Hall sensor, check its sequence, change the corresponding wiring, so as not to cause permanent damage to your raspberry PI.`

Circuit
================================================================

+------------------------------------------------------------------------------------------------+
|   Schematic diagram                                                                            |
|                                                                                                |
|   |Hall_Sensor_Sc|                                                                             |
+------------------------------------------------------------------------------------------------+
|   Hardware connection. If you need any support,please feel free to contact us via:             |
|                                                                                                |
|   support@freenove.com                                                                         | 
|                                                                                                |
|   |Hall_Sensor_Fr| :xx-large:`or` |Hall_Sensor_Fr_1|                                           |
+------------------------------------------------------------------------------------------------+

.. |Hall_Sensor_Sc| image:: ../_static/imgs/Hall_Sensor_Sc.png
.. |Hall_Sensor_Fr| image:: ../_static/imgs/python29_00.png
    :width: 45%
.. |Hall_Sensor_Fr_1| image:: ../_static/imgs/python29_01.png
    :width: 45%

.. note::
    
    :red:`Please check the sequence of your Hall sensor and select the appropriate wiring to avoid permanent damage to your raspberry PI.`

Code
================================================================

Python Code HallSensor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 
    
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.  Use ``cd`` command to enter 29.1.1_HallSensor directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/29.1.1_HallSensor

2.  Use python command to execute code ``HallSensor.py``

.. code-block:: console

    $ python  HallSensor.py

After the program is executed, when the sensor is close to the magnetic field (horn) by hand, the LED will turn on, and if the sensor does not sense the magnetic field (horn), the LED will turn off.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/29.1.1_HallSensor/HallSensor.py
    :linenos: 
    :language: python
    :dedent:

Import the HallSensor class from the sensor module. HallSensor is similar to the MotionSensor class in the GPIO Zero library in that they both actually use the SmoothedInputDevice class.

.. code-block:: python

    from sensor import HallSensor

.. seealso::

    For more information about the methods used by the SmoothedInputDevice class in the GPIO Zero library,please refer to: https://gpiozero.readthedocs.io/en/stable/api_input.html#smoothedinputdevice

Project Hall Sensor and Buzzer
****************************************************************

This project uses Hall sensor to make a simple magnetic field detection sound and light alarm.

Component List
================================================================

.. table:: 
    :align: center
    :width: 80%

    +--------------------------------------------------+-------------------------------------------------+
    |1. Raspberry Pi (with 40 GPIO) x1                 |                                                 |     
    |                                                  | Jumper Wires x6                                 |       
    |2. GPIO Extension Board & Ribbon Cable x1         |                                                 |       
    |                                                  |  |jumper-wire|                                  |                                                            
    |3. Breadboard x1                                  |                                                 |                                                                 
    +--------------------------------------------------+-------------+-----------------------------------+
    | Hall sensor x1                                   | LED x1      | NPN-transistor                    |
    |                                                  |             |                                   |
    |  |Hall_Sensor| :xx-large:`or` |Hall_Sensor_1|    |  |red-led1| |  |NPN-transistor|                 |                           
    +-----------------------+--------------------------+-------------+----------+------------------------+
    | Speaker x1            | Active buzzer x1         | Resistor 220Ω x1       | Resistor 1kΩ x1        |
    |                       |                          |                        |                        |
    |  |Speaker1|           |  |Active-buzzer|         |  |res-220R1|           |  |Resistor-1kΩ|        |                           
    +-----------------------+--------------------------+------------------------+------------------------+

.. |red-led1| image:: ../_static/imgs/red-led.png
    :width: 50%
.. |res-220R1| image:: ../_static/imgs/res-220R.png
    :width: 25%
.. |Speaker1| image:: ../_static/imgs/Speaker.png
    :width: 60%
.. |Active-buzzer| image:: ../_static/imgs/Active-buzzer.png
    :width: 60%
.. |NPN-transistor| image:: ../_static/imgs/NPN-transistor.png
.. |Resistor-1kΩ| image:: ../_static/imgs/Resistor-1kΩ.png
    :width: 28%
    
:red:`For the above two hall sensors, their difference is only the pin sequence is different, please get the Hall sensor, check its sequence, change the corresponding wiring, so as not to cause permanent damage to your raspberry PI.`

Circuit
================================================================

+------------------------------------------------------------------------------------------------+
|   Schematic diagram                                                                            |
|                                                                                                |
|   |Hall_Sensor_Sc_1|                                                                           |
+------------------------------------------------------------------------------------------------+
|   Hardware connection. If you need any support,please feel free to contact us via:             |
|                                                                                                |
|   support@freenove.com                                                                         | 
|                                                                                                |
|   |Hall_Sensor_Fr_2| :xx-large:`or` |Hall_Sensor_Fr_3|                                         |
+------------------------------------------------------------------------------------------------+

.. |Hall_Sensor_Sc_1| image:: ../_static/imgs/Hall_Sensor_Sc_1.png
.. |Hall_Sensor_Fr_2| image:: ../_static/imgs/python29_02.png
    :width: 48%
.. |Hall_Sensor_Fr_3| image:: ../_static/imgs/python29_03.png
    :width: 48%

.. note::
    
    :red:`Please check the sequence of your Hall sensor and select the appropriate wiring to avoid permanent damage to your raspberry PI.`

Code
================================================================

Python Code Alertor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.  Use ``cd`` command to enter 29.2.1_Alertor directory of Python code

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/29.2.1_Alertor

2.  Use python command to execute code ``Alertor.py``

.. code-block:: console

    $ python Alertor.py

After the program is executed, every time the sensor is close to the magnetic field (speaker) by hand, the buzzer will sound an alarm, and the LED will flash to remind.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/29.2.1_Alertor/Alertor.py
    :linenos: 
    :language: python
    :dedent: