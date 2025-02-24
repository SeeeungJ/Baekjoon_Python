# 입력값 N과 비교하여 output값을 구해주는 변수
output = 1
compare = 1

N = int(input())

# compare 값이 N보다 작을 때 반복
while(compare < N):
    compare += 6 * output
    output += 1
print(output)