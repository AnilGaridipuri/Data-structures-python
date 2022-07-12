class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,n):
        if (len(self.stack)==n):
            print("stack is full")
        else:
            ele=int(input("Enter the elements"))
            self.stack.append(ele)
        
    def pop(self):
        if(len(self.stack)==0):
            print("Stact is empty")
        else:
            print("the pop the element is",self.stack.pop())
    def display(self):
        if(len(self.stack)==0):
            print("Stact is empty")
        else:
            for a in self.stack:
                print(a)
def main():
    s=stack()
    n=int(input("Enter the size of the stact"))
    while True:
        print("menu")
        print("1.push")
        print("2.pop")
        print("3.display")
        print("4.exit")
        opt=int(input("Enter your option"))
        if opt==1:
            s.push(n)
        elif opt==2:
            s.pop()
        elif opt==3:
            s.display()
        elif opt==4:
            break
main()
    







# # Stack implementation in python


# # Creating a stack
# def create_stack():
#     stack = []
#     return stack


# # Creating an empty stack
# def check_empty(stack):
#     return len(stack) == 0


# # Adding items into the stack
# def push(stack, item):
#     stack.append(item)
#     print("pushed item: " + item)


# # Removing an element from the stack
# def pop(stack):
#     if (check_empty(stack)):
#         return "stack is empty"

#     return stack.pop()


# stack = create_stack()
# push(stack, str(1))
# push(stack, str(2))
# push(stack, str(3))
# push(stack, str(4))
# print("popped item: " + pop(stack))
# print("stack after popping an element: " + str(stack))
