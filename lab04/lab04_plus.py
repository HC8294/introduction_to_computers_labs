A = []
B = []
C = [] #建立三個學生的list

print("開始輸入A學生的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(0, 5):#重複步驟五次
  SCORE = input()#將輸入的值儲存至SCORE
  score = int(SCORE)#把str強制轉型成int
  while (score < 0 or score > 100):#當分數超出範圍時
    print("輸入0~100的數值!還想騙阿!")
    SCORE = input()#再輸入一次並將輸入的值儲存至SCORE
    score = int(SCORE)#把str強制轉型成int
  A.append(score)#把這次的score儲存到A列表
print("A學生的成績:")
print("國文:" + str(A[0]) + "、英文:" + str(A[1]) + "、數學:" + str(A[2]) + "、自然:" + str(A[3]) + "、社會" + str(A[4]))#輸出A學生各科成績
print(" ") #空一行

print("開始輸入B學生的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(0, 5):
  SCORE = input()
  score = int(SCORE)
  while (score < 0 or score > 100):
    print("輸入0~100的數值!還想騙阿!")
    SCORE = input()
    score = int(SCORE)
  B.append(score)
print("B學生的成績:")
print("國文:" + str(B[0]) + "、英文:" + str(B[1]) + "、數學:" + str(B[2]) + "、自然:" + str(B[3]) + "、社會" + str(B[4]))
print("") #以上同A

print("開始輸入C學生的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(0, 5):
  SCORE = input()
  score = int(SCORE)
  while (score < 0 or score > 100):
    print("輸入0~100的數值!還想騙阿!")
    SCORE = input()
    score = int(SCORE)
  C.append(score)
print("C學生的成績:")
print("國文:" + str(C[0]) + "、英文:" + str(C[1]) + "、數學:" + str(C[2]) + "、自然:" + str(C[3]) + "、社會" + str(C[4]))
print(" ") #以上同A

i = 0 #宣告i=0(整數)
averageA = 0.0
averageB = 0.0
averageC = 0.0#宣告A、B、C為0.0(浮點數)
while i < 5: #重複五次此步驟
  averageA = averageA + A[i]/5 #將五分之一的各科分數輸入到averageA中
  averageB = averageB + B[i]/5 #將五分之一的各科分數輸入到averageB中
  averageC = averageC + C[i]/5 #將五分之一的各科分數輸入到averageC中
  
  i += 1

print("A學生平均成績:" + str(averageA))
print("B學生平均成績:" + str(averageB))
print("C學生平均成績:" + str(averageC)) #輸出各學生平均成績
print(" ")  #空一行

average=[] #建立名為average的list
subject=['國文','英文','數學','自然','社會'] #建立有各個科目的list
for i in range(0,5): #重複五次
  average.append (str((int(A[i]) + int(B[i]) +int(C[i]))/3))#增加subject第i個科目的平均成績至average
  print(subject[i]+'平均成績是:' + average[i])#輸出subject中第i個科目的平均成績A = []

