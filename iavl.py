
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root = self.root.insert(key, value)
        self.size += 1

    def delete(self, key):
        if self.root is None:
            raise KeyError(key)
        else:
            self.root = self.root.delete(key)
            self.size -= 1
    
    def __len__(self):
        return self.size

    def __getitem__(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        raise KeyError(key)

    def display(self):
        if self.root is None:
            return ''
        return self.root.display()
    

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

    def display(self, level=0, prefix=''):
        ret = "\t"*level + prefix + repr(self.key) + " : " + repr(self.value) + "\n"
        if self.left is not None:
            ret += self.left.display(level+1, 'L: ')
        if self.right is not None:
            ret += self.right.display(level+1, 'R: ')
        return ret

    def clone(self):
        node = Node(self.key, self.value)
        node.height = self.height
        node.left = self.left
        node.right = self.right
        return node

    def insert(self, key, value, rebalance=True):
        if self.is_leaf():
            if key < self.key:
                node = Node(key, '')
                node.left = Node(key, value)
                node.right = self
                node.height = 2
                return node
            elif key > self.key:
                node = Node(self.key, '')
                node.left = self
                node.right = Node(key, value)
                node.height = 2
                return node
            else:
                return Node(key, value)
        else:
            node = self.clone()
            if key < self.key:
                node.left = self.left.insert(key, value)
            else:
                node.right = self.right.insert(key, value)
            if rebalance:
                return node.rebalance()
            return node
    
    def delete(self, key, rebalance=True):
        if self.is_leaf():
            if key != self.key:
                raise KeyError(key)
            return None
        else:
            node = self.clone()
            if key < self.key:
                node.left = self.left.delete(key)
                if node.left is None:
                    node.key = node.right.key
                    node.value = node.right.value
                    node.left = node.right.left
                    node.right = node.right.right
            else:
                node.right = self.right.delete(key)
                if node.right is None:
                    node.key = node.left.key
                    node.value = node.left.value
                    node.right = node.left.right
                    node.left = node.left.left
            if rebalance:
                return node.rebalance()

            return node                 

    def rebalance(self):
        self.update_height()
        balance = self.balance()
        if balance > 1:
            if self.left.balance() < 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        elif balance < -1:
            if self.right.balance() > 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        return self

    def rotate_right(self):
        node = self.clone()
        root = node.left.clone()
        node.left = root.right
        root.right = node
        node.update_height()
        root.update_height()
        return root

    def rotate_left(self):
        node = self.clone()
        root = self.right.clone()
        node.right = root.left
        root.left = node
        node.update_height()
        root.update_height()
        return root

    def update_height(self):
        self.height = 1 + max(self.left_height(), self.right_height())

    def balance(self):
        return self.left_height() - self.right_height()

    def left_height(self):
        if self.left is None:
            return 0
        return self.left.height

    def right_height(self):
        if self.right is None:
            return 0
        return self.right.height

    def is_leaf(self):
        return self.height == 1
