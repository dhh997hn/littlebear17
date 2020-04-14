import os
from obshi import encode,decode,get_opts

opts, args = get_opts()

#encode: get cipher_text from container after added special symbols
if 'e' in opts.keys():
    file_o = args[1]
    with open(args[0],'r', encoding='UTF-8') as file_in, \
            open(file_o,'w',encoding='UTF-8') as file_out:
        hided_text = encode(opts['t'])
        index = 0
        letter = ''
        while index < len(hided_text):
            while letter not in [' ','\0']:
                file_out.write(letter)
                letter = file_in.read(1)
                if not letter and index < len(hided_text):
                    raise IOError('Error!! Please try with longer file input!')
            if hided_text[index] == '1':
                letter = chr(169) 
            else:
                letter = chr(999)
            file_out.write(letter)
            letter = file_in.read(1)
            index += 1
        file_out.write(file_in.read())
    if len(args) == 1:
        os.rename(file_o,args[0])
    
#decode: get hided_text from cipher_text then decode
elif 'd' in opts.keys():
    with open(args[0],'r',encoding='UTF-8') as file_in:
        text = {chr(999): '0', chr(169): '1'}
        hided_text=''.join([text[x] if x in text.keys() else '' for x in file_in.read()])
        print(decode(hided_text))
