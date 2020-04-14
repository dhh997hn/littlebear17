import os
from obshi import encode,decode,get_opts

opts,args = get_opts()

#encode: get cipher_text from container after added blank space in the end of lines
if 'e' in opts.keys():
    file_o = args[1]
    with open(args[0],'r', encoding='UTF-8') as file_in, \
            open(file_o,'w', encoding='UTF-8') as file_out:
        hided_text = encode(opts['t'], bits_to_len=5)
        index = 0
        while index < len(hided_text):
            line = file_in.readline()
            if not line:
                raise IOError('Error!! Please try with longer file input!')
            if hided_text[index] == '1':
                file_out.write(line.replace('\n' ,'\t\n'))
            else:
                file_out.write(line)
            index += 1
        file_out.write(file_in.read())
    if len(args) == 1:
        os.rename(file_o, args[0])

#decode: get hided_text from cipher_text then decode
elif 'd' in opts.keys():
    with open(args[0],'r',encoding='UTF-8') as file_in:
        hided_text = ''.join(['1' if '\t\n' in line else '0' for line in file_in.readlines()])
        print(decode(hided_text, bits_to_len=5))

