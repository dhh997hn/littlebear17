import sys
import math
from getopt import GetoptError,getopt 

# ---------NOTE----------------
# input_text: text entered from the keyborad
# container: russian text from internet 
# cipher_text: text, which we have got after encode container
#-------------------------------------------------------------

#create array of russian alphabet (from a to я)
text = [chr(i) for i in range(ord('а'),ord('я')+1)]

#set length of every letter = 5
bits_per_lt = 5;

#convert letter to binary
def hide_letter(letter):
    index = text.index(letter)
    return bin(index)[2:].zfill(bits_per_lt)

def decode_fileo(sequence): 
    return text[int(sequence,2)]

#get options from command line 
def get_opts():
    opts = {'max-len': 8}
    options, args = getopt(sys.argv[1:], 't:ed')
    for key, value in options:
        opts[key.replace('-', '')] = value
    if 'e' in opts.keys() and 't' not in opts.keys():
        raise GetoptError('Error!! Please add -t in the righ of  -e!')
    return opts, args

#encode input_text to binary
def encode(text, bits_to_len=None):
    bits_to_len = 8 if bits_to_len is None else bits_to_len
    hided_text = ''
    lenghth = len(text) 
    for letter in text: 
        hided_text += hide_letter(letter)
    return bin(lenghth)[2:].zfill(bits_to_len) + hided_text

# decode:  get input_text after decode cipher_text 
def decode(text, bits_to_len=None):
    bits_to_len = 8 if bits_to_len is None else bits_to_len
    size = int(text[:bits_to_len], 2)
    text = text[bits_to_len:]
    decoded_text = ''
    for i in range(size):
        decoded_text += decode_fileo(text[i * bits_per_lt: (i+1)*bits_per_lt])
    return decoded_text
