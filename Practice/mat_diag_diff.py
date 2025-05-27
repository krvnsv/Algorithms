def diag_diff(matrix):
    sum1 = 0
    for i in range(len(matrix)):
        sum1 += matrix[i][i]

    sum2 = 0
    for i in range(len(matrix)):
        sum2 += matrix[i][len(matrix) - 1 - i]
    
    diff = sum2 - sum1

    return diff

print(diag_diff(
    [[1,2,3,5,5],
     [4,5,6,5,5],
     [7,8,9,5,5],
     [4,5,6,5,5],
     [7,8,9,5,5]]))