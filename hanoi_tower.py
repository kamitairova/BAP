def hanoi(n, a, b, c):
    if n == 1:
        print(f"{n}{a}{b}")
    else:
        hanoi(n - 1, a, c, b)
        print(f"{n}{a}{b}")
        hanoi(n - 1, c, b, a)

n = int(input(": "))
hanoi(n, 1, 3, 2)