def gcd(a, b):#建立函式
  m = max(a,b)
  n = min(a,b)#分出兩個數哪個大哪個小

  for i in range(1):
    while(n==0):#當兩數中有0時
      error="0沒有gcd"
      return error #回傳error並結束整個函式
    x = m % n
    while(x==m-n or n==1):#兩數互質時
      coprime =str(a)+"和"+str(b)+"互質"
      return coprime #回傳coprime並結束整個函式
    while(n!=0 and x!=0):#開始輾轉相除法
      m = n
      n = x
      x = m % n
  GCD = str(a)+"和"+str(b)+"的gcd="+str(n)  
  return GCD#回傳GCD並結束整個函式

ans1 = gcd(80, 20)
print(ans1) 
ans2 = gcd(10, 0)
print(ans2)
ans3 = gcd(19, 20)
print(ans3)
