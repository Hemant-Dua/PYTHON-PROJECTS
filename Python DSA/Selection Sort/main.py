def selectionsort(arr,size):
    for i in range(0,size-1):
        min = i
        for j in range(i+1,size):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr

if __name__ == "__main__":
    size = int(input("Enter the number of elements in array: "))

    arr = []
    print("Enter the elements of the array: ")
    for i in range(0,size):
        x=int(input())
        arr.append(x)

    print(f"The given array is {arr}")
    arr = selectionsort(arr, size)
    print(f"The sorted array will be {arr}")