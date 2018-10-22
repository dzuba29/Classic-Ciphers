import itertools as it
import numpy as np
import re

b=['1','2','3','4','5','6','7','8','9']
s='БСЕАГНМЗЛАЕООЯНПЛТБНАЕЕСЬЬЕА'
k='2X41XX7'
t=[]

def replace_bruted_key(key,tupl):
	temp=key.copy()
	for item in tupl:
		temp[temp.index('X')]=item
	return temp

def bruteforce(key,key_variants):
	temp_list=[]
	key=list(key) #keyword as list
	sorted_brut = [item for item in key_variants if item not in key] #clean brute list
	print(sorted_brut)
	comb_length=key.count('X') #count of empty symbols in keyword
	tuples_list=list(it.permutations(sorted_brut, comb_length)) #all combs of keys (if all XXX)
	print(tuples_list)
	for i in range(len(tuples_list)):
		temp_list.append(replace_bruted_key(key,tuples_list[i])) 
	return temp_list
	
def decode(string,key):
	dic={}
	temp=[string[i:i+int(len(string)/len(key))] for i in range(0, len(string), int(len(string)/len(key)))]
	inds=[]
	for i in range(len(temp)):
		inds.append(key.index(str(i+1)))
	dic=dict(zip(temp,inds))
	sorted_list = [k for k in sorted(dic, key=dic.get)]
	ls=[]
	for string in sorted_list:
		ls.append(list(string))
	nparr=np.c_[ls]
	return nparr.T


nums=re.findall("\d",k)

yolo=list(filter(lambda a: a <max(nums), b))

# temp_list=[]
# key=list(k) 
# sorted_brut = [item for item in yolo if item not in key] 
# print(sorted_brut)
# comb_length=key.count('X')
# tuples_list=list(it.permutations(sorted_brut, comb_length)) #trouble there
# print(tuples_list)

t=bruteforce(k,yolo)
print(t)
for i in range(len(t)):
	print(decode(s,t[i]))