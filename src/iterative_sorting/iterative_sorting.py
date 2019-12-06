# TO-DO: Complete the selection_sort() function below 
#each index is selected and min value across the array is looked for and is swapped with the index valued if needed
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        min=arr[i]
        for j in range (i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                smallest_index=j
           # TO-DO: swap 
        temp=arr[i]
        arr[j]=arr[smallest_index]
        arr[smallest_index]=temp
    return arr         

print(selection_sort([7,4,9,0,1,2]))

# TO-DO:  implement the Bubble Sort function below[5,2,9,0,4,1]
def bubble_sort( arr ):
    # outer loop that will decide how many times the process will be repeated, the number of passes, it will be len(arr-1
    for i in range(0,len(arr)-1):
        swap=0
        #get inside the inner for loop which will compare the elements and if they are not at the right position it will swap
        for j in range (0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swap=1
        if swap==0:
           break

    return arr
print ("Sorted array",bubble_sort([5,3,8,2,1]))

    





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