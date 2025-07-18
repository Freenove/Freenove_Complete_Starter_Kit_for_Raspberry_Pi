################################################################
Chapter Infrared Obstacle Avoidance Sensor
################################################################

In this chapter, we will learn how to use infrared obstacle avoidance sensor.

Project Infrared obstacle avoidance sensor and LED
****************************************************************

This project uses infrared obstacle avoidance sensor to change the state of LED.

Component List
================================================================

.. table:: 
    :align: center
    :width: 80%
    :class: table-line

    +--------------------------------------------------+-------------------------------------+
    |1. Raspberry Pi (with 40 GPIO) x1                 |                                     |
    |                                                  | Jumper Wires x6                     |
    |2. GPIO Extension Board & Ribbon Cable x1         |                                     |
    |                                                  |  |jumper-wire|                      |
    |3. Breadboard x1                                  |                                     |
    +--------------------------------------------------+------------------+------------------+
    |Infrared obstacle avoidance sensor x1             | LED x1           | Resistor 220Ω x1 |
    |                                                  |                  |                  |
    |  |Infrared_sensor|                               |  |red-led|       |  |res-220R|      |
    +--------------------------------------------------+------------------+------------------+

.. |jumper-wire| image:: ../_static/imgs/jumper-wire.png
    :width: 80%
.. |Infrared_sensor| image:: ../_static/imgs/Infrared_sensor.png
    :width: 80%
.. |red-led| image:: ../_static/imgs/red-led.png
    :width: 25%
.. |res-220R| image:: ../_static/imgs/res-220R.png
    :width: 15%

Component knowledge
================================================================

Infrared obstacle avoidance sensor
----------------------------------------------------------------

The infrared obstacle avoidance sensor module is a distance adjustable obstacle avoidance sensor. The sensor has strong adaptability to ambient light and high precision. It has a pair of infrared emitting and receiving tubes. The transmitting tube emits infrared rays of a certain frequency. When the detection direction encounters an obstacle (reflecting surface), the infrared rays are reflected back and are received by the receiving tube. The indicator light is on at this time. After the circuit processing, the signal output pin outputs digital signal. The detection distance can be adjusted by the potentiometer knob, the effective distance is 2 ~ 30cm, and the detection angle is 35°. 

This module has 3 pins: signal pin, power positive pin and power negative pin. When the positive and negative pins of the module are connected to a suitable power supply, the module starts to work. At this time, only one pin on the development board is needed to read the output signal of the module. When the module is in use, the detection distance can be adjusted to a suitable value through the potentiometer knob. You can use your hand to block the module at a certain distance. When the infrared obstacle avoidance sensor is blocked, the signal pin outputs a low level; if the infrared obstacle avoidance sensor is not blocked, it outputs a high level.

Below is the pinout of infrared obstacle avoidance sensor.

**Pin description:**

.. list-table::
   :align: center
   :header-rows: 1
   :class: zebra

   * - symbol
     - Function

   * - OUT
     - Output control signal 

   * - VCC
     - Power supply pin, +3.3V~5.0V

   * - GND
     - GND

Please do not use the voltage beyond the power supply range to avoid damage to the infrared obstacle avoidance sensor.

.. table:: 
    :align: center
    :width: 80%
    :class: table-line

    +------------------------------------------------------------------------------------+
    |   Schematic diagram                                                                |
    |                                                                                    |
    |   |Infrared_sensor_Sc|                                                             |
    +------------------------------------------------------------------------------------+
    |   Hardware connection. If you need any support,please feel free to contact us via: |
    |                                                                                    |
    |   support@freenove.com                                                             | 
    |                                                                                    |
    |   |Infrared_sensor_Fr|                                                             |
    +------------------------------------------------------------------------------------+

.. |Infrared_sensor_Sc| image:: ../_static/imgs/Infrared_sensor_Sc.png
.. |Infrared_sensor_Fr| image:: ../_static/imgs/Infrared_sensor_Fr.png

