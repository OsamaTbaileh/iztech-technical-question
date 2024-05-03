# Question: Make a function that will take a sorted array of integers and a target number as inputs, 
#           the target number may be repeated in the array. Return an array with the indexes of the 
#           first and last appearances of the target in the array. [first index, last index]

#           -- If the target number not repeated and appear only once then return the same index for 
#              both first and last appearance. [target index, target index]

#           -- If the target is not in the whole array then return [-1, -1]

def find_first_and_last_index_of_target(arr, target):
    first_index = -1
    last_index = -1

    start = 0
    end = len(arr)-1

    # Find first index.
    while(start<=end):
        middle = (start+end) // 2
        if target == arr[middle]:
            first_index = middle
            end = middle - 1 
        elif target < arr[middle]:
            end = middle-1
        elif target > arr[middle]:
            start = middle +1

    # Reset start and end to find the last index.
    start = 0
    end = len(arr)-1

    # Find last index.
    while(start<=end):
        middle = (start+end) // 2
        if target == arr[middle]:
            last_index = middle
            start = middle + 1 
        elif target < arr[middle]:
            end = middle-1
        elif target > arr[middle]:
            start = middle +1

    return [first_index, last_index]



print(find_first_and_last_index_of_target([1,2,7,7,7,8,12], 7))