from Queue import Queue
from Stack import Stack

# q1 = Queue()

# q1.enqueue("A")
# q1.enqueue("B")
# q1.enqueue("C")

# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())
# print(q1.dequeue())

s1 = Stack()

s1.push("A")
s1.push("B")
s1.push("C")
print("size = ", s1.get_size())

print(s1.pop())
print("size = ", s1.get_size())

print(s1.pop())
print(s1.pop())
print(s1.pop())

print("size = ", s1.get_size())