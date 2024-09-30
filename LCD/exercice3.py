from machine import Pin, PWM, ADC, I2C
import utime
from lcd1602 import LCD1602
from dht11 import *
import _thread



i2c=I2C(1,scl=Pin(7),sda=Pin(6),freq=400000)
d=LCD1602(i2c,2,16)
POTENTIO=ADC(0)
POTENTIO_VAL=0
BUZZER_PWM=PWM(Pin(20))
d.display()
setTemp=0
dht=DHT(18)
temp=0
led = Pin(16, Pin.OUT)
alarm_trig=0
warning_trig=0

def setTemperature():
    #1-65535 analog range
    #15-35 degres (20)
    temp=((35-15)/(65535-0)*(POTENTIO_VAL)+15)
    temp=round(temp,1)
    print("Set Temp : ",temp)
    return temp



# Function that will block the thread with a while loop
def led_thread():
    while True:
        if warning_trig==1:
            led.value(not led.value())
            utime.sleep(2)
        elif alarm_trig==1:
            for i in range(5):
                led.value(not led.value())
                utime.sleep_ms(100)
        elif alarm_trig==0 & warning_trig==0:
            led.value(0)
# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.
_thread.start_new_thread(led_thread, ())


while True:
    
    temp=dht.readTemperature()
    POTENTIO_VAL=POTENTIO.read_u16()
    print(POTENTIO_VAL)
    setTemp=setTemperature()
    #print("Temperature :",temp)
    #print("Set temp: ",setTemp)
    
    

    #Print default
    if alarm_trig==0:
        d.setCursor(0,0)
        d.print('Set: ')
        d.setCursor(len('Set:')+1,0)
        d.print("%.2f"%round(setTemp,2)+" °C")
            
        #Print real temp
        d.setCursor(0,1)
        d.print('Ambient: ')
            
        d.setCursor(len('Ambient:'),1)
        d.print("%.2f"%round(temp,2)+" °C")
    else:
        BUZZER_PWM.duty_u16(0)
    
    #Control 
    if temp<setTemp:
        warning_trig=0
        alarm_trig=0
    elif setTemp+3>temp>setTemp:
        alarm_trig=0
        warning_trig=1
    elif temp>setTemp+3:
        BUZZER_PWM.duty_u16(500)
        BUZZER_PWM.freq(1191)
        d.clear()
        d.setCursor(2,0)
        d.print('ALARM')
        alarm_trig=1
        warning_trig=0
    
    utime.sleep_ms(200)
    
    

