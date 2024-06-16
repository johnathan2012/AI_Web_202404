#dump()須有參數fp
import json
from io import StringIO

data = {'C':'Three', 'B':'Two', 'D':'Four'}   # Dict物件

floi = StringIO()   # 寫入類檔案物件

json.dump(['A = One'], floi)
data_json = json.dump(data, floi, sort_keys = True)
print(floi.getvalue())#輸出內容
