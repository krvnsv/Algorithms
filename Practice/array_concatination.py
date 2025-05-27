def concatinateArr(arr1, arr2):
    resultArr = []

    for i in range(len(arr1)):
        resultArr.append(arr1[i])

    for i in range(len(arr2)):
        resultArr.append(arr2[i])

    return resultArr

print(concatinateArr([1,2,3,4],[5,6,7,8]))