from datetime import datetime, date, time

dt = date(2022, 2, 12)    # 時間，取自date()建構式
tm = time(14, 50)         # 日期，取自time()建構式
print(datetime.combine(dt, tm))

print(datetime.combine(dt, tm).strftime(
    '%Y-%m-%d %H:%M:%S'))

