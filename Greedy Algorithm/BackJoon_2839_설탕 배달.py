# 변수
count = 0
pocket = [5, 3]

sugar = int(input())

# pocket 배열 인덱스 지정
i = 0

# 설탕 무게가 5kg 이상일 경우 5kg 주머니 먼저 처리
if sugar >= pocket[i]:
    count += sugar // pocket[i]
    sugar %= pocket[i]
    i += 1
    # 5kg 주머니로 나눈 후 3kg 주머니로 처리
    while(True):
        # 남은 설탕 무게가 3kg으로 처리 되는지 확인
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
    
# 5kg 미만일 경우 3kg 주머니로 처리
else: 
    i += 1
    # 3kg로 나누었을 때 나머지가 없는 지 체크
    if sugar % pocket[i] == 0:
        count += sugar // pocket[i]
        print(count)
    else: 
        print(-1)