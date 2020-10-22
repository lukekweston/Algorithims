
import random


def createArray(size):
    A = []
    for i in range(size):
        A.append(random.randint(0,size))
    return A


#Works by
#starting at element 1 then moving to the right (key, A[j])
#compare the A[J] with its predacessor, (A[i], if it is bigger than key, move this item across one and continue to next element
#if it is smaller than the key insert the key into the element where the previous bigger one was moved from
#or if index = 0, put key into this index as all elements will have been shifted over by one
#go to next element in the array



# before key == 9
# [3, 3, 10, 10, {9}, 0, 10, 5, 6, 8]
# copy 10 into key index
# [3, 3, 10, {10, 10}, 0, 10, 5, 6, 8]
# copy 10 into key index - 1
# [3, 3, {10, 10}, 10, 0, 10, 5, 6, 8]
# compare 9 with 3, 3 < 9 so insert key into the index that the 10 was moved from in the previous step
# [3, {3}, {9}, 10, 10, 0, 10, 5, 6, 8]


# Example -- part way through sorting (moving key to index 0)
# key is 3 at index 3
#
# before          key
# [4, 6, 7, 9, 9, {3}, 10, 7, 5, 5]
# copy array[key index - 1] into key index as 9 > 3
# [4, 6, 7, 9, {9, 9}, 10, 7, 5, 5]
# copy array[key index - 2] into key index -1 as 9 > 3
# [4, 6, 7, {9, 9}, 9, 10, 7, 5, 5]
# copy array[key index - 3] into key index -2 as 7 > 3
# [4, 6, 7, 7, 9, 9, 10, 7, 5, 5]
# copy array[key index - 4] into key index-3 as 6 > 3
# [4, {6, 6}, 7, 9, 9, 10, 7, 5, 5]
# copy array[key index - 5] into key index- 4 as 4 > 3
# [{4, 4}, 6, 7, 9, 9, 10, 7, 5, 5]
# i = 0, so all elements predassing key in array are larger, so insert key in at index 0
# [3, 4, 6, 7, 9, 9, 10, 7, 5, 5]

#




#book assumes lists start from index 1
def insertionSort(A):
    for j in range(1, len(A)):

        key = A[j]
        # insert A[j] into the sorted sequence A[1..j-1]
        i = j -1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

    return A



#Loop through the array 0..len(array) = i
#loop from end of array for each i for len(array)..i = j
#compare A[j] with A[j-1], if A[j-1] < A[j] then swap, this will move the smallest value into index i eventually
#keep looping through until i loop finishes

#example full sort
# [2, 0, 8, 7, 6, 6, 7, 6, 5, 8]
# pass  0
# 0 will be moved to index 0
# [0, 2, 5, 8, 7, 6, 6, 7, 6, 8]
# pass  1
# 2 will be moved to index 1
# [0, 2, 5, 6, 8, 7, 6, 6, 7, 8]
# pass  2
# 5 will be moved to index 2
# [0, 2, 5, 6, 6, 8, 7, 6, 7, 8]
# pass  3
# 6 will be moved to index 3
# [0, 2, 5, 6, 6, 6, 8, 7, 7, 8]
# pass  4
# 6 will be moved to index 4
# [0, 2, 5, 6, 6, 6, 7, 8, 7, 8]
# 6 will be moved to index 5
# [0, 2, 5, 6, 6, 6, 7, 7, 8, 8]
# pass  6
# already sorted at this point but comparissons will be still be made
# [0, 2, 5, 6, 6, 6, 7, 7, 8, 8]
# pass  7
# [0, 2, 5, 6, 6, 6, 7, 7, 8, 8]
# pass  8
# [0, 2, 5, 6, 6, 6, 7, 7, 8, 8]
# pass  9
# [0, 2, 5, 6, 6, 6, 7, 7, 8, 8]


#Example of a pass

# pass  0
# A[j-1] < A[j] == False , no swap
# [1, 7, 7, 7, 1, 5, 2, 8, {0, 6}]
# A[j-1] < A[j] == true , swap
# [1, 7, 7, 7, 1, 5, 2, {8, 0}, 6]
# A[j-1] < A[j] == true , swap
# [1, 7, 7, 7, 1, 5, {2, 0}, 8, 6]
# A[j-1] < A[j] == true , swap
# [1, 7, 7, 7, 1, {5, 0}, 2, 8, 6]
# A[j-1] < A[j] == true , swap
# [1, 7, 7, 7, {1, 0}, 5, 2, 8, 6]
# A[j-1] < A[j] == true , swap
# [1, 7, 7, {7, 0}, 1, 5, 2, 8, 6]
# A[j-1] < A[j] == true , swap
# [1, 7, {7, 0}, 7, 1, 5, 2, 8, 6]
# A[j-1] < A[j] == true , swap
# [1, {7, 0}, 7, 7, 1, 5, 2, 8, 6]
# A[j-1] < A[j] == true , swap
# [{1, 0}, 7, 7, 7, 1, 5, 2, 8, 6]
#A after first pass, smallest item in index i (0)
# [0, 1, 7, 7, 7, 1, 5, 2, 8, 6]



def bubbleSort(A):
    print(A)
    for i in range(len(A)):
        print("pass ", i)
        # print(A)
        for j in range(len(A) -1 , i, -1):
            print(A)
            # print(A[j], A[j - 1])
            if(A[j] < A[j - 1]):
                A[j], A[j-1] = A[j -1], A[j]
            # print(A)

    return A



# https://www.geeksforgeeks.org/merge-sort/

def divide(arr):

    mid = len(arr) // 2  # Finding the mid of the array
    L = arr[:mid]  # Dividing the array elements
    R = arr[mid:]  # into 2 halves
    # recurssively sorts left and right list
    mergeSort(L)  # Sorting the first half
    mergeSort(R)  # Sorting the second half

    return L, R


def conquer(arr, L, R):
    i = j = k = 0

    # ------------ sort L and R into arr by comparing elements 1 at a time and putting in arr (array of len L + R)
    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # ----------- if any elements left in the lists, they will be in sorted order and can just appened onto the end
    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    print(arr)
    return arr


# Python program for implementation of MergeSort
def mergeSort(arr):
    #Check len is > 1, (Array of size 1 is sorted) - > just returns
    if len(arr) > 1:
        # Get L, R by recursively dividing until len of arrays is 1
        L, R = divide(arr)
        print(L, R)
        # keep combining arrays and sorting
        arr = conquer(arr, L, R)


    return arr







A = createArray(10)
print(A)
# print(insertionSort(A))

# print(bubbleSort(A))
print(mergeSort(A))