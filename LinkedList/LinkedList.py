# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None


# %%
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev node is not in the list")
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        # if current_node is not null and current_node.data == key
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node. next

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_position(self, index):
        current_node = self.head
        
        if index == 0:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None

        count = 1
        while current_node and count != index:
            prev_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None


# %%
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.append("F")
# llist.append("G")
# llist.prepend("E")
# llist.delete_node("B")
# llist.delete_node_position(3)
# llist.insert_after_node(llist.head.next.next.next,'I')
# llist.insert_after_node(llist.head.next, "E")
# llist.print_list()


# %%



