from machine import Pin
import utime
import random
from servo import SERVO
import network
import ntptime
import time


servo=SERVO()
servo._init_(Pin(20))
connected=0
_hour=0
_angle=0
i=0
hour_list=[0,6,12,18,24]

def setHour(hour):
  if 12<hour<24:
    hour=hour-12
    
  
  return hour

def setAngle(hour):
  if 0<hour<12:
    angle=(hour*90)/6
  elif hour==12:
    angle=0
  elif hour==24 or hour==0:
    angle=180
  
  return angle
  
while True:
  
  
  #Connecting to the internet
  while connected!=1:
    print('Connecting to WiFi Network Name:', "")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    utime.sleep(3) # wait three seconds for the chip to power up and initialize
    wlan.connect('NETGEAR95', '')
    print('Waiting for access point to log us in.')
    utime.sleep(2)
    if wlan.isconnected():
      print('Success! We have connected to your access point!')
      print('Try to ping the device at', wlan.ifconfig()[0])
      connected=1
    else:
      print('Failure! We have not connected to your access point!  Check your secrets.py file for errors.')
  
  
  ntptime.host="1.be.pool.ntp.org"
  try:
    print("Local time before synchronization：%s" %str(time.localtime()))
    #make sure to have internet connection
    ntptime.settime()
    print("Local time after synchronization：%s" %str(time.localtime()))
    _hour=time.localtime()[3]+2
    print("HOUR : ",_hour)
  except:
    print("Error synchronizing")
    
  utime.sleep(1)
 
  
  #_hour=setHour(hour_list[i])
  _angle=setAngle(_hour)
  print("Real hour:",hour_list[i])
  print("Hour",_hour)
  print("Angle : ",_angle)
  
  
  servo.turn(_angle)
  utime.sleep(1)
  
  """
  i+=1
  if i==4:
    i=0
  """
  
  
  
      
        
        
        
