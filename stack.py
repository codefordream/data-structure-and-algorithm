class Stack:
    def __init__(self):
        self.stack=[]

# method to Push element
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

# method to pop element
    def remove(self):
        if len(self.stack) <= 0:
            return ("Stack is empty")
        else:
            return self.stack.pop()


# method to find Top of the stack  
    def top(self):
        return self.stack[-1]

# Print all elements
    def Sprint(self):
        return (self.stack)

s = Stack()
s.add("Jan")
s.add("Feb")
s.add("Mar")
s.add("Apr")
s.add("May")
print('Top of The Stack: {}'.format(s.top()))
print('Poped Element: {}'.format(s.remove()))
print('Stack Elements: {}'.format(s.Sprint()))