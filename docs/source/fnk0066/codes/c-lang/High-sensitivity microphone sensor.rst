##############################################################################
Chapter High-sensitivity microphone sensor
##############################################################################

In this chapter, we will learn how to use High-sensitivity microphone sensor.

Project High-sensitivity microphone sensor and LED
****************************************************************

This project will use a high-sensitivity microphone sensor to make a sound-controlled light.

Component List
================================================================

+-------------------------------------------------+-------------------------------------------------+
|1. Raspberry Pi (with 40 GPIO) x1                |                                                 |     
|                                                 | Jumper Wires x6                                 |       
|2. GPIO Extension Board & Ribbon Cable x1        |                                                 |       
|                                                 |  |jumper-wire|                                  |                                                            
|3. Breadboard x1                                 |                                                 |                                                                 
+---------------------------------------+---------+------------------------+------------------------+
| High-sensitivity microphone sensor x1 | LED x1                           | Resistor 220Ω x1       |     
|                                       |                                  |                        |       
|  |microphone|                         | |red-led|                        | |res-220R|             |       
+---------------------------------------+----------------------------------+------------------------+

.. |jumper-wire| image:: ../_static/imgs/jumper-wire.png
.. |microphone| image:: ../_static/imgs/microphone.png
    :width: 30%
.. |res-220R| image:: ../_static/imgs/res-220R.png
    :width: 15%
.. |red-led| image:: ../_static/imgs/red-led.png
    :width: 50%

Component knowledge
================================================================

High-sensitivity microphone sensor
----------------------------------------------------------------

The high-sensitivity microphone sensor module is a component that accepts sound waves and converts them into electrical signals, which can detect the sound intensity in the surrounding environment. 

When using it, it should be noted that this sensor can only identify the presence or absence of sound (according to the vibration principle), but cannot identify the size of the sound or the sound of a specific frequency.

This module has 4 pins: digital output (DO), analog output (AO), power supply positive pin and power supply negative pin. AO can output the voltage signal of the microphone in real time. When the ambient sound intensity does not reach the set threshold, the DO outputs a low-level signal, and when the ambient sound intensity exceeds the set threshold, it outputs a high-level signal, and the sensitivity can be adjusted by a potentiometer. When in use, adjust the potentiometer to make the sensitivity to sound reach a more appropriate value, and then read the digital output signal of the module through a pin on the development board. You can speak to the sensor. When the sensor detects a speaking sound, the DO pin outputs a high level; when the sensor does not detect a speaking sound, the DO pin outputs a low level.

Below is the pinout of the high-sensitivity microphone sensor.

**Pin description:**

.. list-table::
   :align: center
   :header-rows: 1
   :class: product-table

   * - symbol
     - Function

   * - DO
     - Digital signal output

   * - VCC
     - Power supply pin, +3.3V~5.0V
    
   * - GND
     - GND
     
   * - AO
     - Analog signal output

Since the default sensitivity of the high-sensitivity microphone sensor is high, the two LED lights on the module are lit up after power-on, and the sensitivity should be adjusted to an appropriate value at this time. When the potentiometer is adjusted clockwise, the module identification sensitivity increases; When counterclockwise adjustment potentiometer, module recognition sensitivity decreases. Please adjust the potentiometer before using the module to make its sensitivity reach the appropriate value. Under normal circumstances, you need counterclockwise rotation of the potentiometer, so that the output of the module LED off, when the sensitivity is low can be appropriate clockwise adjustment of the potentiometer, please ensure that your sensor output LED is extinguished when energized, in order to identify the sound.

Please do not use voltage beyond the power supply range to avoid damage to the high-sensitivity microphone sensor.

Circuit
================================================================

+------------------------------------------------------------------------------------------------+
|   Schematic diagram                                                                            |
|                                                                                                |
|   |microphone_Sc|                                                                              |
+------------------------------------------------------------------------------------------------+
|   Hardware connection. If you need any support,please feel free to contact us via:             |
|                                                                                                |
|   support@freenove.com                                                                         | 
|                                                                                                |
|   |microphone_Fr|                                                                              |
+------------------------------------------------------------------------------------------------+

.. |microphone_Sc| image:: ../_static/imgs/microphone_Sc.png
.. |microphone_Fr| image:: ../_static/imgs/microphone_Fr.png

video: https://www.youtube.com/watch?v=W7fi0Sohpi0

.. raw:: html

   <iframe style="display: block; margin: 0 auto;" height="421.875" width="750" src="https://www.youtube.com/embed/W7fi0Sohpi0" frameborder="0" allowfullscreen></iframe>

Code
================================================================

First observe the project result, and then learn about the code in detail.

.. hint:: 
    
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.  Use ``cd`` command to enter 26.1.1_VoiceLamp directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/26.1.1_VoiceLamp

2.  Use following command to compile ``VoiceLamp.c`` and generate executable file ``VoiceLamp``.

.. code-block:: console

    $ gcc VoiceLamp.c -o VoiceLamp -lwiringPi

3.  Run the generated file ``VoiceLamp``

.. code-block:: console

    $ sudo ./VoiceLamp

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/26.1.1_VoiceLamp/VoiceLamp.c
    :linenos: 
    :language: C

Read the signal pin of the high-sensitivity microphone sensor, and determine whether the state of the sensor is high level. If it is high level, the LED will continue to turn on for 5 seconds.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/26.1.1_VoiceLamp/VoiceLamp.c
    :linenos: 
    :language: C
    :lines: 20-29
    :dedent: