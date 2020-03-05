#Selection Sort
A = [9,4,5,7,1,2,4,6,8,9,10,3,2,7,8,9,0]

for i in range(len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
print(A)

#Reversed
array = [9,4,5,7,1,2,4,6,8,9,10,3,2,7,8,9,0]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] < array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]
print(array)