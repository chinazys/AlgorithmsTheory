import random
import copy

class Node:
    def __init__(self) -> None:
        self.key = None
        self.left = None
        self.right = None
        self.subtree_length = 0
        self.priority = random.randint(0, 1001)

    def set_key(self, key):
        self.key = key
        self.left = Node()
        self.right = Node()
        self.subtree_length = 1

    def unlink_smallest_child(self):
        node = self

        if node.left.key is None:
            return node
        
        while not node.left.left.key is None:
            node.subtree_length -= 1
            node = node.left
        node.subtree_length -= 1

        unlinked = node.right
        node.left = Node()

        return unlinked
    
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

    def is_undefined(self):
        return self.left is None and self.right is None

    def is_leaf(self):
        return self.left.key is None and self.right.key is None

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

        return left_string + '(' + str(node.key) + '; ' + str(node.subtree_length) + '; ' + str(node.priority) + ')' + right_string
    
    
class RandomBST:
    def __init__(self) -> None:
        self.root = Node()
    
    def get_disbalance_rate(self):
        if self.root.subtree_length < 2:
            return 0
        return self._get_disbalance_rate(self.root)
    
    def _get_disbalance_rate(self, node: Node):
        if node.is_undefined():
            return 0
        return max(0, abs(node.left.subtree_length - node.right.subtree_length) - 1) + self._get_disbalance_rate(node.left) + self._get_disbalance_rate(node.right)

    def insert(self, key):
        try:
            self._insert(self.root, key)
        except:
            print('Key already present')

    def _insert(self, node: Node, key):
        if node.key is None:
            node.set_key(key)
            return
        
        if node.key > key:
            self._insert(node.left, key)
            
            node.subtree_length += 1
                
            if node.left.priority > node.priority:
                self._rotate_left_child(node)
        elif node.key < key:
            self._insert(node.right, key)
            
            node.subtree_length += 1
                
            if node.right.priority > node.priority:
                self._rotate_right_child(node)
        else:
            raise Exception('Same key found')

    def _rotate_left_child(self, node: Node):
        prev_root = copy.deepcopy(node)
        new_root = copy.deepcopy(node.left)
        node.key, node.left = new_root.key, new_root.left
        node.right, node.right.left = prev_root, new_root.right
        node.right.subtree_length = node.right.left.subtree_length + node.right.right.subtree_length + 1
        node.subtree_length = node.left.subtree_length + node.right.subtree_length + 1
        node.priority = new_root.priority

    def _rotate_right_child(self, node: Node):
        prev_root = copy.deepcopy(node)
        new_root = copy.deepcopy(node.right)
        node.key, node.right = new_root.key, new_root.right 
        node.left, node.left.right = prev_root, new_root.left
        node.left.subtree_length = node.left.left.subtree_length + node.left.right.subtree_length + 1
        node.subtree_length = node.left.subtree_length + node.right.subtree_length + 1
        node.priority = new_root.priority

    def search_by_key(self, node: Node, key, delete_found=False) -> Node:
        if node.key is None:
            return False
        
        if node.key > key:
            found_node = self.search_by_key(node.left, key, delete_found)
        elif node.key < key:
            found_node = self.search_by_key(node.right, key, delete_found)
        else:
            if not delete_found:
                return node
            self._delete_as_leaf(node)
            return True
        
        if delete_found and found_node:
            node.subtree_length -= 1
        
        return found_node
    
    def search_by_index(self, node: Node, index, delete_found=False):
        if node.left is None or index == 0 or index == node.left.subtree_length + 1:
            if not delete_found:
                return node
            self._delete_as_leaf(node)
            return True
        
        if index > node.left.subtree_length:
            found_node = self.search_by_index(node.right, index - node.left.subtree_length - 1, delete_found)
        else:
            found_node = self.search_by_index(node.left, index, delete_found)
        
        if delete_found:
            node.subtree_length -= 1

        return found_node
    
    def delete_by_key(self, key):
        node_was_deleted = self.search_by_key(self.root, key, delete_found=True)
        if not node_was_deleted:
            print('Key not found')
            return
        
    def _delete_as_leaf(self, node: Node):
        if not node.left.key is None and not node.right.key is None:
            if node.left.priority > node.right.priority:
                self._rotate_left_child(node)
                if node.right.is_leaf():
                    node.right = Node()
                else:
                    self._delete_as_leaf(node.right)
            else:
                self._rotate_right_child(node)
                if node.left.is_leaf():
                    node.left = Node()
                else:
                    self._delete_as_leaf(node.left)
        elif not node.left.key is None:
            self._rotate_left_child(node)
            if node.right.is_leaf():
                node.right = Node()
            else:
                self._delete_as_leaf(node.right)
        elif not node.right.key is None:
            self._rotate_right_child(node)
            if node.left.is_leaf():
                node.left = Node()
            else:
                self._delete_as_leaf(node.left)
        else:
            new_node = Node()
            node.key, node.priority = new_node.key, new_node.priority 

        node.subtree_length -= 1

    def delete_by_index(self, index):
        if index > self.root.subtree_length or index < 1:
            print('Invalid index')
            return
        self.search_by_index(self.root, index, delete_found=True)
        
    def __str__(self) -> str:
        return str(self.root)


if __name__ == '__main__':
    b = RandomBST()
    b.insert(11)
    print(b)
    b.insert(17)
    print(b)
    b.insert(7)
    print(b)
    b.insert(15)
    print(b)
    b.insert(18)
    print(b)
    b.insert(9)
    print(b)
    b.insert(2)
    print(b)
    b.insert(16)
    print(b)
    b.delete_by_index(3)
    print(b)
    b.delete_by_key(16)
    print(b)
    b.insert(10)
    print(b)
    b.delete_by_key(10)
    print(b)
    print(b.get_disbalance_rate())