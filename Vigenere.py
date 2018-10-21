import random
from time import clock

alpha=u'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
dec_string='КОГДАТОЯБЫЛПАРНИШКОЙ'
key_word='ОСЕНЬ'

def get_index(string,symbol):
  for i in range(len(string)):
    if string[i]==symbol:
      return i

def cut_string(decode,key):
  if len(key)==len(decode):
    return key
  if len(key)>len(decode):
    key=key[:len(decode)]
    return cut_string(decode,key)
  if len(key)<len(decode):
    key=key+key
    return cut_string(decode,key)

def random_key(length,alph):
   return ''.join(random.choice(alph) for i in range(length))

def vigenere(code,key,alph,switch):
  vig =[]
  for i in range(len(code)):
    index_code=get_index(alph,code[i])
    index_key=get_index(alph,key[i])
    for i in range(len(alph)):
      if i == (index_code+index_key*switch)%len(alph):
        vig.append(alph[i])
  vig=''.join(vig)
  return vig

def vigenere_second(code,key,alph,switch):
  vig =[]
  for i in range(len(code)):
    index_code=get_index(alph,code[i])
    index_key=get_index(alph,key[i%len(key)])
    for i in range(len(alph)):
      if i == (index_code+index_key*switch)%len(alph):
        vig.append(alph[i])
  vig=''.join(vig)
  return vig

# print(dec_string)
# print(cut_string(dec_string,key_word))
# VIG_decode=vigenere(dec_string,cut_string(dec_string,key_word),alpha,1)
# print(VIG_decode)
# VIG_encode=vigenere(VIG_decode,cut_string(dec_string,key_word),alpha,-1)
# print(VIG_encode)

# print(dec_string)
# print(key_word)
# VIG_decode=vigenere_second(dec_string,key_word,alpha,1)
# print(VIG_decode)
# VIG_encode=vigenere_second(VIG_decode,key_word,alpha,-1)
# print(VIG_encode)


print("C дополнением и нарезкой ключа")
start_first=clock()
random_keyword=random_key(100000,alpha)
my_string=cut_string(dec_string,random_keyword)

VIG_decode=vigenere(dec_string,my_string,alpha,1)

VIG_encode=vigenere(VIG_decode,my_string,alpha,-1)

end_first=clock()
print(end_first-start_first)
print(dec_string)
print(my_string)
print(VIG_decode)
print(VIG_encode)


print("Без дополнения и нарезки ключа")
start_first=clock()

VIG_decode=vigenere_second(dec_string,key_word,alpha,1)

VIG_encode=vigenere_second(VIG_decode,key_word,alpha,-1)

end_first=clock()
print(end_first-start_first)
print(dec_string)
print(key_word)
print(VIG_decode)
print(VIG_encode)




