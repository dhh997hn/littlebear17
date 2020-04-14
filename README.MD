Explain programme: 
My programme has 4 files:

obshi.py - where the functions used in each method are stored (encode text to binary, decode) 
zamena.py - Using method 1: change letters 'o' and 'p' in russian alphabet to 'o' and 'p' in english alphabet
probel.py - Using method 2: add tab,"\n" to the end of lines
simvol.py - Using method 3: change ' ' or '\0' to special symbols.


 ---------NOTE----------------
input.txt: russian text(container) from internet (i chose this text: рассказ Украденные мощи - Автор: Стас Сенькин)
oput1.txt, oput2.txt, oput2.txt: text, which we have got after encode container (with using method 1, method 2 and method 3)
------------------------------------------------------------------------------------------------------------------------------

How to run:

1. Open cmd or terminal
2. Type py *filename* -e -t "*russian text,which needed to encrypt*" input.txt output.txt  to endcode
(example: py zamena.py -e -t "прекрасно" input.txt oput1.txt )
3. Type py *filename* -d output.txt to decode
(examply: py zamena -d output.txt)
4. See result after encode container in files oput1.txt, oput2.txt and oput3.txt

*filename* includes: zamena.py, probel.py and simvol.py

**attention!! input text only includes russian alphabet ( from 'а,б,в,...' to 'я' ) 
