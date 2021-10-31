def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
arr=[40,17,12,6,23,21]
print("Unsorted List:",arr)
selection_sort(arr)
print("Sorted List:",arr)
