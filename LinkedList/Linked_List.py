class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next(self):
        return self._next

node_2 = Node(3)
node_1 = Node(5, node_2)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            current_node = self.head.next

            while (current_node is not None) and (value > current_node.value):
                previous = current_node
                current_node = current_node.next

            new_node.next = current_node
            previous.next = new_node

        # Traversing the list.
        def print_list_items(self):
            if self.head is None:
                print("Linked List is empty.")
            else:
                current_node = self.head
                while current_node is not None:
                    print(current_node.value, end=" ")
                    current_node = current_node.next
                print()

        # Count the total number of nodes
        def count_total_nodes(self):
            pass


