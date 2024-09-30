def sum_without_plus(n1, n2):
    for i in range(n2):
        n1 += 1

    return n1
    # return sum_without_plus(n1+1,n2-1)

a = 6
b = 7
print(sum_without_plus(a,b))