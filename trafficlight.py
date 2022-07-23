import machine
import utime

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_yellow = machine.Pin(21, machine.Pin.OUT)

crazy_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
stop_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def red():
    led_red.value(1)
    led_green.value(0)
    led_yellow.value(0)
    
def yellow():
    led_red.value(0)
    led_green.value(0)
    led_yellow.value(1)

def green():
    led_red.value(0)
    led_green.value(1)
    led_yellow.value(0)

def all_on():
    led_red.value(1)
    led_green.value(1)
    led_yellow.value(1)    
    
def stop_all():
    led_red.value(0)
    led_green.value(0)
    led_yellow.value(0)

def regular_pattern():
    green()
    utime.sleep(2)
    yellow()
    utime.sleep(.5)
    red()
    utime.sleep(2)
    
def crazy_pattern():
    green()
    utime.sleep(.1)
    yellow()
    utime.sleep(.1)
    red()
    utime.sleep(.1)
    all_on()
    utime.sleep(.2)
    stop_all()
    utime.sleep(.2)
    red()
    utime.sleep(.1)    
    yellow()
    utime.sleep(.1)
    green()
    utime.sleep(.1)
    all_on()
    utime.sleep(.2)
    stop_all()
    utime.sleep(.2)
    

while True:        
    regular_pattern()
    
    while crazy_button.value() == 1:
        if stop_button.value() == 1:
            stop_all()
        crazy_pattern()
       

#stop_all()
