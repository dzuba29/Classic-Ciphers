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

def FillGrid(dec_msg,arr,indexes):
  for item in indexes:
    arr[item[0]][item[1]] = dec_msg.pop(0)
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
  
string='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'

string=CheckText(string)
divs=FindAllPairDivisors(len(string))
print(divs) #все возможные решетки

for item in divs:
  arr,grid=CardanoGridShuffle(string,item[0],item[1]) #code
  dec_string=CardanoGridReshuffle(arr,grid) #decode
  print(dec_string)
  if(dec_string==string):
    print("TRUE")
