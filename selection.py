from select import select


def secletion(a,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if(a[j]<a[i]):
                t=a[j]
                a[j]=a[i]
                a[i]=t
    return a

a=[10,2,34,65,33,4]
n=len(a)
print(secletion(a,n))
