class Linked_List:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    
    def update(self, data):
        self.__data = data
    
    def append(self, node):
        self.__next = node

    def set_next_none(self):
        self.__next = None
    
    def get_next(self):
        return self.__next
    
    def remove(self, prev_node):
        if self.__next != None:
            prev_node.append(self.__next)
        else:
            prev_node.set_next_none()

def main():
    l1 = Linked_List(1)

    l1.append(Linked_List(2))
    l1.append(Linked_List(3))
    l1.append(Linked_List(4))
    l1.append(Linked_List(5))

    temp = l1

    while temp.get_next() != None:
        print(temp.__data)
        temp = temp.get_next()
    
        
