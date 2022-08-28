row, column = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(row):
    matrix.append([int(x) for x in input().split(' ')])
list_sums = []
for i in range(column):
    current_sum = 0
    for j in range (row):
        current_sum += matrix[j][i]
    list_sums.append(current_sum)
print(*list_sums, sep='\n')
