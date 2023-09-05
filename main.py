def is_uniq(matrix):
    el = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if i != 0 and j != 0:
                if el == matrix[i][j]:
                    return False
    return True

n = int(input())
numbers = [i for i in range(1, n ** 2 + 1)]
matrix = [[int(i) for i in input().split()] for _ in range(n)]
sums = []
flag = True

flag = is_uniq(matrix)

for i in range(n):  # is correct numbers
    for j in range(n):
        if matrix[i][j] not in numbers:
            flag = False

for i in range(n):  # sum rows
    sums.append(sum(matrix[i]))

for i in range(n):  # sum cols
    s = 0
    for j in range(n):
        s += matrix[j][i]
    sums.append(s)

sd = 0  # sum main diagonal
for i in range(n):
    for j in range(n):
        if i == j:
            sd += matrix[i][j]
sums.append(sd)

sd = 0
for i in range(n):  # sums second diagonal
    for j in range(n):
        if j == n - i - 1:
            sd += matrix[i][j]
sums.append(sd)

for i in range(len(sums) - 1):
    if sums[i] != sums[i + 1]:
        flag = False

#print(sums)

if flag == True:
    print("YES")
else:
    print("NO")
