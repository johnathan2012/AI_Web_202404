'''裝飾器 -- 定義 Decorator
    *args -- 收集位置參數，**kw -- 收集關鍵字引數
'''
import time, functools

def Records(some_func):    # 定義裝飾器，以函式為傳入值

   @functools.wraps(some_func)
   
   def inner(*args, **kw): # 回傳函式
      print(f'Hi! 呼叫了{some_func.__name__}()')   # 屬性__name__取得函式名稱
      return some_func(*args, **kw)

   return inner

@Records #裝飾器

def Atonce():
   #將取得時間做格式化動作
   return time.strftime('%Y-%b-%d %H:%M:%S',
      time.localtime())

#呼叫函式
print('登入時間:', Atonce())
