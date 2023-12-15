def search(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    
    return -1

if __name__ == "__main__":
    arr_size=int(input("Enter the number of elements in array: "))

    arr=[]
    print("Enter the elements of the array: ")
    for i in range(0,arr_size):
        x = int(input())
        arr.append(x)

    target = int(input("Enter the target: "))

    result = search(arr, 0, arr_size-1, target)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("The element is not present in the array")