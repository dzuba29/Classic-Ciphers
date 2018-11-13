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

def CheckTextBinary(string):
  if len(string)%60 == 0:
    return string
  else:
    string+=' '
    return CheckTextBinary(string)

def FillGrid(dec_msg,arr,indexes):
  for item in indexes:
    arr[item[0]][item[1]] = dec_msg.pop(0)
  return arr

def FillGridBinary(arr,indexes):
  for item in indexes:
    arr[item[0]][item[1]] = 1
  return arr

def GenerateGridIndexes(element,arr,ind_row_add,ind_col_add):
  i, j = np.where(arr == element)
  indexes = zip(i+ind_row_add,j+ind_col_add)
  return indexes

def CardanoGridExtract(arr,indexes):
  symbol_list=[]
  for item in indexes:
    symbol_list.append(arr[item[0]][item[1]])
  return symbol_list

def CardanoGridReshuffle(arr,indexes):
  symbol_list=[]
  symbol_list.append(''.join(CardanoGridExtract(arr,indexes)))
  arr = np.rot90(arr, 2)
  symbol_list.append(''.join(CardanoGridExtract(arr,indexes)))
  arr = np.fliplr(arr)
  symbol_list.append(''.join(CardanoGridExtract(arr,indexes)))
  arr = np.rot90(arr, 2)
  symbol_list.append(''.join(CardanoGridExtract(arr,indexes)))
  return ''.join(list(reversed(symbol_list)))

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

  main_arr = FillGrid(decode_msg,main_arr,sorted_grid)
  print(main_arr)

  main_arr = np.rot90(main_arr, 2)
  main_arr = FillGrid(decode_msg,main_arr,sorted_grid)
  # print(main_arr)
 
  main_arr = np.fliplr(main_arr)
  main_arr = FillGrid(decode_msg,main_arr,sorted_grid)
  # print(main_arr)

  main_arr = np.rot90(main_arr,2)
  main_arr = FillGrid(decode_msg,main_arr,sorted_grid)
  print(main_arr)

  return main_arr,sorted_grid
  
def grouper(string, n):
  args = [iter(string)]*n
  return zip(*args)


def main(divs,string):
  for item in divs:
    arr,grid=CardanoGridShuffle(string,item[0],item[1]) #code
    dec_string=CardanoGridReshuffle(arr,grid) #decode
    print(dec_string)
    if(dec_string==string):
      print("TRUE")

def Decode(main_arr,cut_string,sorted_grid):
  for i in range(len(cut_string)):
    temp=list(cut_string[i])
    main_arr = FillGrid(temp,main_arr,sorted_grid)
    
    main_arr = np.rot90(main_arr, 2)
    main_arr = FillGrid(temp,main_arr,sorted_grid)
    # print(main_arr)

    main_arr = np.fliplr(main_arr)
    main_arr = FillGrid(temp,main_arr,sorted_grid)
    # print(main_arr)

    main_arr = np.rot90(main_arr,2)
    main_arr = FillGrid(temp,main_arr,sorted_grid)
    print(main_arr)



def second_main(string,rows,columns):
  grid=[]

  arr1 = np.random.randint(4, size=(int(rows/2),int(columns/2)))

  main_arr = np.zeros((int(rows),int(columns))).astype('object')
  
  grid+=GenerateGridIndexes(0,arr1,0,0)
  grid+=GenerateGridIndexes(1,np.fliplr(arr1),0,int(columns/2))
  grid+=GenerateGridIndexes(2,np.flipud(arr1),int(rows/2),0)
  grid+=GenerateGridIndexes(3,np.flipud(np.fliplr(arr1)),int(rows/2),int(columns/2))

  main_arr = FillGridBinary(main_arr,grid)
  print(main_arr)

  sorted_grid = list(sorted(grid))

  # number_of_matrix=int(len(string)/(int(rows)*int(columns)))

  cut_string = [''.join(i) for i in grouper(string,int(rows)*int(columns))]
  print(cut_string)
  
  Decode(main_arr,cut_string,sorted_grid)

# string='ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИSSS'
# # string=CheckText(string)
# divs=FindAllPairDivisors(len(string))
# print(divs) #все возможные решетки
# main(divs,string)

string='ШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУЧАЕМШИФРАМАРШРУТНОЙПЕРЕСТАНОВКИШИФРРЕШЕТКАЯВЛЯЕТСЯЧАСТНЫМСЛУ'
print(len(string))
string=CheckTextBinary(string)
print(len(string))
second_main(string,6,10)
