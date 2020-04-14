import os
from obshi import encode, decode, get_opts

opts,args = get_opts()

#encode: get cipher_text from container after changed russian letters to english letters
if 'e' in opts.keys():
    file_o = args[1] 
    with open(args[0], 'r', encoding='UTF-8') as file_in,\
            open(file_o,'w',encoding='UTF-8') as file_out:
        hided_text = encode(opts['t'])
        index = 0
        letter = ''
        replace = {'о': 'o', 'р': 'p'} #change russian letters to english letters
        while index < len(hided_text):
            while letter not in ['о','р']:
                file_out.write(letter)
                letter = file_in.read(1)
                if not letter and index < len(hided_text):
                    raise IOError('Error!! Please try with longer file input!')
            if hided_text[index] == '1':
                letter = replace[letter]
            file_out.write(letter)
            letter = file_in.read(1)
            index += 1  
        file_out.write(file_in.read())

#get hided_text from cipher_text and then decode
elif 'd' in opts.keys():
    with open(args[0],'r',encoding='UTF-8') as file_in:
        text = {
            'о': '0', 'р': '0', #rus
            'o': '1', 'p': '1', #eng
        }
        hided_text =''.join([text[x] if x in text.keys() else '' for x in file_in.read()])
        print(decode(hided_text))


