import random as r #匯入random模組並去小名為r
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}#製作骰子字典
list1=list(Times.keys())#把Times的keys存到list1裡以便用迴圈
for i in range(1000000):#重複1000000次
  x=r.randint(0, 5) #x=0~5之間取亂數
  Times[list1[x]] = Times[list1[x]] + 1/10000#把keys加0.0001%
for i in range(0,6):#輸出六次
  print ("The probability of "+list1[i]+" is "+str(round(Times[list1[i]],2))+"%" )
#取Times字典裡第i個key的value到小數點第二位