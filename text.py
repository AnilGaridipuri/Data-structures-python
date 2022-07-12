def mergesort(mylist):
    if  len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while(i<len(left) and j<len(right)):
            if(left[i]<=right[j]):
                mylist[k]=left[i]
                i=i+1
            else:
                mylist[k]=right[j]
                j=j+1
            k=k+1
        
        while(i<len(left)):
            mylist[k]=left[i]
            i=i+1
            k=k+1

        while(j<len(right)):
            mylist[k]=right[j]
            j=j+1
            k=k+1
mylist=[10,2,32,16,75,22]
mergesort(mylist)
print(mylist)
        