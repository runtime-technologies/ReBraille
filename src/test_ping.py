import Jetson.GPIO as GPIO
import time

SLEEP_TIME =2 #0.007
GPIO.setmode(GPIO.BOARD)
#channels = [11, 15, 23, 31, 29, 19]#, 32, 33, 35, 36, 37, 38, 40]
c_pin = 38
'''
11 -> 1
15 -> 2
19 -> 3
23 -> 4
29 -> 5
31 -> 6
35 -> 7
40 -> 8
'''
channels = [11, 15, 19, 23, 29, 31, 35, 40]

gpio_high_list = [GPIO.HIGH] * len(channels)
gpio_low_list = [GPIO.LOW] * len(channels)

# setup
GPIO.setup(c_pin, GPIO.OUT, initial=GPIO.LOW)
for c in channels:
  GPIO.setup(c, GPIO.OUT, initial=GPIO.HIGH)

mode = GPIO.getmode()

# functions for operation and reset
def off():
  '''
    [Default] motors don't move in this state
  '''
  GPIO.output(c_pin, GPIO.LOW)
  GPIO.output(channels, gpio_low_list)

def reset():
  '''
    Reset the motors to their OFF state
  '''
  GPIO.output(c_pin, GPIO.HIGH)
  GPIO.output(channels, gpio_low_list)

def op():
  '''
    Turn motors so they eventually end up pushing the braille pins to an ON
    state
  '''
  GPIO.output(c_pin, GPIO.LOW)
  GPIO.output(channels, gpio_high_list)

func_str_list = ['reset', 'off', 'op', 'off']
func_list = [reset, off, op, off]
#for i in range(10):
while True:
  for func, fstr in zip(func_list, func_str_list):
    print(fstr)
    func()
    time.sleep(SLEEP_TIME)
