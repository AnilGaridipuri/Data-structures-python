class queue:
    def __init__(self):
        self.queue=[]
    def push(self,n):
        if (len(self.queue)==n):
            print("queue is full")
        else:
            ele=int(input("Enter the elements"))
            self.queue.append(ele)
        
    def pop(self):
        if(len(self.queue)==0):
            print("queue is empty")
        else:
            print("the pop the element is",self.queue.pop(0))
    def display(self):
        if(len(self.queue)==0):
            print("queue is empty")
        else:
            for a in self.queue:
                print(a)

def main():
    q=queue()
    n=int(input("Enter the size of the queue"))
    while True:
        print("menu")
        print("1.push")
        print("2.pop")
        print("3.display")
        print("4.exit")
        opt=int(input("Enter your option"))
        if opt==1:
            q.push(n)
        elif opt==2:
            q.pop()
        elif opt==3:
            q.display()
        elif opt==4:
            break
main()