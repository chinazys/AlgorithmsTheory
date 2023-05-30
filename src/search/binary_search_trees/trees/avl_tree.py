class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def contains_left_node(self):
        if self.left == None:
            return False
        return True

    def contains_right_node(self):
        if self.right == None:
            return False
        return True

    def is_leaf(self):
        if self.left or self.right:
            return False
        return True

    def get_balance(self):
        if self.is_leaf():
            return 0
        elif self.contains_right_node() == False:
            return-self.left.height - 1
        elif self.contains_left_node() == False:
            return self.right.height + 1
        return self.right.height - self.left.height

    def get_height(self):
        if self.is_leaf():
            self.height = 0
        elif not self.contains_left_node():
            self.height = self.right.height + 1
        elif not self.contains_right_node():
            self.height = self.left.height + 1
        else:
            self.height = max(self.left.height, self.right.height) + 1
        
    def left_rotation(self):
        right_child = self.right
        self.right = right_child.left
        right_child.left = self
        self.get_height()
        right_child.get_height()
        return right_child

    def right_rotation(self):
        left_child = self.left
        self.left = left_child.right
        left_child.right = self
        self.get_height()
        left_child.get_height()
        return left_child
    
    def __str__(self) -> str:
        return '{ ' + self._get_node_str(self) + ' }'
    
    def _get_node_str(self, node):
        if node is None:
            return ''

        left_string = self._get_node_str(node.left)
        if len(left_string) > 0:
            left_string += ' <- '

        right_string = self._get_node_str(node.right)
        if len(right_string) > 0:
            right_string = ' -> ' + right_string

        return left_string + str(node.key) + right_string
 
class AVLTree:
    def __init__(self):
        self.root = None

    def get_leaves_height(self):
        if self.root is None:
            return []
        
        leaves_height_list = []
        self._get_leaves_height(self.root, leaves_height_list, 0)

        return leaves_height_list

    def _get_leaves_height(self, node: Node, leaves_height_list: list, depth):
        if node.is_leaf():
            leaves_height_list.append(depth + 1)
            return
        if node.contains_left_node():
            self._get_leaves_height(node.left, leaves_height_list, depth + 1)
        if node.contains_right_node():
            self._get_leaves_height(node.right, leaves_height_list, depth + 1)

    def find(self, key):
        node = self._find(key, self.root)
        return node if node else None
    
    def _find(self, key, node: Node):
        if node is None:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._find(key, node.left)
        elif key > node.key:
            return self._find(key, node.right)
    
    def insert(self, key, node=None):
        if self.root is None:
            self.root = Node(key)
            return

        if node is None:
            node = self.root

        if key == node.key:
            return
        elif key < node.key:
            if node.contains_left_node():
                added_subtree = self.insert(key, node.left)
                if added_subtree is not None:
                    node.left = added_subtree
            else:
                added_node = Node(key)
                node.left = added_node
        else:
            if node.contains_right_node():
                added_subtree = self.insert(key, node.right)
                if added_subtree is not None:
                    node.right = added_subtree
            else:
                added_node = Node(key)
                node.right = added_node
        node.get_height()
        return self.balance(node)

    def balance(self, node: Node):
        bf = node.get_balance()
        if bf < 2 and bf > -2: 
            return None
        if bf < -1:
            if node.left.get_balance() < 0:
                new_root = node.right_rotation()
            else:
                node.left = node.left.left_rotation()
                new_root = node.right_rotation()
        else:
            if node.right.get_balance() > 0:
                new_root = node.left_rotation()
            else:
                node.right = node.right.right_rotation()
                new_root = node.left_rotation()
        if node is self.root:
            self.root = new_root
        return new_root
    
    def __str__(self) -> str:
        return str(self.root)

if __name__ == '__main__':
    b = AVLTree()
    b.insert(11)
    print(b)
    b.insert(15)
    print(b)
    b.insert(17)
    print(b)
    b.insert(18)
    print(b)
    b.insert(19)
    print(b)
    b.insert(22)
    print(b)
    b.insert(16)
    print(b)
    print(b.get_leaves_height())