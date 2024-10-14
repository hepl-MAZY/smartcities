# RGB light in response to music + decent bpm calculator 

## Overview

RGB light response to sound variation using the sound sensor 

- Reads sound sensor value
- When above threshold turns a random colored light on
- IF a beat is detected, it will calculate the BPM 

Note: Volume test before playing the music (ajust according to threshold)

## Components

- Sound sensor
- RGB light

## Circuit diagram 

Here are the connections:

- RGB connected to Pin D18
- Sound sensor connected to A0


## Program

The program will read the sound sensor value and if the value is above the threshold (10% of 8 bit ADC here), it will display a random colored light. If value below threshold, no light will be shown.

## Addtionnal features

- Calculates BPM 
