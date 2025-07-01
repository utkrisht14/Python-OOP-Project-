# Node class defines the structure of each element in the linked list
class Node:

    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    # Getter for value
    @property
    def value(self):
        return self._value

    # Setter for value
    @value.setter
    def value(self, new_value):
        self._value = new_value

    # Getter for next node reference
    @property
    def next(self):
        return self._next

    # Setter for next node reference
    @next.setter
    def next(self, new_next):
        self._next = new_next


# Node objects can be manually linked like this
node_2 = Node(3)
node_1 = Node(5, node_2)

"""
LinkedList stores a sequence of nodes by maintaining a reference to the head node.
Disadvantages of LinkedList:
- It uses more memory due to storing references for each node.
- Elements must be accessed sequentially as there is no direct indexing.
"""

class LinkedList:

    def __init__(self):
        self.head = None

    # Inserts a new node into the linked list while maintaining sorted order
    def insert_node(self, value):
        new_node = Node(value)

        # Case 1: Insert when list is empty
        if self.head is None:
            self.head = new_node

        # Case 2: Insert at the beginning if value is smaller than or equal to head
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node

        # Case 3: Insert in the middle or end
        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next

            new_node.next = runner
            previous.next = new_node

    # Traverses the linked list and prints each value
    def print_list_items(self):
        if self.head is None:
            print("Empty list.")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print()

    # Counts and prints the total number of nodes in the list
    def count_total_nodes(self):
        runner = self.head
        nodes_array = []
        if not runner:
            print("Empty list. So length of list is 0")
        while runner is not None:
            nodes_array.append(runner)
            runner = runner.next
        print(f"Here is your total count: {len(nodes_array)}")

    # Searches for a target value in the list and prints its index
    def find_node(self, target_value):
        if self.head is None:
            print("List is empty. Nothing to search")
            return

        runner = self.head
        index = 0
        while runner is not None:
            if runner.value == target_value:
                print(f"Target value {target_value} was found at index {index}")
                return
            runner = runner.next
            index += 1

        print(f"{target_value} not found in the list")

    # Deletes a node with the given target value from the list
    def delete_node(self, target_value):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        # Case 1: Deleting the head node
        if self.head.value == target_value:
            self.head = self.head.next
            return

        # Case 2 or 3: Deleting a node from the middle or end
        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == target_value:
                prev.next = current.next
                return
            prev = current
            current = current.next

        # Case 4: Target value not found in the list
        print("Target value not found.")


# Creating a new linked list instance
my_linked_list = LinkedList()

# Inserting nodes to form a sorted list
my_linked_list.insert_node(9)
my_linked_list.insert_node(3)
my_linked_list.insert_node(6)
my_linked_list.insert_node(15)

# Accessing values for verification
print(my_linked_list.head.next.value)
print(my_linked_list.head.value)
print(my_linked_list.head.next.next.next.value)

# Traversing the list and printing elements
print("\n================Traversing the list=====================")
my_linked_list.print_list_items()

# Counting the total number of nodes
print("\n================Count total number of nodes=============")
my_linked_list.count_total_nodes()

# Searching for a specific value in the list
print("\n================Find item in a list======================")
my_linked_list.find_node(6)

# Deleting a node and printing the updated list
print("\n================Deleting item from a list===============")
my_linked_list.delete_node(15)
print("After deleting, the updated list is: ")
my_linked_list.print_list_items()
