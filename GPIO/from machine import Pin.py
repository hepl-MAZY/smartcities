from machine import Pin
from time import sleep
import utime


#VARIABLES
led = Pin(16, Pin.OUT)
button= Pin(18,Pin.IN)
print('Running basic functions')


# %% ex1

while True:
  led.value(not led.value())
  sleep(0.5)



# %% ex2
"""
for i in range(10):
  led.value(not led.value())
  sleep(1)
  sleep_us // for microseconds
"""

# %% ex3 if else statement
"""
while True:
  val=button.value()
  if val == 1:
    led.value(1)
  else:
    led.value(0)
"""


"""
#%% ex4 ifelse elseif statement with button
val=0
while True:
  if button.value()==1:
    val += 1
  elif val == 2:
    val=0
  led.value(val)
"""