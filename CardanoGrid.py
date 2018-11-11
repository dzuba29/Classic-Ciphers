import math
import numpy as np

def FindAllPairDivisors(value):
  res=[]
  for x in range(1, int(math.sqrt(value)+1)):
    if (value % x == 0 and (value//x)%2 == 0 and x%2 == 0):
      res.append([x,value//x])
  return res

def CheckText(string):   
  if len(string)%4 == 0:
    return string
  else:
    string+=' '
    return CheckText(string)

def Decode(dec_msg,arr,indexes):
  for item in indexes:
    arr[item[0]][item[1]] = dec_msg.pop(0)
  return arr

def GenerateGridIndexes(element,arr,ind_row_add,ind_col_add):
  i, j = np.where(arr == element)
  indexes = zip(i+ind_row_add,j+ind_col_add)
  return indexes

def CardanoGridShuffle(string,rows,columns):
  decode_msg=list(string)
  grid=[]

  arr1 = np.random.randint(4, size=(int(rows/2),int(columns/2)))

  grid+=GenerateGridIndexes(0,arr1,0,0)
  grid+=GenerateGridIndexes(1,np.fliplr(arr1),0,int(columns/2))
  grid+=GenerateGridIndexes(2,np.flipud(arr1),int(rows/2),0)
  grid+=GenerateGridIndexes(3,np.flipud(np.fliplr(arr1)),int(rows/2),int(columns/2))

  main_arr = np.zeros((rows,columns)).astype('object')
  sorted_grid = list(sorted(grid))

  main_arr = Decode(decode_msg,main_arr,sorted_grid)
  print(main_arr)

  main_arr = np.rot90(main_arr, 2)
  main_arr = Decode(decode_msg,main_arr,sorted_grid)
  # print(main_arr)
 
  main_arr = np.fliplr(main_arr)
  main_arr = Decode(decode_msg,main_arr,sorted_grid)
  # print(main_arr)

  main_arr = np.rot90(main_arr,2)
  main_arr = Decode(decode_msg,main_arr,sorted_grid)
  print(main_arr)
  
  return main_arr
  
string='ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИ'

string=CheckText(string)
divs=FindAllPairDivisors(len(string))

CardanoGridShuffle(string,divs[1][0],divs[1][1])
