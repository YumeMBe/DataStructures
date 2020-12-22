class LinkedNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def __lt__(self, other):

        if self.data < other.data:
            return True
        else:
            return False

class DoubleLinked:
    def __init__(self, python_list):
        self.node = LinkedNode(python_list[0], None, None)
        for element in python_list[1:]:
            self.insert_elm(element)

    def lst_length(self):
        x = self.node
        index = 0

        while x:
            x = x.next
            index += 1
        return index

    def insert_elm(self, y):
        x = self.node
        y = LinkedNode(y, None, None)
        verification_var = False

        while not verification_var:
            if y < x:
                verification_var = True
                y.prev = x.prev
                y.next = x
                if x.prev is not None:
                    x.prev.next = y
                    x.prev = y
                else:
                    self.node = y
            else:
                if x.next is not None:
                    x = x.next
                else: # last element
                    x.next = y
                    y.next = None
                    y.prev = x
                    verification_var = True

    def delete_elm(self, y):
        x = self.node

        while True:
            if y == x.data:  # element to be deleted is found

                if x.prev is None:  # if elm to be deleted is the firs elm
                    self.node = x.next

                elif x.next is None:  # if elm to be deleted is last
                    x.prev.next = None

                else:
                    x.prev.next = x.next  # general case

                break
            else:
                x.prev = x
                x = x.next
                continue

    def search_elm(self, y):
        index = 1
        x = self.node

        while True:
            if y == x.data:
                return index

            index += 1
            x = x.next




