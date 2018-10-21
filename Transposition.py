import itertools as it
import numpy as np

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
	key=list(key) #keyword as list
	sorted_brut = [item for item in key_variants if item not in key] #clean brute list
	comb_length=key.count('X') #count of empty symbols in keyword
	temp_list=[]
	tuples_list=list(it.combinations(sorted_brut, comb_length)) #all combs of keys (if all XXX)
	for i in range(len(tuples_list)):
		temp_list.append(replace_bruted_key(key,tuples_list[i])) 
	return temp_list
	
def decode(string,key,bruted_list):
	temp=[string[i:i+int(len(string)/len(key))] for i in range(0, len(string), int(len(string)/len(key)))]
	inds=[]
	print(temp)
	for i in range(len(temp)):
		inds.append(key.index(temp[i])+1)
	print(inds)


t=bruteforce(k,b)
decode(s,t[0],b)