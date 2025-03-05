n = int(input())
count = 0
for i in range(1, n+1):
    sub_list = []
    if i < 100:
        count += 1
    else:
        while_num = i
        while(while_num > 9):
            sub = (while_num % 10) - ((while_num // 10) % 10)
            sub_list.append(sub)
            while_num //= 10
        unique_list = list(set(sub_list))
        if len(unique_list) == 1:
            count += 1
print(count)