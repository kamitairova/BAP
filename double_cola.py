def double_cola(queue, n):
    length = len(queue)

    if n <= length:
        return queue[n - 1]

    return double_cola(queue, (n - length + 1) // 2)



names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input("Enter: "))
print(double_cola(names, n))


