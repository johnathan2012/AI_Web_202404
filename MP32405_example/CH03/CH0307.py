# 巢狀if敘述判斷輸入分數

score = int(input('請輸入分數-> '))

if score >= 60:
    if score >= 70:
        if score >= 80:
            if score >= 90:
                print(score, '= A')
            else:
                print(score, '= B')
        else:
            print(score, '= C')
    else:
        print(score, '= D')
else:
    print(score, '= E')
