dict0 = {"index":['國文','英文','數學','自然','社會'],"StuA":['50','60','70','80','90'], "StuB":['57','86','73','82','43'] ,"StuC":['97','96','86','97','83']}#建立字典dict0

print(dict0)

i = 0 #宣告i=0(整數)
avgA = 0.0
avgB = 0.0
avgC = 0.0#宣告A、B、C為0.0(浮點數)
for i in range(0,5): #重複五次
  avgA = avgA + int(dict0["StuA"][i])/5 #將五分之一的各科分數輸入到avgA中
  avgB = avgB + int(dict0["StuB"][i])/5 #將五分之一的各科分數輸入到avgB中
  avgC = avgC + int(dict0["StuC"][i])/5 #將五分之一的各科分數輸入到avgC中
print("A學生平均成績:" + str(avgA))
print("B學生平均成績:" + str(avgB))
print("C學生平均成績:" + str(avgC))#輸出各學生平均成績

avg=[] #建立名為average的list
for i in range(0,5): #重複五次
  avg.append (str((int(dict0["StuA"][i]) + (int(dict0["StuB"][i])) +int(dict0["StuC"][i]))/3))#增加subject第i個科目的平均成績至average
  print(dict0["index"][i]+'平均成績是:' + avg[i])#輸出subject中第i個科目的平均成績
