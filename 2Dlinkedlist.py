class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prve=None
    
class DLinkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Double Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

    def delet_beginning(self):
        temp=self.head
        self.head=temp.next
        print(temp.data,"is delete")
        temp.next=None
        temp.next.prve=None

    def delet_end(self):
        before=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            before=before.next
        print(temp.data,"is delete")
        before.next=None
        temp.prev=None
    
    def delete_position(self,pos):
        before=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        print(temp.data,"is delete")
        before.next=temp.next
        temp.next.prve=before
        temp.next=None
        temp.prve=None


def main():
    llist=DLinkedlist()
    n=Node(10)
    llist.head=n
    n1=Node(20)
    n1.prev=n
    n.next=n1
    n2=Node(30)
    n2.prve=n1
    n1.next=n2
    n3=Node(40)
    n3.prve=n2
    n2.next=n3
    while(True):
        print(' \n Menu')
        print('1.Delete a Node at delet_beginning')
        print('2.Delete a Node at delet_end')
        print('3.Delete a Node at delete_position')
        print('4.display')
        print('5.exit')
        option=int(input('Enter your option:'))
        if(option==1):
            llist.delet_beginning()
            llist.display() 
        elif(option==2):
            llist.delet_end()
            llist.display()
        elif(option==3):
            pos=int(input("Enter the positions"))
            llist.delete_position(pos)
            llist.display()
        elif(option==4):
            llist.display()
        elif(option==5):
            break
main()