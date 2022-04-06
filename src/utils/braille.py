"""
Utility to convert characters to their Braille code representation.
"""

CHARACTERS = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.;:!()+&_"'?-"""

LOWERCASE_ALPHA_CODES = [
    0b10000000, 0b10100000, 0b11000000, 0b11010000, 0b10010000,
    0b11100000, 0b11110000, 0b10110000, 0b01100000, 0b01110000,
    0b10001000, 0b10101000, 0b11001000, 0b11011000, 0b10011000,
    0b11101000, 0b11111000, 0b10111000, 0b01101000, 0b01111000,
    0b10001100, 0b10101100, 0b01110100, 0b11001100, 0b11011100,
    0b10011100
]

UPPERCASE_ALPHA_CODES = [(i + 2) for i in LOWERCASE_ALPHA_CODES]

NUMBER_CODES = [
    0b01001100, 0b10000100, 0b10100100, 0b11000100, 0b11010100,
    0b10010100, 0b11100100, 0b11110100, 0b10110100, 0b01100100
]

PUNCTUATION_CODES = [
    0b00000000, 0b00100000, 0b00110100, 0b00101000, 0b00110000,
    0b00111000, 0b00111100, 0b01010010, 0b00110010, 0b11101100,
    0b00100001, 0b00011100, 0b00001000, 0b00101100, 0b00001100
]

BRAILLE_CODES = LOWERCASE_ALPHA_CODES + \
    UPPERCASE_ALPHA_CODES + NUMBER_CODES + PUNCTUATION_CODES

BRAILLE_MAP = {character: braille_code for (
    character, braille_code) in zip(CHARACTERS, BRAILLE_CODES)}


def convert_string_to_braille(string):
    """
    Converts a character string to its Braille representation.

    Args:
        string (string): A string of characters to convert.

    Returns:
        list: List of {0, 1} Braille codes for the input string.
    """
    braille_string = []

    for character in string:
        # Ignore the character if not in predefined list.
        if character not in CHARACTERS:
            continue

        # Converts number representation to {0, 1} string before storing.
        braille_string.append('{0:08b}'.format(BRAILLE_MAP[character]))

    return braille_string
