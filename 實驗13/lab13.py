import matplotlib.pyplot as plt
import numpy as np
import os
path = 'Temperature.txt'
f = open(path, 'r')
temp=[]
year=[]
month=list(range(1,13))

for i in f.readlines():
    if i == "Tainan:\n":
        continue
    a = list(map(float,i.rstrip("\n").split(",")))
    temp.append(a[1:])
    year.append(int(a[0]))

f.close() 

for j in range(9):
    plt.plot(month, temp[j], label=str(year[j]))
plt.title('Tainan Monthly Mean Temperature Form 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()
plt.show()

temp_m=[]

for l in range(12):
    total=0
    for k in range(len(temp)):
        total += temp[k][l]
    temp_m.append(round(total/len(temp),2))
print(temp_m)

avg=round(sum(temp_m)/12,2)
avg_list=[]
for m in range(12):
    avg_list.append(avg)

plt.plot(month, temp_m, '-o', markerfacecolor='red',markeredgecolor='red')
plt.plot(month, avg_list, color='red',linestyle='--',label='Mean of 9 years')
plt.text(x=1,y=avg,s=avg,va='bottom',fontsize=10)
for t in range(12):
    plt.text(x=month[t],y=temp_m[t],s=temp_m[t],va='bottom',fontsize=10)
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temoperature in Degree C')
plt.legend()
plt.show()

fig = plt.figure(figsize=(15,6))
plt.subplot(1,2,1)#圖像位置
plt.plot(month, temp_m, '-o', markerfacecolor='red',markeredgecolor='red')
plt.plot(month, avg_list, color='red',linestyle='--',label='Mean of 9 years')
plt.text(x=1,y=avg,s=avg,va='bottom',fontsize=10)
for t in range(12):
    plt.text(x=month[t],y=temp_m[t],s=temp_m[t],va='bottom',fontsize=10)
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temoperature in Degree C')
plt.subplot(1,2,2)#圖像位置
for j in range(9):
    plt.plot(month, temp[j], label=str(year[j]))
plt.title('Tainan Monthly Mean Temperature Form 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()
plt.show()
fig.suptitle('lab13_03',fontsize=16)
plt.tight_layout
plt.show()
fig.savefig('lab13_03.png')
