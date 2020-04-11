n = int(input())
matrix = [[0] * n for i in range(n)]
num = 1
end = n
start = 0
while num != num**2:
    for i in range(start, end):
        if num == num**2:
            break
        for j in range(start, end):
            if num == num**2:
                break
            matrix[i][j] = num
            num += 1
            if j + 1 == end:
                for k in range(start+1, end):
                    if num == num**2:
                        break
                    matrix[k][j] = num
                    num += 1
                    if k + 1 == end:
                        for l in range(-end+1, -start):
                            if num == num**2:
                                break
                            matrix[k][l] = num
                            num += 1
                            if l + 1 == start:
                                for m in range(-end+1, -start-1):
                                    if num == num**2:
                                        break
                                    matrix[m][l] = num
                                    num += 1
        end -= 1
        start += 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end='\t')
    print()