K=[]#建立儲存keys的list
V=[]#建立儲存values的list
dict0={}#建立一個空的字典
for i in range(0,4):#重複四次
  K.append(input("Enter keys:"))#把這次輸入的key加進"K"list
  v=input("Enter values:")#先把輸入的value當成字串
  V.append(v.split())#把字串分割並加進"V"list
  dict0[str(K[i])] = V[i]#將這次的key&value加入dict0
print(dict0)#輸出dict0