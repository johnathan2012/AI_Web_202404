import math

#算出圓周長
def calcPerimeter(radius):
    return 2 * radius * math.pi

#算出圓面積
def roundArea(radius):
    return radius * radius * math.pi

print(f'圓周長：{calcPerimeter(15):4f}')
print(f'圓面積：{roundArea(15):4f}')
