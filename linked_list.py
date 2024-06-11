class Node:
    """
    Representation of a node, with data and a reference to the next node.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly linked list.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Returns True if the list is empty, False otherwise.
        Takes O(1) time.
        """

        return True if self.head is None else False

    def size(self):
        """
        Determines the size of the list.
        Takes O(n) time.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a node at the head of the list. Takes O(1) time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Searches for a given key, and returns the node if the key
        is found.
        Takes O(n) time to traverse the list and find the node.
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a node with the given data at the given index.
        Inserting takes O(1) time, but searching for the index
        takes O(n) time, so overall runtime is O(n)
        """
        if index == 0:
            self.add(data)

        current = self.head
        position = index
        while position > 1:
            current = current.next_node
            position -= 1

        new_node = Node(data)
        new_node.next_node = current.next_node
        current.next_node = new_node

    def remove(self, key):
        """
        Removes a node from the list, if the given key value is found.
        Takes O(n) time.
        """
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                self.head = current.next_node
                found = True
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node

        return current

    def remove_at_index(self, index):
        """
        Takes in an index and removes the node at that index.
        Runtime is O(n)
        """
        current = self.head
        prev = None

        if index == 0:
            self.head = current.next_node
            return current

        position = 0
        while position < index:
            prev = current
            current = current.next_node
            position += 1

        prev.next_node = current.next_node
        return current

    def node_at_index(self, index):
        """
        Takes in an index and returns the node at that index.
        Runtime is O(n)
        """
        current = self.head

        if index == 0:
            return current

        position = 0
        while position < index:
            current = current.next_node
            position += 1

        return current

    def __repr__(self):
        """
        Returns a string representation of the linked list.
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return "->".join(nodes)


list = LinkedList()
list.add(3)

list.add(10)
list.add(12)
list.add(7)
list.add(3)
list.add(1)
list.add(0)
list.add(-3)
list.add(20)
list.add(15)

# Checking size
print(list.size())

# Checking search function
print(list.search(0))

# Checking is_empty function
print(list.is_empty())

# Checking insert function
print(list.insert(5, 1))
print(list.search(5))

# Checking remove function
print(list.remove(5))
print(list.search(5))

# Checking __repr__function
print(list)

# Checking node_at_index function
print(list.node_at_index(1))

# Checking remove_at_index function
print(list.remove_at_index(2))
print(list)
