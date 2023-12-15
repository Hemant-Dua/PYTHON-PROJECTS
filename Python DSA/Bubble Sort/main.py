def bubblesort(arr,size):
    passes = 0
    while (passes != size):
        for i in range(0,size):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        passes+=1
    return arr

if __name__ == "__main__":
    size = int(input("Enter the number of elements in array: "))

    arr = []
    print("Enter the elements of the array: ")
    for i in range(0,size):
        x = int(input())
        arr.append(x)
    
    print(f"The Given array is: {arr}")
    arr = bubblesort(arr,size-1)
    print(f"The Sorted array will be: {arr}")