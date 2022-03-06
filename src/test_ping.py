import Jetson.GPIO as GPIO
import time

SLEEP_TIME = 2
GPIO.setmode(GPIO.BOARD)
channels = [11, 15, 23, 31, 29, 19]#, 32, 33, 35, 36, 37, 38, 40]

gpio_hl_list = [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH]
gpio_hl_list2 = [GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW]

for c in channels:
  GPIO.setup(c, GPIO.OUT, initial=GPIO.HIGH)

mode = GPIO.getmode()

for i in range(10):
  print(i)
  GPIO.output(channels, gpio_hl_list)
  time.sleep(SLEEP_TIME)
  GPIO.output(channels, gpio_hl_list2)
  time.sleep(SLEEP_TIME)

# for c in channels:
#   time.sleep(SLEEP_TIME)
#   GPIO.output(channels, [GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW])
#   time.sleep(SLEEP_TIME)
#   GPIO.output(channels, [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH])
    
