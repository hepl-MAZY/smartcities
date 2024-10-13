from machine import Pin, PWM, ADC, I2C
from ws2812 import WS2812
import utime
import random
import collections


#Colors 
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
LIME=(0,255,0)
YELLOW=(255,255,0)
PURPLE=(128,0,128)

COLORS=(RED,LIME,BLUE,YELLOW,PURPLE)

led=WS2812(18,1)

SOUND_SENSOR=ADC(0)
noise=0
selected_color=RED
peakCount=0
avg_bpm=0
bpm_list=[]

while True:
    temp_value=noise
    #from 0-255
    for i in range(5000):
        noise=noise+SOUND_SENSOR.read_u16()/256

    noise=noise/5000
    #print(noise)
    print(abs(noise-temp_value))
            
    if noise<25:
        led.pixels_fill(BLACK)
        led.pixels_show()
    elif noise>=25:
        selected_color=random.choice(COLORS)
        led.pixels_fill(selected_color)
        led.pixels_show()
        #Previous value-current value
        if (abs(noise-temp_value))>10:
            print("Peak count=",peakCount)
            if peakCount==0:
                print("start")
                start_time= utime.ticks_ms()
                peakCount=peakCount+1
            elif peakCount==1:
                print("end")
                elasped_time=utime.ticks_diff(utime.ticks_ms(),start_time)
                bpm=60000/elasped_time
                bpm_list.append(bpm)
                print("BPM = ",bpm)
                peakCount=0
        
    
    if len(bpm_list)==10:
        for i in range(10):
            avg_bpm=avg_bpm+bpm_list[i]
        
        avg_bpm=avg_bpm/10
        print("AVERAGE BPM=",avg_bpm)
        bpm_list.clear()
    
        
    
    
    

