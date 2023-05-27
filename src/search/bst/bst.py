class Node:
    def __init__(self) -> None:
        self.key = None
        self.left = None
        self.right = None
        self.subtree_length = 0

    def set_key(self, key):
        self.key = key
        self.left = Node()
        self.right = Node()
        self.subtree_length = 1
    
    def unlink_biggest_child(self):
        node = self

        if node.right.key is None:
            return node
        
        while not node.right.right.key is None:
            node.subtree_length -= 1
            node = node.right
        node.subtree_length -= 1

        unlinked = node.right
        node.right = Node()

        return unlinked

    def __str__(self) -> str:
        return '{ ' + self._get_node_str(self) + ' }'
    
    def _get_node_str(self, node):
        if node.key is None:
            return ''

        left_string = self._get_node_str(node.left)
        if len(left_string) > 0:
            left_string += ' <- '

        right_string = self._get_node_str(node.right)
        if len(right_string) > 0:
            right_string = ' -> ' + right_string

        return left_string + '(' + str(node.key) + '; ' + str(node.subtree_length) + ')' + right_string
    
    
class BST:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert_as_leaf(self, key):
        result = self._insert_as_leaf(self.root, key)
        if not result:
            print('Key already present')

    def _insert_as_leaf(self, node: Node, key):
        if node.key is None:
            node.set_key(key)
            return True
        
        result = True
        if node.key > key:
            result = self._insert_as_leaf(node.left, key)
        elif node.key < key:
            result = self._insert_as_leaf(node.right, key)
        else:
            result = False

        if result:
            node.subtree_length += 1   
        return result
             
    def insert_as_root(self, key):
        root = self._insert_as_root(self.root, key)
        if root is None:
            print('Key already present')
        else:
            root.subtree_length = self.root.subtree_length + 1
            self.root = root
            if not self.root.left.key is None:
                self.root.left.subtree_length = self.root.left.left.subtree_length + self.root.left.right.subtree_length + 1
            if not self.root.right.key is None:
                self.root.right.subtree_length = self.root.right.left.subtree_length + self.root.right.right.subtree_length + 1

    def _insert_as_root(self, node: Node, key) -> Node:
        if node.key is None:
            node = Node()
            node.set_key(key)
            node.subtree_length = self.root.subtree_length + 1
            return node

        insertion = None
        if node.key > key:
            insertion = self._insert_as_root(node.left, key)
            if insertion is None:
                return None
            node.left = insertion.right
            insertion.right = node
        if node.key < key:
            insertion = self._insert_as_root(node.right, key)
            if insertion is None:
                return None
            node.right = insertion.left
            insertion.left = node
        
        return insertion

    def delete_by_key(self, key):
        root = self._delete_by_key(self.root, key)
        if root is None:
            print('Key not found')
        else:
            root.subtree_length = self.root.subtree_length - 1
            self.root = root

    def _delete_by_key(self, node: Node, key):
        if node.key is None:
            return None
        
        if node.key > key:
            substitute = self._delete_by_key(node.left, key)
            if substitute is None:
                return None
            substitute.subtree_length = node.left.subtree_length - 1
            node.left = substitute
            return node
        elif node.key < key:
            substitute = self._delete_by_key(node.right, key)
            if substitute is None:
                return None
            substitute.subtree_length = node.right.subtree_length - 1
            node.right = substitute
            return node

        return self._get_substitute(node)
    
    def _get_substitute(self, node: Node):
        if node.left.key is None and node.right.key is None:
            substitute = Node()
        elif not node.left.key is None and not node.right.key is None:
            substitute = node.left.unlink_biggest_child()
            substitute.right =  node.right
            if substitute.key != node.left.key:
                substitute.left = node.left
        else:
            substitute = node.right if node.left.key is None else node.left
        
        return substitute

    def delete_by_index(self, index):
        if index > self.root.subtree_length or index < 1:
            print('Invalid index')
            return
        self._delete_by_index(self.root, index)
    
    def _delete_by_index(self, node: Node, index):
        if node.left is None or index == 0 or index == node.left.subtree_length + 1:
            substitute = self._get_substitute(node)
            node.subtree_length -= 1
            node.key, node.left, node.right = substitute.key, substitute.left, substitute.right
            return
        
        if index > node.left.subtree_length:
            self._delete_by_index(node.right, index - node.left.subtree_length - 1)
        else:
            self._delete_by_index(node.left, index)
        
        node.subtree_length -= 1
        
    def __str__(self) -> str:
        return str(self.root)


if __name__ == '__main__':
    b = BST()
    b.insert_as_root(11)
    print(b)
    b.insert_as_leaf(15)
    print(b)
    b.insert_as_leaf(7)
    print(b)
    b.insert_as_leaf(17)
    print(b)
    b.insert_as_leaf(9)
    print(b)
    b.insert_as_leaf(2)
    print(b)
    b.insert_as_leaf(16)
    print(b)
    b.delete_by_index(3)
    print(b)
    b.delete_by_key(16)
    print(b)
    b.insert_as_root(10)
    print(b)
    b.insert_as_root(8)
    print(b)