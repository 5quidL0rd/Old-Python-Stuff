MyStack = []
StackSize = 3

def DisplayStack(): 
    print("Stack currently contains:") 
    for item in MyStack:
        print(item)

def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stack is full!")

def Pop():
    if len(MyStack) > 0:
        print("Popping:", MyStack.pop())
    else:
        print("Stack is empty.")

# Function calls
Push(1)
Push(2)
Push(3)
DisplayStack()
Push(4)
Pop()
DisplayStack()
Pop()
Pop()
Pop()
