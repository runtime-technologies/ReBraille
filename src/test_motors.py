import utils.gpio as GPIO

GPIO.initialize_gpio()
GPIO.test_all_pins(interval=0.2, iterations=10000)
