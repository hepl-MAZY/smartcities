# LED Blinking project

## Overview

Led blinking at different speed depending the number of times the button was pressed :

- ONCE : led blinking forever at 0.5Hz (2s)
- TWICE : faster than 0.5hz -> 1hz (1s)
- THREE : led turns off 

## Components

- LED
- Button 

## Circuit diagram 

Here are the connections:

- LED connected to PIN D16
- BUTTON connected to PIN D18 

## Program

The program will increment button_val each time the button is pressed, then resets as zero when it reaches the third time. 

## Addtionnal features

- Transitions between 2 differents speed blinking leds temporary blinks at a higher speed (~500ms)