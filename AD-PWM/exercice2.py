"""Buzzer volume controlled by potentiometer

    Buzzer : musical sound
    
    LOGIC : read analog value from potentio meter (ADC 0) then setting buzzer volume
    0-65535
    Frequency note value : https://www.reddit.com/r/shenzhenIO/comments/57nzgs/table_of_buzzer_frequencies/
    
"""
from machine import Pin, PWM, ADC
import utime


#VARIABLES

POTENTIO=ADC(0)
POTENTIO_VAL=0
BUZZER_PWM=PWM(Pin(20))
led = Pin(16, Pin.OUT)
button= Pin(18,Pin.IN,Pin.PULL_UP)
interrupt_flag=0

silence=32767 #Setting frequency very high (no sound)

def callback(button):
    global interrupt_flag
    interrupt_flag=1
    
button.irq(trigger=Pin.IRQ_FALLING, handler=callback)


#MINUET IN G BACH => 2 bars per line in array
notes=[1191,787,881,980,1050,1191,787,silence,787,
       1335,1050,1191,1335,1519,1573,787,silence,787,
       1060,1191,1060,980,881,980,1050,980,881,787,
       734,787,881,980,787,980,881,silence]
duration=[0.50,0.25,0.25,0.25,0.25,0.50,0.40,0.05,0.40,
          0.5,0.25,0.25,0.25,0.25,0.50,0.40,0.05,0.40,
          0.5,0.25,0.25,0.25,0.25,0.5,0.25,0.25,0.25,0.25,
          0.5,0.25,0.25,0.25,0.25,0.5,1,0.05]

#AN OCTAVE HIGHER 
notes_octave_higher=[]
for i in notes:
    notes_octave_higher.append(i*2)

selected_array=notes
switch_value=0

while True:
    index=0
    for n in selected_array:
        if interrupt_flag is 1:
            interrupt_flag=0
            print('An interrupt has occurred')
            if switch_value == 0:
                selected_array=notes_octave_higher
                switch_value+=1
            elif switch_value==1:
                selected_array=notes
                switch_value-=1
            index=0
            break
        else:
            led.value(not led.value())
            POTENTIO_VAL=POTENTIO.read_u16()
            print(POTENTIO_VAL)
            BUZZER_PWM.duty_u16(POTENTIO_VAL)
            BUZZER_PWM.freq(n)
            utime.sleep(duration[index])
            led_value=1
            index+=1
    


