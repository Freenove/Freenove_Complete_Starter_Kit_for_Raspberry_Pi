##############################################################################
Chapter U-shaped photoelectric sensor
##############################################################################


In this chapter, we will learn how to use a U-shaped photoelectric sensor.

Project U-shaped photoelectric sensor and LED
****************************************************************

This project uses a U-shaped photoelectric sensor to control the state of the LED.	

Component List
================================================================

.. table:: 
    :align: center  
    :width: 80%

    +-------------------------------------------------+------------------------------------+
    |1. Raspberry Pi (with 40 GPIO) x1                |                                    |     
    |                                                 | Jumper Wires x6                    |       
    |2. GPIO Extension Board & Ribbon Cable x1        |                                    |       
    |                                                 |  |jumper-wire|                     |                                                            
    |3. Breadboard x1                                 |                                    |                                                                 
    +-------------------------------------------------+-----------------+------------------+
    | TTP223 Touch Sensor x1                          | LED x1          | Resistor 220Ω x1 |   
    |                                                 |                 |                  |       
    | |photoelectric| :xx-large:`or` |photoelectric_1||  |red-led1|     | |res-220R1|      |       
    +-------------------------------------------------+-----------------+------------------+

.. |jumper-wire| image:: ../_static/imgs/jumper-wire.png
.. |photoelectric| image:: ../_static/imgs/photoelectric.png
    :width: 35%
.. |photoelectric_1| image:: ../_static/imgs/photoelectric_1.png
    :width: 30%
.. |res-220R1| image:: ../_static/imgs/res-220R.png
    :width: 15%
.. |red-led1| image:: ../_static/imgs/red-led.png
    :width: 30%

Component knowledge
================================================================

U-shaped photoelectric sensor
----------------------------------------------------------------

The U-shaped photoelectric sensor is a through-beam photoelectric sensor, which consists of a transmitting end and a receiving end. Its working principle is blocking and conducting the infrared emission light will change the current induced by the infrared receiving tube. 

This module has 4 pins: digital output (DO), analog output (AO), power supply positive pin and power supply negative pin. When the positive and negative pins of the module are connected to a suitable power supply, the module starts to work. Only one pin on the development board is needed to read the digital output (DO) signal of the module. When the photoelectric sensor is blocked, the digital signal pin outputs a low level. If the photoelectric sensor is not blocked, it outputs a high level.

Below is the pinout of the touch sensor.

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
     - Output control signal(High or low level)

   * - AO
     - Output invalid

   * - GND
     - GND

:red:`Please do not use the voltage beyond the power supply range to avoid damage to the U-shaped photoelectric sensor.`

:red:`The difference between the above two U-type photoelectric sensors is that in addition to the different pin sequence, the output signal is opposite when you block it, that is, there are modules that output high level and low level U-type photoelectric sensor. The specific module is subject to the one in your hand. Please check the pin sequence of your U-shaped photoelectric sensor and replace the appropriate wiring to avoid permanent damage to your raspberry PI.`

Circuit
================================================================

+-------------------------------------------------------------------------------------+
|   Schematic diagram                                                                 |
|                                                                                     |
|   |photoelectric_Sc|                                                                |
+-------------------------------------------------------------------------------------+
|   Hardware connection. If you need any support,please feel free to contact us via:  |
|                                                                                     |
|   support@freenove.com                                                              | 
|                                                                                     |
|   |photoelectric_Fr|                                                                |
+-------------------------------------------------------------------------------------+

.. |photoelectric_Sc| image:: ../_static/imgs/photoelectric_Sc.png
.. |photoelectric_Fr| image:: ../_static/imgs/photoelectric_Fr.png

.. note::
    
    :red:`Please check the sequence of your U-shaped photoelectric sensor and select the appropriate wiring to avoid permanent damage to your raspberry PI.`

Code
================================================================

C Code PhotoSensor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.  Use cd command to enter 28.1.1_PhotoSensor directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/28.1.1_PhotoSensor

2.  Use following command to compile " PhotoSensor.c" and generate executable file "PhotoSensor".

.. code-block:: console

    $ gcc PhotoSensor.c -o PhotoSensor -lwiringPi

3.  Run the generated file " PhotoSensor"

.. code-block:: console

    $ sudo ./PhotoSensor    

When you use the module whose output signal is low level, after the program is executed, when the photoelectric sensor is blocked, the LED lights up, when the photoelectric sensor is not blocked, the LED turns off.

When you use the module whose output signal is low level, after the program is executed, when the photoelectric sensor is blocked, the LED lights up, when the photoelectric sensor is not blocked, the LED turns off.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/28.1.1_PhotoSensor/PhotoSensor.c
    :linenos: 
    :language: C



Project U-shaped photoelectric sensor and buzzer
****************************************************************

This project uses U-shaped photoelectric sensor to make a simple sound and light alarm. 

