


def min_taxi(n, members):
    g_1 = 0
    g_2 = 0
    g_3 = 0
    g_4 = 0
    for i in range(n):
        if members[i] == 1:
            g_1 += 1
        elif members[i] == 2:
            g_2 += 1
        elif members[i] == 3:
            g_3 += 1
        else:
            g_4 += 1
    diff = g_1 - g_3
    
    
    
    counter = g_4 + g_3 +g_2//2
    if g_2%2 !=0:
        counter += 1
    if diff > 0:
        counter += (diff)//4
    


    return counter



groups_2 = int(input(""))
mem_in_groups_2 = input()
taxis = min_taxi(groups_2, mem_in_groups_2)
print(taxis)


    


