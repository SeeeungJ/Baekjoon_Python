m, n = list(map(int, input().split()))
division = 2

num_list = [i for i in range(1, n+1)]

for i in range(1, len(num_list)+1):
    for j in range(i, len(num_list), division):
        if num_list[j] % division == 0:
            if num_list[j] != division:
                num_list[j] = 0
    division += 1
    
for i in range(m-1, len(num_list)):
    if num_list[i] != 0:
        print(num_list[i])
        
        # 추가 수정 틀림