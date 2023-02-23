

def partition(arr,left,right,pivot):
    # choose rightmost element as pivot
    while left <= right:
        while arr[left] < pivot:
            left+=1

        while arr[right] > pivot:
            right-=1

        if left<=right:
            s = arr[left]
            arr[left] = arr[right]
            arr[right] = s
            left+=1
            right-=1

    return left

def quicksort(arr,left,right):
    if left >= right:
        return
    pivot = arr[(left+right)/2]
    index = partition(arr,left,right,pivot)
    quicksort(arr, left, index-1)
    quicksort(arr, index, right)




