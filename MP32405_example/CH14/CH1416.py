#將Python dict 物件轉成 JSON 格式
import json #匯入json模組

data = dict(name = 'Tom',
      sex = 'Male', salary = 25000)
data_json = json.dumps(data)#轉成JSON格式
print('JSON:', data_json)

# loads()方法還原Python物件
data_p = json.loads(data_json)
print('dict:', data_p)