Code
================================================================

Python Code InfraredSensor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.  Use ``cd`` command to enter 30.1.1_InfraredSensor directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/30.1.1_InfraredSensor

2.  Use python command to execute code ``InfraredSensor.py``

.. code-block:: console

    $ python InfraredSensor.py

After the program is executed, when you block the sensor with your hand at a certain distance or the sensor encounters an obstacle, the LED will turn on, and when the sensor is not blocked or the sensor does not encounter an obstacle, the LED will turn off.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/30.1.1_InfraredSensor/InfraredSensor.py
    :linenos: 
    :language: python

Import the InfraredSensor class from the sensor module. InfraredSensor is similar to the MotionSensor class in the GPIO Zero library in that they both actually use the SmoothedInputDevice class.

.. code-block:: python

    from sensor import InfraredSensor

.. seealso::

    For more information about the methods used by the SmoothedInputDevice class in the GPIO Zero library,please refer to: https://gpiozero.readthedocs.io/en/stable/api_input.html#smoothedinputdevice

Project Infrared obstacle avoidance sensor and buzzer
****************************************************************

This project uses an infrared obstacle avoidance sensor to make a simple reminder.

Component List
================================================================

.. table:: 
    :align: center
    :width: 80%
    :class: table-line

    +-------------------------------------------+---------------------------------------------+
    |1. Raspberry Pi (with 40 GPIO) x1          |                                             |
    |                                           | Jumper Wires x10                            |
    |2. GPIO Extension Board & Ribbon Cable x1  |                                             |
    |                                           |  |jumper-wire|                              |
    |3. Breadboard x1                           |                                             |
    +-------------------------------------------+--------------------------+------------------+
    |Active buzzer x1                           | NPN transistorx1 (S8050) | Resistor 1kΩx1   |
    |                                           |                          |                  |
    |  |Active-buzzer|                          |  |NPN-transistor|        |  |Resistor-1kΩ|  |
    +-------------------------------------------+--------------------------+------------------+
    |Infrared obstacle avoidance sensor x1      | LED x1                   | Resistor 220Ω x1 |
    |                                           |                          |                  |
    |  |Infrared_sensor|                        |  |red-led|               |  |res-220R|      |
    +-------------------------------------------+--------------------------+------------------+

.. |Active-buzzer| image:: ../_static/imgs/Active-buzzer.png
    :width: 30%
.. |NPN-transistor| image:: ../_static/imgs/NPN-transistor.png
    :width: 40%
.. |Resistor-1kΩ| image:: ../_static/imgs/Resistor-1kΩ.png
    :width: 20%

Circuit
================================================================

.. table:: 
    :align: center
    :width: 80%
    :class: table-line

    +-------------------------------------------------------------------------------------+
    |   Schematic diagram                                                                 |
    |                                                                                     |
    |   |Infrared_sensor_Sc_1|                                                            |
    +-------------------------------------------------------------------------------------+
    |   Hardware connection. If you need any support,please feel free to contact us via:  |
    |                                                                                     |
    |   support@freenove.com                                                              | 
    |                                                                                     |
    |   |Infrared_sensor_Fr_1|                                                            |
    +-------------------------------------------------------------------------------------+

.. |Infrared_sensor_Sc_1| image:: ../_static/imgs/Infrared_sensor_Sc_1.png
.. |Infrared_sensor_Fr_1| image:: ../_static/imgs/Infrared_sensor_Fr_1.png

Code
================================================================

Python Code Alertor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 

    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.  Use ``cd`` command to enter 30.2.1_Alertor directory of Python code

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/30.2.1_Alertor

2.  Use python command to execute code ``Alertor.py``

.. code-block:: console

    $ python Alertor.py

After the program is executed, when you block the sensor with your hand at a certain distance or the sensor encounters an obstacle, the buzzer will sound a reminder, and the LED will flash to remind you.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/30.2.1_Alertor/Alertor.py
    :linenos: 
    :language: python
    :dedent: