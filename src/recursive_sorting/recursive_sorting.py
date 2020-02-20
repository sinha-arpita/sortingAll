# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
   # elements = len( arrA ) + len( arrB )
    #merged_arr = [0] * elements
    merged_arr=[]
    # TO-DO
    i=0
    j=0
    while i < len(arrA) and j < len(arrB):
        if arrA[i]< arrB[j]:
            merged_arr.append(arrA[i])
            i += 1

        else :

            merged_arr.append(arrB[j])
            j += 1
    while i<len(arrA) :

        merged_arr.append(arrA[i])
        i += 1


    while j < len(arrB):

        merged_arr.append(arrB[j])
        j += 1


    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    arr= merge(left,right)

    return arr

print(merge_sort([7,5,9,2,3,1]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
def partition(arr):
    left=[]
    right=[]
    pivot =arr[0]
    for i in arr[1:]:
        if pivot>= i:
            left.append(i)
        else:
             right.append(i)

    return left,pivot,right
def quicksort(array):
    if len(array)<=1 :
        return array
    left,pivot,right=partition(array)
    return quicksort(left)+[pivot]+quicksort(right)

print(quicksort([7,5,9,2,3,1]))


