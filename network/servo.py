from machine import Pin,PWM

#16 bit adc 0-65536

class SERVO:
    def _init_(self, pin):
        self.pin=pin
        self.pwm=PWM(self.pin)    
           
    def turn(self, val):
        self.pwm.freq(100)
        self.pwm.duty_u16(int(val/180*11000+4000))