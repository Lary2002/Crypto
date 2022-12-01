#coding:utf8

def chiffreletter(let, cle):
    alphabet = []
    crypte = []
    liste = range(65, 91)
    for i in liste:
        alphabet.append(chr(i))

    i = alphabet.index(cle)
    while i<len(alphabet):
        crypte += alphabet[i] 
        i = i+1
        a=0
    
    j = alphabet.index(cle)
    while a<j:
        crypte+=alphabet[a]
        a = a +1
    
    indice = alphabet.index(let)
    ret = crypte[indice]
    return ret


msg = input('Tapez votre message: ')
msg = msg.upper()

pivaut = input('Entrez la clé: ')
pivaut = pivaut.upper()

longpivaut = pivaut
taille = len(msg) - len(pivaut)

alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i))

v = 0
while v < taille:
    longpivaut += pivaut 
    v += 1

liste = []
for l in longpivaut:
    liste += l
liste = liste[:len(msg)]

chiffemsg =[]
t=0
for letter in msg:
    if letter not in alphabet:
        chiffemsg += letter
        t-=1
        continue
    else:
        chiffemsg+= chiffreletter(letter, liste[t])
    t+=1
    
chiffemsg = ''.join(chiffemsg)
print('Le message chiffré est: {} '.format(chiffemsg))






    