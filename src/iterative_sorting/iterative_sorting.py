# TO-DO: Complete the selection_sort() function below 
#each index is selected and min value across the array is looked for and is swapped with the index valued if needed
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        min = arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range (i+1,len(arr)):
            if arr[j] <min :
               min= arr[j]
               cur_index= j

        # TO-DO: swap
        temp= arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index]= temp

    return arr

print ("Sorted array",selection_sort([5,3,8,2,1]))

# TO-DO:  implement the Bubble Sort function below[5,2,9,0,4,1]
def bubble_sort( arr ):
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    maxNum=max(arr)
    minNum=min(arr)
    dict={}
    for  num in arr:
        if num in dict:
            dict[num]+=1
        else:
            dict[num]=1
    result=[]
    for i in range (minNum,maxNum+1) :#For each number possible in range
         if i in dict:# Check if we have seen this number. d[i] represents number of times i appeared
             while  dict[i]:#We need to append i d[i] times
                 result.append(i)
                 dict[i]-=1#Reduce frequence.

    return result

print ("Sorted count array",count_sort([5,3,8,2,5,2,1,3]))