from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
dict1={}

@app.route('/',methods=['GET'])
def root():
  return 'ok'
    
@app.route('/set',methods=['POST'])
def root1():
  key=request.form.get("key")#把在網頁中輸入的key存成變數'key'
  value=request.form.get("value")#把在網頁中輸入value的存成變數'value'
  check=key in dict1#如果key原本就存在於字典裡，check會==True
  if check==True:
    return "key exist"#key存在於字典裡就回傳"key exist"
  else:
    dict1[key] = value
    return "set success"#key沒有在字典裡就增加key&value到字典並回傳"key exist"

@app.route('/key_list',methods=['GET'])
def root2():
  return str(dict1)#把整個字典用字串形式回傳
  
@app.route('/get_value/<key>',methods=['GET'])
def root3(key):
  value=dict1.get(key)#取value值
  if value=="None":#如果key不存在Value==none
    return "key not found"
  else:
    return str(value)#回傳key的value

@app.route('/update_value',methods=['POST'])
def root4():
  key_u=request.form.get("key")#把在網頁中輸入的key存成變數'key_u'
  value_u=request.form.get("value")#把在網頁中輸入value的存成變數'value_u'
  check=key_u in dict1#如果key原本就存在於字典裡，check會==True
  if check==True:
    dict1[key_u] = value_u#更新key&value
    return "update success"
  else:
    return "key does not exist"
    
@app.route('/delete/<key>',methods=['GET'])
def root5(key):
  value_d=dict1.get(key)
  if value_d=="None":#如果key不存在Value==none
    return "key not found"
  else:
    del dict1[key]#刪除key&value
    return "delete success"
app.run(host="0.0.0.0", port=3000, debug=True)