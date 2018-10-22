import itertools as it
import numpy as np
import re

bigrams = ["ГЪ","КЩ","ЩФ","ЩЗ","ЭЩ","ЩК","ГЩ","ЩП","ЩТ","ЩШ","ЩГ","ЩМ","ФЩ","ЩЛ","ЩД","ДЩ","ЧЦ","ВЙ","ЙА","ШЯ","ШЫ","ГЮ","ХЯ","ЙЫ","ЦЯ","ГЬ","СЙ","ХЮ","ЪЖ","ЪД","УЬ","ЩЧ","ЧЙ","ШЙ","ШЗ","ЫФ","ЖЩ","ЖШ","ЖЦ","ЫЪ","ЫЭ","ЫЮ","ЫЬ","ЖЙ","ЫЫ","ЖЪ","ЖЫ","ЪШ","ПЙ","ЪЩ","ЗЩ","ЪЧ","ЪЦ","ЪУ","ЪФ","ЪХ","ЪЪ","ЪЫ","ЫО","ЖЯ","ЗЙ","ЪЬ","ЪЭ","ЫА","НЙ","ЕЬ","ЦЙ","ЬЙ","ЬЛ","ЬР","ПЪ","ЕЫ","ЕЪ","ЬА","ШЪ","ЪТ","ЩС","ОЬ","КЪ","ОЫ","ЩХ","ЩЩ","ЩЪ","ЩЦ","КЙ","ОЪ","ЦЩ","ЛЪ","МЙ","ШЩ","ЦЬ","ЦЪ","ЩЙ","ЙЬ","ЪГ","ИЪ","ЪБ","ЪВ","ЪИ","ЪЙ","ЪП","ЪР","ЪС","ЪО","ЪН","ЪК","ЪЛ","ЪМ","ИЫ","ИЬ","ЙУ","ЩЭ","ЙЫ","ЙЪ","ЩЫ","ЩЮ","ЩЯ","ЪА","МЪ","ЙЙ","ЙЖ","ЬУ","ГЙ","ЭЪ","УЪ","АЬ","ЧЪ","ХЙ","ТЙ","ЧЩ","РЪ","ЮЪ","ФЪ","УЫ","АЪ","ЮЬ","АЫ","ЮЫ","ЭЬ","ЭЫ","БЙ","ЯЬ","ЬЫ","ЬЬ","ЬЪ","ЯЪ","ЯЫ","ХЩ","ДЙ","ФЙ"]

b=['1','2','3','4','5','6','7','8','9']
s='БСЕАГНМЗЛАЕООЯНПЛТБНАЕЕСЬЬЕА'
k='2X41XX7'

t=[]

def fltr(bigs,string):
  count=0
  for bi in bigs:
    if bi in string:
      count=count+1
  if count==0: return True
  else: return False

def replace_bruted_key(key,tupl):
	temp=key.copy()
	if 'X' in temp:
		for item in tupl:
			temp[temp.index('X')]=item
		return temp
	else: 
		return key

def bruteforce(key,key_variants):
	temp_list=[]
	nums=re.findall("\d",key)
	key=list(key) #keyword as list

	if nums:
		key_variants=list(filter(lambda a: a <max(nums),key_variants))
		sorted_brut = [item for item in key_variants if item not in key] #clean brute list
	else:
		sorted_brut = [item for item in key_variants if item not in key] #clean brute list
	comb_length=key.count('X') #count of empty symbols in keyword
	if comb_length!=0:
		tuples_list=list(it.permutations(sorted_brut, comb_length)) #all combs of keys (if all XXX)
	else:
		tuples_list=key
	for i in range(len(tuples_list)):
		temp_list.append(replace_bruted_key(key,tuples_list[i])) 
	return temp_list
	
def decode(string,key):
	dic={};inds=[];ls=[]
	temp=[string[i:i+int(len(string)/len(key))] for i in range(0, len(string), int(len(string)/len(key)))]
	for i in range(len(temp)):
		inds.append(key.index(str(i+1)))
	dic=dict(zip(temp,inds))
	sorted_list = [k for k in sorted(dic, key=dic.get)]
	for string in sorted_list:
		ls.append(list(string))
	nparr=np.c_[ls].T
	dec_str=''.join([''.join(row) for row in nparr])
	return dec_str

t=bruteforce(k,b)
for i in range(len(t)):
	if fltr(bigrams,decode(s,t[i]))==True:
		print(decode(s,t[i]))