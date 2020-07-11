class Queue:
    def __init__(self):
        self.queue = []

# enqueue operation
    def add(self,dataval):
        self.queue.insert(0,dataval)
        return True

# dequeue operation
    def remove(self):
        if len(self.queue) <= 0:
            return "Queue is Empty"
        else:
            return self.queue.pop()

# Print all elements
    def Sprint(self):
        return (self.queue)

#print Front 
    def front(self):
        if len(self.queue) <= 0:
            return "Empty Queue"
        else:
            return self.queue[-1]

#print Rear
    def rear(self):
        if len(self.queue) <= 0:
            return "Empty Queue"
        else:
            return self.queue[0]

q = Queue()
q.add("Jan")
q.add("Feb")
q.add("Mar")
q.add("Apr")
q.add("May")
print('Front of The Queue: {}'.format(q.front()))
print('Rear of The Queue: {}'.format(q.rear()))
print('Poped Element: {}'.format(q.remove()))
print('Queue Elements: {}'.format(q.Sprint()))