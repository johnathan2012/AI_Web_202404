from datetime import date, timedelta

tody = date.today() # 今天日期

# 到職日期
work = date(2004, 7, 12)
diff = tody - work

# 輸出工作天數
print(f'工作天數：{diff.days:,}天')
result = diff/timedelta(days = 365)
print(f'{result:.2f}年')
