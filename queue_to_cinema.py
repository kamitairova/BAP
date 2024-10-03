import random
def f(n):
    banknotes = [25, 50, 100]
    l = 0
    money = [random.choice(banknotes) for _ in range(n)]

    for i in money:
        if i == 25:
            l += 25
        elif i == 50:
            if l >= 25:
                l += 50
                l -= 25
            else:
                print(money)
                print('No')
                return
        else:
            if l >= 75:
                l += 100
                l -= 75
            else:
                print(money)
                print('No')
                return

    print(money)
    print(l)
    print('Yes')

f(3)







