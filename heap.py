# def heapify(arr,n,i):
#     large=i
#     l=2*i+1
#     r=2*i+2
#     if l<n and arr[i]<arr[l]:
#         large=i
#     if r < n and arr[large] < arr[r]:
#         large = r
#     if large!=i:
#         arr[i],arr[large]=arr[large],arr[i]
#     heapify(arr,n,large)
# def heapsort(arr):
#     n=len(arr)
#     for i in range((n//2)-1,-1,-1):
#         heapify(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[i],arr[0]=arr[0],arr[i]
#         heapify(arr,i,0)


# arr=[10,2,32,43,21,5]
# n=len(arr)
# heapsort(arr)
# print("sorted arry")
# print(arr)


# def heapify(arr, n, i):
#     largest = i 
#     l = 2 * i + 1    
#     r = 2 * i + 2     
  
#     if l < n and arr[i] < arr[l]:
#         largest = l
  
#     if r < n and arr[largest] < arr[r]:
#         largest = r
  
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i] 
#         heapify(arr, n, largest)
  
# # The main function to sort an array of given size
# def heapSort(arr):
#     n = len(arr)
  
#     # Build a maxheap.
#     # Since last parent will be at ((n//2)-1) we can start at that location.
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
  
#     # One by one extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]   # swap
#         heapify(arr, i, 0)
  
# # Driver code to test above
# arr = [ 12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print ("Sorted array is")
# for i in range(n):
#     print ("%d" %arr[i]),






def heapify(arry,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arry[i]<arry[l]:
        largest=l
    if r<n and arry[largest]<arry[r]:
        largest=r
    if largest!=i:
        arry[i],arry[largest]=arry[largest],arry[i]
        heapify(arry,n,largest)

def heapsort(arry):
    n=len(arry)
    for i in range(n//2-1,-1,-1):
        heapify(arry,n,i)
    for i in range(n-1,0,-1):
        arry[i],arry[0]=arry[0],arry[i]
        heapify(arry,i,0)


arry = [ 12, 11, 13, 5, 6, 7]
heapsort(arry)
n = len(arry)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arry[i])











