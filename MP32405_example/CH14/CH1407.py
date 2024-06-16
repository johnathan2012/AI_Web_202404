# 實作 with/as 的 __enter__()和__exit__()方法

class AutoClose:
   def __init__(self, msg):
      self.show = msg
      print('開啟' + msg)

   def __enter__(self):
      print('進入with區塊')
      return self.show

   def __exit__(self, type, value, tb):
      if type is None:
         print('檔案自動關閉')
      else:
         print('引發異常! ' + str(type))
      return False

with AutoClose('../Demo/demo1407.txt') as file:
    for line in file:
        print(line, end = '')

