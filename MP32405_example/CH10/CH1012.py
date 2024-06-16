from datetime import datetime, timedelta

d1 = timedelta(days = 3, hours = 6)
d2 = timedelta(hours = 3.2)
dr = d1 + d2    #將兩個日期和時間相加
print(dr)
print(dr.days, '天')
print(f'9.2時 = {dr.seconds:,} 秒')   # 輸出33120秒
print(f'3天9.2時 = {dr.total_seconds():,}秒')
