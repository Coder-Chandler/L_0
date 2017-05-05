class Node_Double(object):
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleList(object):
    head = None
    tail = None

    def append(self,data):
        new_node = Node_Double(data,None,None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self,node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                if current_node.prev is not None and current_node.next is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                elif current_node.prev is None:
                    self.head = current_node.next
                    current_node.next.prev = None
            current_node = current_node.next

    def show(self):
        print 'Show List data: '
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev,'data') else None,
            print '<-',current_node.data,'->',
            print current_node.next.data if hasattr(current_node.next,'data') else None

            current_node = current_node.next


d = DoubleList()

d.append(5)
d.append(5)
d.append(50)
d.append(30)
d.append(30)
d.show()

d.remove(30)

d.show()
