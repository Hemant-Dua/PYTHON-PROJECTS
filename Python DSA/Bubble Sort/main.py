def bubblesort(arr):
    flag = True
    while (flag == True):
        flag = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
    return arr

if __name__ == "__main__":
    size = int(input("Enter the number of elements in array: "))

    arr = []
    print("Enter the elements of the array: ")
    for i in range(size):
        x = int(input())
        arr.append(x)
    
    print(f"The Given array is: {arr}")
    arr = bubblesort(arr)
    print(f"The Sorted array will be: {arr}")