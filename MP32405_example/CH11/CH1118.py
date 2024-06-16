#含有引數的裝飾器 -- 定義 Decorator
import time, functools

def Records(name): # 定義裝飾器函式

   def Person(some_func):
      #@functools.wraps(some_func)

      def inner(*args, **kw):
         print(f'Hi! {name}, 呼叫了{some_func.__name__}()')
         return some_func(*args, **kw)

      return inner # 回傳函式
   return Person

@Records('Joson')   # 含有參數的裝飾器

def Atonce():
   #將取得時間做格式化動作
   return time.strftime('%Y-%b-%d %H:%M:%S',
        time.localtime())

#呼叫函式
print('登入時間:', Atonce())

