# def quick_sort(arry,left,right):
#     if(left<right):
#         partition_pos=partition(arry,left,right)
#         quick_sort(arry,left,partition_pos-1)
#         quick_sort(arry,partition_pos+1,right)
# def partition(arry,left,right):
#     i=left
#     j=right-1
#     t=arry[right]
#     while i<j:
#         while i<right and arry[i]<t:
#             i=i+1
#         while j>left and arry[j]>t:
#             j=j+1
#         if(i<j):
#             arry[i],arry[j]=arry[j],arry[i]
#     if(arry[i]>t):
#         arry[i],arry[t]=arry[t],arry[i]
#     return i

# arry=[10,2,34,21,65,3,24]
# n=len(arry)
# (quick_sort(arry,0,n-1))
# print(arry)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr, low, high):
    i = (low-1)      
    pivot = arr[high]    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])