from datetime import date, datetime

now = datetime.now() # 取得目前的日期和時間
print('目前', now)

special = now.year, now.month, now.day # 取得年、月、日屬性
print(f'日期 {special[0]}-{special[1]}-{special[2]}')

tm = now.hour, now.minute, now.second   # 取得時、分、秒屬性
print(f'時間 {tm[0]}:{tm[1]}:{tm[2]}')
