while(1) :
    data = list(map(int, input().split()))
    data.sort()

    if (data[0]==0) and (data[1]==0) and (data[2]==0) :
        break
    else :
        if data[2]**2 == data[0]**2 + data[1]**2 :
            print('right')
        else :
            print('wrong')
