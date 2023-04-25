class STACK(object):
    
    def __init__(self):
        self.stack = []
        self.top = -1
        self.maxSize = 5
    
    def push(self,item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        self.stack.pop()
        self.top -= 1

    def peek(self):
        try:
            print(self.stack[self.top]) # self.stack[-1]
        except:
            print("Stack is EMPTY")
    
    def display(self):
        display_stack = []
        for i in range(self.top+1):
            display_stack.append(self.stack[i])
        print(display_stack)

    def isEmpty(self):
        if self.top == -1:
            return True
    
    def isFull(self):
        if self.top >= (self.maxSize-1):
            return "Full"
        
    def work(self):
        print("""\n\n
        a).PUSH item onto STACK
        b).POP item from STACK
        c).PEEK item
        d).Display STACK
        e).Exit""")
        while True:
            choice = input("\nEnter your choce: ").lower()
            if choice == 'a' and self.top+1 <= self.maxSize-1:
                item = int(input("Enter Integer item: "))
                self.push(item)
            elif choice == 'b' and self.top >= 0:
                self.pop()
            elif choice == 'c':
                self.peek()
            elif choice == 'd':
                self.display()
            elif choice == 'e':
                break
            else:
                print("Operation cannot be performed")
                print(f"""
                The Stack           : {self.stack}
                Total items count   : {self.top+1}
                Maximium Stack Size : {self.maxSize}""")
        print("You Quit working with STACK.")

my_stack = STACK()
my_stack.work()
