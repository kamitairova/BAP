s = 20000
y = 5
p = 0.07

#s = s*(1+p)**y

#print(s)

# ls = [-7, -6, -1, 0, 1, 2, 4, 6, 13, 26, 35]
#
#
# n = 6
#
# start_index = 0
# end_index = len(ls)-1
#


def deposit(s, p, y):
    result = s * (1 + p)
    y_left = y - 1
    if y_left > 0:
        return deposit(result, p, y_left)
    return result


result = deposit(s,p,y)
print(result)
