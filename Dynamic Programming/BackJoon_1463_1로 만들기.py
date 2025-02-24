while(True):
    count = 0
    x = int(input("x 입력 : "))
    
    # test 종료
    if x == -1:
        break
    while(True):
        if x == 1:
            break
        elif x % 3 == 0:
            x //= 3
            print("x를 3으로 나누기 x = ", x)
            count += 1
        elif x % 2 == 0:
            x //= 2
            print("x를 2으로 나누기 x = ", x)
            count += 1
        else:
            x -= 1
            print("x - 1, x = ", x)
            count += 1
    print(count)