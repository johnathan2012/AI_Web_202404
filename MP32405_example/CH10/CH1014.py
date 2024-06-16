from datetime import datetime, timedelta

#建立儲存星期的list物件
weeklst = ['Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday', 'Sunday']

def getWeeks(wkName, beginDay = None):
    # 如果未傳入beginDay之日期，就以今天為主
    if beginDay is None:
        beginDay = datetime.today()

    # weekday()方法回傳取得星期的索引值，Monday索引值為0
    indexNum = beginDay.weekday()
    target = weeklst.index(wkName)
    lastWeek = ( 7 + indexNum - target) % 7

    if lastWeek == 0:
        lastWeek = 7

    # timedelta()建構式取得天數
    lastWeek_Day = beginDay - timedelta(days = lastWeek)
    return lastWeek_Day.strftime('%Y-%m-%d')

# 只傳入一個參數
print('今天的上週二：', getWeeks('Tuesday'))

# 傳入二個參數
dt = datetime(2022, 3, 23)
print('2022/3/23 的上週六：', getWeeks('Saturday', dt))
