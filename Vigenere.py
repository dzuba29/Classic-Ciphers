alpha='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
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

print(dec_string)
print(cut_string(dec_string,key_word))

VIG_decode=vigenere(dec_string,cut_string(dec_string,key_word),alpha,1)
print(VIG_decode)
VIG_encode=vigenere(VIG_decode,cut_string(dec_string,key_word),alpha,-1)
print(VIG_encode)
