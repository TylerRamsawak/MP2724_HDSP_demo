from machine import Pin
from sr74hc595 import SR74HC595_BITBANG
from hdsp import HDSP_controller
import time
import utime

led = Pin(10, Pin.OUT)


#74HC595
ser = Pin(12, Pin.OUT)
rclk = Pin(13, Pin.OUT)
srclk = Pin(14, Pin.OUT)

sr = SR74HC595_BITBANG(ser, srclk, rclk)


#HDSP-2113
A0 = Pin(21, Pin.OUT)
A1 = Pin(20, Pin.OUT)
A2 = Pin(19, Pin.OUT)
A3 = Pin(18, Pin.OUT)
rst = Pin(17, Pin.OUT)
wr = Pin(15, Pin.OUT)
ce = Pin(11, Pin.OUT)

display = HDSP_controller(A0, A1, A2, A3, rst, wr, ce)

display.reset()

def update_display(time):
    char_codes = []
    for i, char in enumerate(time):
        char_code = display.get_char_code(char) #returns 18 since char='H'
        sr.bits(char_code, 8)
        sr.latch()
        position = 8-len(time)+i
        display.char_position(position)
        display.write_cycle()


hour = 14
minute = 16
second = 00

last_update = utime.time()

while True:
    current_time = utime.time()
    
    if current_time - last_update >= 1:
        elapsed = current_time - last_update
        last_update = current_time

        # Update seconds, minutes, and hours
        second += elapsed
        if second >= 60:
            minute += second // 60
            second = second % 60
        if minute >= 60:
            hour += minute // 60
            minute = minute % 60
        if hour >= 24:
            hour = hour % 24
            
        update_display(f'{hour}:{minute}:{second}')
    utime.sleep(0.1)

