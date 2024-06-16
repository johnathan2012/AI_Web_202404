# 將金額打9折處理的第二種方式 - 使用裝飾器

def discount(price):   # 定義裝飾器函式
   if price() >= 500.0:
      return lambda: price() * 0.9
   else:
      return lambda: price()

@discount   # 裝飾器

def Entirely():   # 購物金額
    return 455.0

print('合計：', Entirely())
