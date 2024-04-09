# 1
a = []
s = ''
for i in input():
    a.append(i)
while a!=[]:
    q=a.pop()
    if q in '()':
        s+=q
while')(' in s:
    s=s.replace(')(', '', 1)
if '(' in s or ')' in s:
    print('В строке некорректное количество скобок')
else:
    print('В строке корректное количество скобок')
    

# 2
class Stack:
    def __init__(self, max_len):
        self.stack = []
        self.max_len = max_len

    def push(self, item):
        if len(self.stack) + 1 > self.max_len:
            return Exception('Еrror: eмкость стека превышена')
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return Exception('Error: стек пуст')
        removed = self.stack.pop()
        return removed

    def top(self):
        if len(self.stack) == 0:
            return Exception('Error: стек пуст')
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def __len__(self):
        return len(self.stack)


s = Stack(2)
print(s.push(12))
print(s.push(12))
print(s.push(12))
print(len(s))
print(s.is_empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())


# 3, 3.1
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def adding(self, data)  :
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


my_list = LinkedList()
my_list.adding('C')
my_list.adding('B')
my_list.adding('A')
my_list.adding('225225')
my_list.display()
