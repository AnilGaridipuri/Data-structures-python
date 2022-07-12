def insetion(a,n):
    for i in range(0,n):
        t=a[i]
        j=i
        while(j>0 and t<a[j-1]):
            a[j]=a[j-1]
            j=j-1
        a[j]=t
    return a
a=[10,21,3,2,53,12,32,35]
n=len(a)
print("Before the sort the arry",a)
print("After sort the arry",insetion(a,n))