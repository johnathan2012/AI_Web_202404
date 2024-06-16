price = 135884
rate = 0.08 #稅率
print('%4s:'%'定價', format(price, '>8d'))
tax = price * rate 
print('%4s:'%'稅率', format(tax, '011.2f'))

total = price + tax
print('含稅價：', format(total, '011.2f'))
