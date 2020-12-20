class LinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, python_list):
        self.node = LinkedListNode(python_list[0], None)
        for element in python_list[1:]:
            self.insert(element)

    def length_list(self):
        index = 0
        x = self.node

        while x is not None:
            index +=1
            x = x.next
        return index

    def insert(self, y):
        prev = None
        x = self.node
        y = LinkedListNode(y, None)
        verification_var = False

        while not verification_var :
            if y.data < x.data:
                verification_var = True
                y.next = x
                if prev is not None:
                    prev.next = y
                else:
                    self.node = y
            else:
                prev = x
                if x.next is not None:
                    x = x.next
                else: # x= last
                    x.next = y
                    verification_var = True

    def delete(self, y):
        prev = None
        x = self.node

        while True:
            if y == x.data:  # element to be deleted is found

                if prev is None:  # if elm to be deleted is the firs elm
                    self.node = x.next

                elif x.next is None:  # if elm to be deleted is last
                    prev.next = None

                else:
                    prev.next = x.next  # general case

                break
            else:
                prev = x
                x = x.next
                continue

    def search(self, y):
        index = 1
        x = self.node

        while True:
            if y == x.data:
                return index

            index += 1
            x = x.next

    @staticmethod
    def printer_list(cap_da_tanc):
        x = cap_da_tanc.node

        while x:
            print(x.data)
            x = x.next



# lista = LinkedList([3, 9, 0, 17, 2])
# print(lista)
# lista.delete(17)
# LinkedList.printer_list(lista)