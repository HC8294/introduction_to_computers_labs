import requests
import pymysql
response = requests.get("https://www.chpb.gov.tw/opendata/2XvPDK8t9UC1v65F7FQ4Kw/json",verify =False)
num=[]
locat=[]
speed=[]
dirc=[]
data = response.json()

for i in data:
  num.append(i["編號"])
  locat.append(i["設備地點"])
  speed.append(i["速限"])
  dirc.append(i["方向"])

for j in range(74):
  connect_db = pymysql.connect(host = 'localhost', user = 'E94116130',  password = '0731hank', db ='wordpress')
  with connect_db.cursor() as cursor:
    cursor.execute('''insert into 彰化縣警察局固定桿式自動取締違規照相設置地點一覽表 values(%s,%s,%s,%s)''',(num[j],locat[j],speed[j],dirc[j]))
    connect_db.commit()
  connect_db.close()
  
  
