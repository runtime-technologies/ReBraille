# ------------------------------------------------------------------------------
'''
    Mapping from english alphabet to Braille.
'''
# ------------------------------------------------------------------------------
import sys
import time
import Jetson.GPIO as GPIO
# ------------------------------------------------------------------------------
# setup GPIO pins on Jetson
GPIO.setmode(GPIO.BOARD)
#channels = [21, 22, 23, 24, 26, 29, 31, 32]
#channels = [31, 32, 33, 35, 36, 37, 38, 40]
channels = [11, 15, 19, 23, 29, 31, 35, 40]
GPIO.setup(channels, GPIO.OUT, initial=GPIO.LOW)
#GPIO.output(channels, GPIO.LOW)

# ------------------------------------------------------------------------------
SLEEP_TIME_SEC = 1
# ------------------------------------------------------------------------------
braille_map = dict()

# letters and corresponding braille sequences
letters = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.;:!()+&_"'?"""
small_brailles = [ 0b10000000, 0b10100000, 0b11000000, 0b11010000, 0b10010000,
                   0b11100000, 0b11110000, 0b10110000, 0b01100000, 0b01110000,
                   0b10001000, 0b10101000, 0b11001000, 0b11011000, 0b10011000,
                   0b11101000, 0b11111000, 0b10111000, 0b01101000, 0b01111000,
                   0b10001100, 0b10101100, 0b01110100, 0b11001100, 0b11011100,
                   0b10011100 ]
cap_brailles = [(i + 2) for i in small_brailles]
num_brailles = [0b01001100, 0b10000100, 0b10100100, 0b11000100,
                0b11010100, 0b10010100, 0b11100100, 0b11110100,
                0b10110100, 0b01100100 ]
punct_brailles = [ 0b00000000, 0b00100000, 0b00110100, 0b00101000, 0b00110000,
                   0b00111000, 0b00111100, 0b01010010, 0b00110010, 0b11101100,
                   0b00100001, 0b00011100, 0b00001000, 0b00101100 ]
brailles = [*small_brailles, *cap_brailles, *num_brailles, *punct_brailles]

braille_map = {l: b for (l, b) in zip(letters, brailles)}

print(braille_map)
# ------------------------------------------------------------------------------
# test out for a sample string
sample = "Hello world! This is RunTime, over."
#sample = sample.upper()

sample_braille = [0 for c in sample]
for i, c in enumerate(sample):
    sample_braille[i] = braille_map[c]

braille_bin_list = ['{0:08b}'.format(n) for n in sample_braille]
print(sample_braille)
print(braille_bin_list)
# ------------------------------------------------------------------------------
def binlist_to_gpio(binlist):
    def __bin_to_gpioHL(bin_str):
       return [GPIO.LOW if ch is '1' else GPIO.HIGH for ch in bin_str ] 
       #return ['high' if ch == '1' else 'low' for ch in bin_str ] 
    gpio_list = [__bin_to_gpioHL(bin_str) for bin_str in binlist]
    return gpio_list
print(binlist_to_gpio(braille_bin_list))
# ------------------------------------------------------------------------------
# convert to list of GPIO.HIGH/GPIO.LOW
gpio_sequence = binlist_to_gpio(braille_bin_list)

for gpio_out in gpio_sequence:
    GPIO.output(channels, gpio_out)
    print(gpio_out)
    sys.stdout.flush()
    time.sleep(SLEEP_TIME_SEC)
# ------------------------------------------------------------------------------
