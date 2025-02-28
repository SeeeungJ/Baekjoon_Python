# 사용자가 원하는 막대기 길이
X = int(input())

# 처음에 가지고 있는 64cm의 막대기
stick = [64]

while(sum(stick) != X):
    # 1조건 실행
    if sum(stick) > X:
        # 1-1조건 실행
        temp = min(stick) // 2
        # 가장 마지막 인덱스의 숫자가 나눠진 것임으로 -1번째 인덱스를 제거
        stick.pop(-1)
        # 반으로 나눈 것의 절반을 배열에 추가하여 1-2조건을 테스트
        stick.append(temp)
        # 1-2조건에 부합하지 않으면 반으로 나눈 막대기를 버리지 않고 배열에 추가
        if sum(stick) < X:
            stick.append(temp)
# 배열의 길이로 과정을 거친 횟수 출력
print(len(stick))