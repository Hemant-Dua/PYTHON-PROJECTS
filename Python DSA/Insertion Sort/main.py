def insertionsort(arr, size):
    for i in range(1,size):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
    return arr

if __name__ == "__main__":
    size = int(input("Enter the number of elements in array: "))

    arr = []
    print("Enter the elements of the array: ")
    for i in range(0,size):
        x=int(input())
        arr.append(x)
        
    print(f"The Given array is: {arr}")
    arr = insertionsort(arr, size)
    print(f"The Sorted array will be: {arr}")