import os#引進程式庫

path_1 = os.getcwd()#取得目前路徑
split_b = path_1.lstrip('/')#把開頭的/去掉
split_m = split_b.split('/')#把中間的/去掉
list_1 = list(split_m)#把目前的路徑轉成列表
print(list_1)

print(sep = ' ')#換行

path_2 = '/home/E94116130' #取得目前路徑
files = os.listdir(path_2)#從目標路徑取出資料
list_2 = list(files)#把目前的路徑轉成列表
print(list_2)

A=open('E94116130.txt','w')
for i in list_1:
    A.write(i+os.linesep)#寫入list_1裡的第i項

A.write(os.linesep)#換行

for i in list_2:
    A.write(i+os.linesep)#寫入list_2裡的第i項

A.close
