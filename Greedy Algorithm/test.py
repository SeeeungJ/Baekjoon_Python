count = 0
pocket = [5, 3]

sugar = int(input("설탕 무게 : "))    
i = 0
if sugar >= pocket[i]:
    count += sugar // pocket[i]
    sugar %= pocket[i]
    i += 1
    while(True):
        if sugar % 3 == 0:
            count += sugar // pocket[i]
            print(count)
            break
        else:
            if count == 0:
                print(-1)
                break
            else:
                count -= 1
                sugar += pocket[i-1]

else: 
    i += 1
    if sugar % pocket[i] == 0:
        count += sugar // pocket[i]
        print(count)
    else: 
        print(-1)