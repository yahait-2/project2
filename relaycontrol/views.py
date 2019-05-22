from django.shortcuts import render 
from django.http import HttpResponse 
# GPIO port numbers 
import RPi.GPIO as GPIO
import Adafruit_HTU21D.HTU21D as HTU21D
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
sensor = HTU21D.HTU21D()



def relaycontroller(request): 
    if 'on' in request.POST: 
        GPIO.setup(20, GPIO.OUT)
        time.sleep(1)
        GPIO.output(21, 1)
        time.sleep(1)
        GPIO.output(21, 0)
        time.sleep(1)
        print('on')
        
    elif 'off' in request.POST: 
       GPIO.cleanup(20)
       print('off')
       

    elif 'temp' in request.POST:
        print ('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
        print ('Humidity  = {0:0.2f} %'.format(sensor.read_humidity()))
        print ('Dew Point = {0:0.2f} *C'.format(sensor.read_dewpoint()))
               
    return render(request,'control.html')
