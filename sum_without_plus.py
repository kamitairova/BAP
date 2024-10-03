def sum_without_plus(n1, n2):
    for i in range(n2):
        n1 += 1

    return n1

a = 10
b = 9
print(sum_without_plus(a,b))