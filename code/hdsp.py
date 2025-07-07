#HDSP Display Controller by Tyler Ramsawak


__version__ = "1.0.0"


import time

class HDSP_controller:
    char_set = {
    '<_full': [0, 0],
    '¿': [1, 0],
    'x_bar': [2, 0],
    'Ñ': [3, 0],
    'ñ': [4, 0],
    'alpha': [5, 0],
    'beta': [6, 0],
    'delta': [7, 0],
    '^': [8, 0],
    'eta': [9, 0],
    'theta': [10, 0],
    'lamda': [11, 0],
    'mu': [12, 0],
    'pi': [13, 0],
    'baby_sigma': [14, 0],
    'sigma': [15, 0],

    'tau': [0, 1],
    'phi': [1, 1],
    'omega': [2, 1],
    'Å': [3, 1],
    'å': [4, 1],
    'Ä': [5, 1],
    'ä': [6, 1],
    'Ö': [7, 1],
    'ö': [8, 1],
    'Ü': [9, 1],
    'ü': [10, 1],
    'arrow_r': [11, 1],
    'sqrt': [12, 1],
    'square': [13, 1],
    '£': [14, 1],
    '¥': [15, 1],

    ' ': [0, 2],
    '!': [1, 2],
    '"': [2, 2],
    '#': [3, 2],
    '$': [4, 2],
    '%': [5, 2],
    '&': [6, 2],
    "'": [7, 2],
    '(': [8, 2],
    ')': [9, 2],
    '*': [10, 2],
    '+': [11, 2],
    ',': [12, 2],
    '-': [13, 2],
    '.': [14, 2],
    '/': [15, 2],

    '0': [0, 3],
    '1': [1, 3],
    '2': [2, 3],
    '3': [3, 3],
    '4': [4, 3],
    '5': [5, 3],
    '6': [6, 3],
    '7': [7, 3],
    '8': [8, 3],
    '9': [9, 3],
    ':': [10, 3],
    ';': [11, 3],
    '<': [12, 3],
    '=': [13, 3],
    '>': [14, 3],
    '?': [15, 3],

    '@': [0, 4],
    'A': [1, 4],
    'B': [2, 4],
    'C': [3, 4],
    'D': [4, 4],
    'E': [5, 4],
    'F': [6, 4],
    'G': [7, 4],
    'H': [8, 4],
    'I': [9, 4],
    'J': [10, 4],
    'K': [11, 4],
    'L': [12, 4],
    'M': [13, 4],
    'N': [14, 4],
    'O': [15, 4],

    'P': [0, 5],
    'Q': [1, 5],
    'R': [2, 5],
    'S': [3, 5],
    'T': [4, 5],
    'U': [5, 5],
    'V': [6, 5],
    'W': [7, 5],
    'X': [8, 5],
    'Y': [9, 5],
    'Z': [10, 5],
    '[': [11, 5],
    '\\': [12, 5],
    ']': [13, 5],
    'arrow_up': [14, 5],
    '_': [15, 5],

    '`': [0, 6],
    'a': [1, 6],
    'b': [2, 6],
    'c': [3, 6],
    'd': [4, 6],
    'e': [5, 6],
    'f': [6, 6],
    'g': [7, 6],
    'h': [8, 6],
    'i': [9, 6],
    'j': [10, 6],
    'k': [11, 6],
    'l': [12, 6],
    'm': [13, 6],
    'n': [14, 6],
    'o': [15, 6],

    'p': [0, 7],
    'q': [1, 7],
    'r': [2, 7],
    's': [3, 7],
    't': [4, 7],
    'u': [5, 7],
    'v': [6, 7],
    'w': [7, 7],
    'x': [8, 7],
    'y': [9, 7],
    'z': [10, 7],
    '{': [11, 7],
    '|': [12, 7],
    '}': [13, 7],
    '~': [14, 7],
    'cursor': [15, 7]
    }

    def __init__(self, A0, A1, A2, A3, rst, wr, ce):
        self.A0 = A0
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.rst = rst
        self.wr = wr
        self.ce = ce
        
    #onvert to binary and pad to specified length
    def binary_pad(self, data, length):
        binary_data = bin(data)[2:]
        while len(binary_data) < length:
            binary_data = '0' + binary_data
        
        return binary_data
    
    #reverse string
    def reverse_str(self, string):
        return ''.join(reversed(string))

    #reset HDSP
    def reset(self):
        self.rst.low()
        time.sleep(1) #needs 3 clock cycles
        self.rst.high()
        time.sleep(1)

        #set Character RAM address
        self.A3.high()
        
        print('initialized display')
        
    #set position addresses
    def char_position(self, dig):
        bin_dig = self.binary_pad(dig, 3)
        bits = [int(b) for b in bin_dig]

        self.A0.value(bits[2])
        self.A1.value(bits[1])
        self.A2.value(bits[0])
        
        print('set position:' + bin_dig)
        
    #HDSP write cycle
    def write_cycle(self):
        self.ce.low()
        time.sleep_us(1)
        self.wr.low()
        time.sleep_us(1)
        self.wr.high() #data read from RAM on rising edge of WR pulse
        time.sleep_us(1)
        self.ce.high() #data transfered into position on rising edge of CE pulse
        time.sleep_us(1)
        
        print('writing')


    #get character from character map
    def get_char_code(self, char):
        bin_char_row = self.binary_pad(self.char_set[char][0], 4)
        rev_bin_char_row = self.reverse_str(bin_char_row)

        bin_char_col = self.binary_pad(self.char_set[char][1], 4)
        rev_bin_char_col = self.reverse_str(bin_char_col)        

        return int(rev_bin_char_row+rev_bin_char_col, 2)
        

