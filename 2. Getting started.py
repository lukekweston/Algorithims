
import random


def createArray(size):
    A = []
    for i in range(size):
        A.append(random.randint(0,size))
    return A


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
        # print(A)

    return A

def mergeSort(A):
    return

def bubbleSort(A):
    print(A)
    for i in range(len(A)):
        print("pass ", i)
        for j in range(len(A) -1 , i, -1):
            print(A[j], A[j - 1])
            if(A[j] < A[j - 1]):
                A[j], A[j-1] = A[j -1], A[j]
                print(A)

    return A


A = createArray(10)
print(A)
# print(insertionSort(A))

print(bubbleSort(A))