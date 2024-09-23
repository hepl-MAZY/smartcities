"""Led blinking at different speed (depending on how many time the button was pressed)
    
    Button pressed :
    ONCE : led blinking forever at 0.5Hz (2s)
    TWICE : faster than 0.5hz -> 1hz (1s)
    THREE : led turns off 
"""
from machine import Pin
import utime


interrupt_flag=0
led = Pin(16, Pin.OUT)
button= Pin(18,Pin.IN,Pin.PULL_UP)

def callback(button):
    global interrupt_flag
    interrupt_flag=1
    
button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

val_button=0 #BY default led is OFF
transition=0
led_value=0
led.value(0)
blinking_time=0
print('Blinking LED program\n')
print('Button pressed : \n',val_button)

while True:
    print('Button pressed : \n',val_button)
    if interrupt_flag is 1:
        for i in range(5):
                led.value(not led.value())
                utime.sleep_ms(100)
        print('Interrupt has occured')
        interrupt_flag=0
        val_button+=1
        print('Button incremented',val_button)
        if val_button==0:
            led_value=0
        elif val_button == 1:
            led_value=1
            blinking_time=2
        elif val_button == 2:
            led_value=1
            blinking_time=1
        elif val_button>2:
            led_value=0
            val_button=0
    else:
        if led_value==0:
            led.value(0)
        else:
            led.value(not led.value())
            utime.sleep(blinking_time)
    utime.sleep_ms(500)

    