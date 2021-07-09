class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        '''Appends a new node at the end.'''
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def push(self, data):
        '''insert a new node at the beginning'''
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAfter(self, data, prev_node):
        '''Inserts a new node after the given prev_node.'''
        node = Node(data)
        found = False
        # look for prev_node
        current_node = self.head
        while current_node:
            if current_node.data == prev_node:
                found = True
                break
            current_node = current_node.next
        if found:
            node.next = current_node.next
            current_node.next = node
        else:
            print('Previous node does not exists')

    def delete(self, data):
        '''delete a node'''
        found = False
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == data:
                found = True
                break
            previous_node = current_node
            current_node = current_node.next
        if found:
            if previous_node is None:
                self.head = current_node.next
            else:
                previous_node.next = current_node.next
        else:
            print('Requested does not exists')

    def deleteList(self):
        current_node = self.head
        while current_node:
            temp = current_node.next
            del current_node.data
            current_node = temp

    def traverse(self):
        output_list = []
        current_node = self.head
        while current_node:
            output_list.append(current_node.data)
            current_node = current_node.next
        return output_list

    def getCount(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def _getCountRecursive(self, node):
        if not node:
            return 0
        else:
            return 1 + self._getCountRecursive(node.next)

    def getCount2(self):
        return self._getCountRecursive(self.head)

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def getNth(self, index):
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node.data
            count += 1
            current_node = current_node.next
        return None

    def print_list(self):
        list = self.traverse()
        if len(list) > 0:
            for element in self.traverse():
                print(element, end='=>')
        print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.push(3)
    ll.insertAfter(4, 1)
    print('No of elements ', ll.getCount())
    ll.print_list()
    print('Is 2 available(before delete) ?', ll.search(2))
    ll.delete(2)
    print('Is 2 available(after delete) ?', ll.search(2))
    ll.print_list()
    ll.delete(3)
    ll.print_list()
    ll.delete(4)
    ll.print_list()
    print('No of elements ', ll.getCount())
    print('No of elements(Recursive) ', ll.getCount2())
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.print_list()
    print(ll.getNth(0))
    print(ll.getNth(2))
    print(ll.getNth(4))
