import numpy as np

key_word='СВЯЗЬ'
alph_rus='АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ' #del Й Ё Ъ
decode_string_rus='ЛМЧШЮГХТЯПХООПКПЖМКЧВЦАОБФЖГКХПНЯВЖФЪЛЯНХОФЗТЪСЦПИЛФЛЪШШ' #вариант 9 replace Ъ Й
encode_string_rus='КОДПЛЕЙФЕЙЕРАОСНОВАННАИСПОЛЬЗОВАНИИМАТРИЦЫБУКВ'

print(len(encode_string_rus))
def key_matrix(key,alph):
  temp = list(key)
  for char in alph:
    if (key.find(char) == -1):
      temp += char;
  array=np.array(temp).reshape(5,6)
  return array

def decode_encode(decode_string,matrix,switch):
  temp=[decode_string[i:i+2].replace('Ъ','Ь').replace('Й','И').replace('Ё','Е') for i in range(0, len(decode_string), 2)]
  answer=''
  for element in temp:
    first_index=np.where(matrix == element[0])
    second_index=np.where(matrix == element[1])
    i,j=first_index[0][0],first_index[1][0]
    n,m=second_index[0][0],second_index[1][0]
    if (i==n):
      answer+=matrix[i][(j+switch)%6]+matrix[n][(m+switch)%6]
    elif (j==m):
      answer+=matrix[(i+switch)%5][j]+matrix[(n+switch)%5][m]
    else:
      answer+=matrix[i][m]+matrix[n][j]
  return answer
        
key_array=key_matrix(key_word,alph_rus)
enc=decode_encode(decode_string_rus,key_array,-1)
dec=decode_encode(encode_string_rus,key_array,1)