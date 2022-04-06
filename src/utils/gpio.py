"""
Utility to control GPIO pins for the Nvidia Jetson Nano.
"""

from time import sleep

import Jetson.GPIO as GPIO

"""
Pin to Dot Map
1 -> 11     2 -> 15
3 -> 19     4 -> 23
5 -> 29     6 -> 31
7 -> 35     8 -> 40

Direction Pin Map
Low     -> Forward
High    -> Reverse
"""

BRAILLE_MATRIX_SIZE = 8

DIRECTION_PIN = 38
CONTROL_PINS = [11, 15, 19, 23, 29, 31, 35, 40]

PINS_HIGH = [GPIO.HIGH] * BRAILLE_MATRIX_SIZE
PINS_LOW = [GPIO.LOW] * BRAILLE_MATRIX_SIZE


def initialize_gpio():
    """
    Initialises the GPIO pins on the Jetson.
    """
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(DIRECTION_PIN, GPIO.OUT, initial=GPIO.LOW)

    for c in CONTROL_PINS:
        GPIO.setup(c, GPIO.OUT, initial=GPIO.LOW)

    mode = GPIO.getmode()


def sleep_state():
    """
    Sets the GPIO pins to the default off state.
    """
    GPIO.output(DIRECTION_PIN, GPIO.LOW)
    GPIO.output(CONTROL_PINS, PINS_LOW)


def reset_pins():
    """
    Resets all pins to the lowered state.
    """
    GPIO.output(DIRECTION_PIN, GPIO.HIGH)
    GPIO.output(CONTROL_PINS, PINS_LOW)


def set_pins(pin_configuration=PINS_LOW):
    """
    Sets the pins defined by the configuration.

    Args:
        pin_configuration (array of GPIO state, optional): Array of 8 GPIO states for each of the 8 pins. Defaults to PINS_LOW.
    """
    GPIO.output(DIRECTION_PIN, GPIO.LOW)
    GPIO.output(CONTROL_PINS, pin_configuration)


def test_all_pins(interval=1, iterations=10):
    """
    Sets and resets all pins for testing for the specified number
    of iterations with the specified interval.

    Args:
        interval (int, optional): Delay between each set and reset. Defaults to 1.
        iterations (int, optional): Number of times to set and reset the pins. Defaults to 10.
    """
    for i in range(iterations):
        set_pins(PINS_HIGH)
        sleep(interval)
        sleep_state()
        sleep(interval)
        reset_pins()
        sleep(interval)
        sleep_state()
        sleep(interval)


def display_character(braille_code='00000000'):
    """
    Converts braille code to GPIO configuration.

    Args:
        braille_code (string): 8 character string of 1s and 0s, Defaults to 00000000.
    """
    pin_configuration = [
        GPIO.HIGH if character is '1' else GPIO.LOW for character in braille_code]
    set_pins(pin_configuration)
