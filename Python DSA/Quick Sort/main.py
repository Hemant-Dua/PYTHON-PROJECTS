def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub

    while (start < end):
        while (arr[start] <= pivot):
            start+=1
        while (arr[end] > pivot):
            end-=1
        if start < end:
            arr[start],arr[end] = arr[end],arr[start]
        
    arr[lb],arr[end] = arr[end],arr[lb]
    return end
    
def quicksort(arr, lb, ub):
    if (lb < ub):
        loc = partition(arr, lb, ub)
        quicksort(arr, lb, loc-1)
        quicksort(arr, loc+1, ub)

if __name__ == "__main__":
    size = int(input("Enter the number of elements in array: "))

    arr = []
    print("Enter the elements of the array: ")
    for i in range(0,size):
        x=int(input())
        arr.append(x)

    print(f"The given array is: {arr}")
    quicksort(arr, 0, size-1)
    print(f"The sorted array will be: {arr}")