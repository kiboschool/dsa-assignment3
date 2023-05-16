class LLString:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self, s):
        self.head = None
        self.tail = None

        for char in s:
            self.append(char)

    def append(self, new_val):
        new_node = LLString.Node(new_val, None)

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    # recursive helper method for printing
    def __print(self, node):
        if node is None:
            print()
        else:
            print(node.val, end='')
            self.__print(node.next)

    def print(self):
        # just invoke the recursive helper method
        self.__print(self.head)

    def to_string(self):
        s = ''
        trav = self.head
        while trav is not None:
            s += trav.val
            trav = trav.next
        return s

    def find(self, c):
        trav = self.head
        index = 0
        while trav is not None:
            if trav.val == c:
                return index
            trav = trav.next
            index += 1
        return -1

    def __to_upper_case(self, node):
        if node is None:
            return
        node.val = node.val.upper()
        self.__to_upper_case(node.next)

    def to_upper_case(self):
        self.__to_upper_case(self.head)

    def replace(self, old, new):
        trav = self.head
        while trav is not None:
            if trav.val == old:
                trav.val = new
            trav = trav.next

    def copy(self):
        return LLString(self.to_string())

    def trim(self):
        while self.head is not None and self.head.val == ' ':
            self.head = self.head.next

        if self.head is None:
            return

        trav = self.head
        last_non_space = trav
        while trav is not None:
            if trav.val != ' ':
                last_non_space = trav
            trav = trav.next

        self.tail = last_non_space
        self.tail.next = None

    def __find_nth(self, n, c, node):
        if node is None:
            return -1
        if node.val == c and n == 1:
            return 0

        if node.val == c:
            next_n = n - 1
        else:
            next_n = n

        index_in_rest = self.__find_nth(next_n, c, node.next)
        if index_in_rest == -1:
            return -1
        else:
            return index_in_rest + 1

    def find_nth(self, n, c):
        if n < 1:
            return -1
        return self.__find_nth(n, c, self.head)
