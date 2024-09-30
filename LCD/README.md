# Thermostat 

## Overview

DHT11 temperature displays on lcd display with set temperature with rotary angle sensor.

- Reads rotary angle value
- Displays set temperature value base on rotary value (15-35 °C)
- Triggers blinking led AND/OR buzzer  

## Components

- LED
- Buzzer
- Rotary angle sensor
- DHT11

## Circuit diagram 

Here are the connections:

- LED connected to PIN D16
- Buzzer connected to PIN D20
- Rotary angle sensor connected to PIN A0
- DHT11 sensor connected to PIN 18

## Program

The program will read the rotary angle value then translate it into a temperature value then displays on lcd screen. It also displays the real measured temperature. 

## Addtionnal features

- Using threads for blinking leds