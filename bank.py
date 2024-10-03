def f():
    s = 20000
    p = 7
    for i in range(5):
        s = s * (p/ 100) + s
    print(s)
f()
