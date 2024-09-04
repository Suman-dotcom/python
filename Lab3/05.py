def reversed_list(arr):
    rev_arr =[]
    for i in range(len(arr)-1, -1,-1):
        rev_arr.append(arr[i])
    return rev_arr

arr = [1,2,3,4,5,6]

print(reversed_list(arr))