pos_y = int(input("Enter y position of chess figure: "))
pos_x = int(input("Enter x position of chess figure: "))

st_y = int(input("Enter y position of your move: "))
st_x = int(input("Enter x position of your move: "))

dif_y = abs(pos_y - st_y)
dif_x = abs(pos_x - st_x)

if 0 > min(pos_y, pos_x, st_y, st_x) > 8:
    print("you are Invalid")
elif dif_y + dif_x == 3:
    print("it is possible to move here")
else:
    print('it is not possible to move here')

