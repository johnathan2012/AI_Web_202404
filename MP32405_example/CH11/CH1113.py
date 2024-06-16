def Entirely():  # 購物金額
   return 455.0

# 將金額打9折就是原有的函式Entirely()沒有改變，另行定義函式discount()
def discount(price):
   if price() >= 500.0:
      return lambda: price() * 0.9
   else:
      return lambda: price()

Entirely = discount(Entirely)
print('合計：', Entirely())
