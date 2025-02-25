# 셀프 넘버 구하기 함수
def d(n):
    self_number = n
    while(n > 0):
        self_number += (n % 10)
        n //= 10
    return self_number

# 본문
# 셀프 넘버에 해당하는 인덱스를 0으로 변경해야 함으로 배열의 크기를 10001로 지정정
number_array = [i for i in range(10001)]

for i in range(1, 10001):
    # 셀프 넘버 함수 호출
    self_number = d(i)
    # 허용된 인덱스 안에서 진행되도록 조건문 실행
    if self_number < 10000:
        # 셀프 넘버 일경우 인덱스 값을 0으로 변경
        number_array[self_number] = 0

# 결과 출력(0번째 인덱스는 스킵)
for i in range(10000):
    if number_array[i] != 0:
        print(number_array[i])