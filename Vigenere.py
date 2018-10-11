alph='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
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



def vigenere(decode,key,alph):
  
  vig=[]
  for symbol in decode:
    index_sym=get_index(alph,symbol)
    for item in key:
      index_item=get_index(alph,item)
      total_index=index_sym-index_item
    vig.append(alph[total_index])
  print(vig)

      

print(dec_string)
print(cut_string(dec_string,key_word))

vigenere(dec_string,cut_string(dec_string,key_word),alph)
