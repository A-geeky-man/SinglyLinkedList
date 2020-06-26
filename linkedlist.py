class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    # Display the linked list
    def __repr__(self):
        temp = self.head
        nodes = []
        while temp:
            nodes.append(repr(temp))
            temp = temp.next
        return '[' + ', '.join(nodes) + ']'

    # Insert in the linked list
    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data=data)

    # Insert in the beginning of the linked list
    def appendleft(self, data):
        self.head = Node(data=data, next=self.head)

    # Find the element in the linked list
    def find(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        return temp

    # Delete the element from the linked list
    def delete(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not prev:
            self.head = temp.next
        elif temp:
            prev.next = temp.next
            temp = None
        else:
            print(f'{key} not found')

    # Reverse the linked list
    def reverse(self):
        temp = self.head
        prev_node = None
        next_node = None
        while temp:
            next_node = temp.next
            temp.next = prev_node
            prev_node = temp
            temp = next_node
        self.head = prev_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1998)
    ll.append('A-geeky-man')
    ll.append('GitHub')
    ll.appendleft('Jan')
    ll.appendleft(20)
    print(ll)           # printing the original linked list
    ll.reverse()
    print(ll)           # printing the reversed linked list
    print(ll.find(20))  # printing the found element
    print(ll.find('GitHub'))    # printing the found element
    ll.delete(1998)
    print(ll)           # printing the linked list after deleting an element
    ll.reverse()
    print(ll)           # printing the reversed linked list
