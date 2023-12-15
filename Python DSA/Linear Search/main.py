def search(arr,size,x):
    for i in range(0,size):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr_size=int(input("Enter the number of elements in array: "))

    arr=[]
    print("Enter the elements of the array: ")
    for i in range(0,arr_size):
        x=int(input())
        arr.append(x)

    target=int(input("Enter the target: "))

    result = search(arr, arr_size, target)
    
    if result == -1:
        print("The required number is not in the array.")

    else:
        print(f"The Target is present at the index: {result}")