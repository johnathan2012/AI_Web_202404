#匯入CH1217，輸出三個物件

from CH1217 import Motor, sportCar, Hybrid

altiz = Motor('Altiz', 487500) # 父類別物件
print(f'{altiz.show():8s} 定價{altiz.equip():10,}')

inno = sportCar('Innovate', 638000) #子類別物件
print(f'{inno.show():8s} 定價{inno.equip():12,}')

suv = Hybrid('SUV', 1150000) # 子類別物件
print(f'{suv.show():8s} 定價{suv.equip():12,}')