Component List
================================================================

.. table:: 
    :align: center
    :width: 80%

    +------------------------------------------------------------+-------------------------------------------------+
    |1. Raspberry Pi (with 40 GPIO) x1                           |                                                 |     
    |                                                            | Jumper Wires x10                                |       
    |2. GPIO Extension Board & Ribbon Cable x1                   |                                                 |       
    |                                                            |  |jumper-wire|                                  |                                                            
    |3. Breadboard x1                                            |                                                 |                                                                 
    +--------------------------------------------------+---------+------------------------+------------------------+
    | Active buzzer x1                                 | NPN transistorx1 (S8050)         | Resistor 1kΩx1         |     
    |                                                  |                                  |                        |       
    |  |Active-buzzer|                                 | |NPN-transistor|                 | |Resistor-1kΩ|         |       
    +--------------------------------------------------+----------------------------------+------------------------+
    | U-shaped photoelectric sensor x1                 | LED x1                           | Resistor 220Ω x1       |     
    |                                                  |                                  |                        |       
    | |photoelectric| :xx-large:`or` |photoelectric_1| | |red-led|                        | |res-220R|             |       
    +--------------------------------------------------+----------------------------------+------------------------+

.. |Active-buzzer| image:: ../_static/imgs/Active-buzzer.png
    :width: 40%
.. |res-220R| image:: ../_static/imgs/res-220R.png
    :width: 15%
.. |NPN-transistor| image:: ../_static/imgs/NPN-transistor.png
    :width: 30%
.. |Resistor-1kΩ| image:: ../_static/imgs/Resistor-1kΩ.png
    :width: 15%
.. |red-led| image:: ../_static/imgs/red-led.png
    :width: 30%

Circuit
================================================================

+------------------------------------------------------------------------------------------------+
|   Schematic diagram                                                                            |
|                                                                                                |
|   |photoelectric_Sc_1|                                                                         |
+------------------------------------------------------------------------------------------------+
|   Hardware connection. If you need any support,please feel free to contact us via:             |
|                                                                                                |
|   support@freenove.com                                                                         | 
|                                                                                                |
|   |photoelectric_Fr_2|                                                                         |
|                                                                                                |
|   .. centered::                                                                                |
|      :xx-large:`or`                                                                            |
|                                                                                                |
|   |photoelectric_Fr_3|                                                                         |
+------------------------------------------------------------------------------------------------+

.. |photoelectric_Sc_1| image:: ../_static/imgs/photoelectric_Sc_1.png
.. |photoelectric_Fr_2| image:: ../_static/imgs/photoelectric_Fr_2.png
    :width: 80%
.. |photoelectric_Fr_3| image:: ../_static/imgs/photoelectric_Fr_3.png
    :width: 80%

.. note::
    
    :red:`Please check the sequence of your U-shaped photoelectric sensor and select the appropriate wiring to avoid permanent damage to your raspberry PI.`

Code
================================================================

C Code Alertor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.  Use ``cd`` command to enter 28.2.1_Alertor directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/28.2.1_Alertor

2.  Use following command to compile ``Alertor.c`` and generate executable file ``Alertor``.

.. code-block:: console

    $ gcc Alertor.c -o Alertor -lwiringPi

3.  Run the generated file ``Alertor``

.. code-block:: console

    $ sudo ./Alertor

After the program is executed, every time the U-shaped photoelectric sensor is blocked by hand, the buzzer will sound an alarm, and the LED will flash to remind.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/28.2.1_Alertor/Alertor.c
    :linenos: 
    :language: C

The wiringPiISR() function associates the sensor pins with sensorEven().Because there are high level triggering module and low level triggering module in the U-type photoelectric sensor, we use the double-edge detection method here to make the program compatible with the module in your hand. When sensorPin detects low level or high level, it will call and execute the sensorEven() function.

.. code-block:: c
    :linenos: 

    wiringPiISR(sensorPin,INT_EDGE_BOTH,&sensorEven);
    void sensorEven(void){
        alarm(3);
    }

The function alarm() is used to control the active buzzer to emit an alarm sound and control the LED to flash at the same time. Use variable times to pass in the number of times the alarm sounds and the LED blinks.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/28.2.1_Alertor/Alertor.c
    :linenos: 
    :language: C
    :lines: 14-23
    :dedent:

.. c:function:: int wiringPiISR (int pin, int edgeType, void (*function)(void)) ;

    This is an interrupt detection function. The first parameter specifies the IO port to detect. The second parameter specifies the trigger method to detect. The third parameter specifies the function name. The function will be executed when the specified action is detected.
    
    The following are common detection triggers:
    
    **INT_EDGE_FALLING**: falling edge trigger 
    
    **INT_EDGE_RISING**: rising edge trigger 
    
    **INT_EDGE_BOTH**: triggers both up and down