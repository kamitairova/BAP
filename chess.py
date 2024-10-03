def chess():
    x0 = int(input('x0: '))
    y0 = int(input('y0: '))
    x1 = int(input('x1: '))
    y1 = int(input('x2; '))
    if x0 > 0 and x0 < 9 and y0 > 0 and y0 < 9 and x1 > 0 and x1 < 9 and y1 > 0 and y1 < 9:
        if abs(x0-x1)==2 and abs(y0-y1)==1 or abs(x0-x1)==1 and abs(y0-y1)==2:
           print(True)
        else:
            print(False)
    else:
        print(False)
chess()