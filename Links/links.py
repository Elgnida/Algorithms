class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getData(self):
        return self.val
    
    def getNext(self):
        return self.next
    
    def setNext(self, new_next):
        self.next = new_next

    def setVal(self, new_val):
        self.val = new_val



class Unordered_list:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.getNext()    
        return count
    
un_lst = Unordered_list()
un_lst.add(5)
un_lst.add(5)
un_lst.add(5)
un_lst.add(5)
print(un_lst.size())


l = [1, 2, 3, 4]

a = l

a.pop()

print(a, l)