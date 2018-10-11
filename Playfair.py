import numpy as np

key_word='КАТЕР'
alph_rus='АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ' #del Й Ё Ъ
decode_string_rus='ЗЛНЖКГСЩЯЪАОЕСМЩЯСОЛКДБОУЩФРКЖФТАРТЮВИОАСЫЫРМРЕПМЩ' #вариант 9 replace Ъ Й
encode_string_rus='КОДПЛЕЙФЕЙЕРАОСНОВАННАИСПОЛЬЗОВАНИИМАТРИЦЫБУКВ'

def check_on_repeat(string,word):
  temp=''
  for i in range(len(string)-1):
    if string[i]==string[i+1]:
      temp=string[:i]+string[i]+word+string[i+1:]
    else: 
      continue;
  if len(temp)%2!=0:
    temp+=word
  if temp=='': return string
  else: return temp

def key_matrix(key,alph):
  temp = list(dict.fromkeys(key+alph))
  array=np.array(temp).reshape(5,6)
  return array

def decode_encode(decode_string,matrix,switch): # if switch = 1 - encode else decode
  temp=[decode_string[i:i+2].replace('Ъ','Ь').replace('Й','И').replace('Ё','Е') for i in range(0, len(decode_string), 2)]
  answer=''
  for element in temp:
    first_index=np.where(matrix == element[0])
    second_index=np.where(matrix == element[1])
    i,j=first_index[0][0],first_index[1][0]
    n,m=second_index[0][0],second_index[1][0]
    if (i==n):
      answer+=matrix[i][(j+switch)%np.shape(matrix)[1]]+matrix[n][(m+switch)%np.shape(matrix)[1]]
    elif (j==m):
      answer+=matrix[(i+switch)%np.shape(matrix)[0]][j]+matrix[(n+switch)%np.shape(matrix)[0]][m]
    else:
      answer+=matrix[i][m]+matrix[n][j]
  return answer
        
key_array=key_matrix(key_word,alph_rus)
print(key_array)
string=check_on_repeat(decode_string_rus,'З')
print(decode_encode(string,key_array,-1))
