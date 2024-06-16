# 使用del運算子移除物件

class RemoveAt():   # 定義函式
   def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

   def __del__(self): # destructor - 用來清除物件
      number = self.__class__.__name__   # 取得類別的實體物件
      print('已清除', number)

one = RemoveAt(15, 20) # 產生物件
two = one # 兩個物件同時指向一個參照
print(f'one = {id(one)} \ntwo = {id(two)}')

del one; del two
