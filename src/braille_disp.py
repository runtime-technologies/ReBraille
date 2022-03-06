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
channels = [31, 32, 33, 35, 36, 37, 38, 40]
GPIO.setup(channels, GPIO.OUT)
GPIO.output(channels, GPIO.LOW)

# ------------------------------------------------------------------------------
SLEEP_TIME_SEC = 2
# ------------------------------------------------------------------------------
braille_map = dict()

# letters and corresponding braille sequences
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.;!"
brailles = [ 0b100000,
             0b101000,
             0b110000,
             0b110100,
             0b100100,
             0b111000,
             0b111100,
             0b101100,
             0b011000,
             0b011100,
             0b100010,
             0b101010,
             0b110010,
             0b110110,
             0b100110,
             0b111010,
             0b111110,
             0b101110,
             0b011010,
             0b011110,
             0b100011,
             0b101011,
             0b011101,
             0b110011,
             0b110111,
             0b100111,
             0b000000,
             0b001000,
             0b001101,
             0b001010,
             0b001110]

for l, b in zip(letters, brailles):
    braille_map[l] = b

print(braille_map)
# ------------------------------------------------------------------------------
# test out for a sample string
sample = "Hello world"
sample = sample.upper()

sample_braille = [0 for c in sample]
for i, c in enumerate(sample):
    sample_braille[i] = braille_map[c]

braille_bin_list = ['{0:08b}'.format(n) for n in sample_braille]
print(sample_braille)
print(braille_bin_list)
# ------------------------------------------------------------------------------
def binlist_to_gpio(binlist):
    def __bin_to_gpioHL(bin_str):
       #return [GPIO.HIGH if ch is '1' else GPIO.LOW for ch in bin_str ] 
       return ['high' if ch == '1' else 'low' for ch in bin_str ] 
    gpio_list = [__bin_to_gpioHL(bin_str) for bin_str in binlist]
    return gpio_list
print(binlist_to_gpio(braille_bin_list))
# ------------------------------------------------------------------------------
# convert to list of GPIO.HIGH/GPIO.LOW
gpio_sequence = binlist_to_gpio(braille_bin_list)

for gpio_out in gpio_sequence:
    GPIO.output(channels, gpio_out)
    print(channels, gpio_out)
    sys.stdout.flush()
    time.sleep(SLEEP_TIME_SEC)
# ------------------------------------------------------------------------------
