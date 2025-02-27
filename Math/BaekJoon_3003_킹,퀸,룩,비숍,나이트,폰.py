white_chess = [1, 1, 2, 2, 2, 8]

find_white_chess = list(map(int, input().split()))

result = [chess - find for chess, find in zip(white_chess, find_white_chess)]

for i in range(len(result)):
    print(result[i], end=" ")