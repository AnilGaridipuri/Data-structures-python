class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLinkedlist:
    def __inti__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Linked list is emty:")
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

    def delet_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        print(temp.data,"is delete")
        prev.next=None
    
    def delete_position(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        print(temp.data,"is delete")
        prev.next=temp.next


def main():
    llist=SLinkedlist()
    n=Node(10)
    llist.head=n
    n1=Node(20)
    n.next=n1
    n2=Node(30)
    n1.next=n2
    n3=Node(40)
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