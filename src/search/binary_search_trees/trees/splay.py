import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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

class SplayTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, parent=None):
        if parent == None:
            parent = self.root
        if parent == None:
            self.root = Node(key)
        elif key < parent.key:
            if parent.left == None:
                parent.left = Node(key)
            else:
                self.insert(key, parent.left)
        else:
            if parent.right == None:
                parent.right = Node(key)
            else:
                self.insert(key, parent.right)

    def find(self, key, height_cnt=1, node=None, p=None, g=None, gg=None):
        if node == None:
            node = self.root
        if node == None:
            return None, height_cnt
        elif key == node.key:
            if p != None:
                if g == None:
                    self.rotate_up(node, p, g)
                elif g.left == p and p.left == node or g.right == p and p.right == node:
                    self.rotate_up(p, g, gg)
                    self.rotate_up(node, p, gg)
                else:
                    self.rotate_up(node, p, g)
                    self.rotate_up(node, g, gg)
            return node, height_cnt
        elif key < node.key:
            if node.left != None:
                leftrv, height_cnt = self.find(key, height_cnt + 1, node.left, node, p, g)
                if leftrv != None:
                    return leftrv,  height_cnt
        elif key > node.key:
            if node.right != None:
                rightrv, height_cnt = self.find(key, height_cnt + 1, node.right, node, p, g)
                if rightrv != None:
                    return rightrv, height_cnt
        return None, height_cnt

    def rotate_up(self, node, parent, gp=None):
        if node == parent.left: 
            parent.left = node.right
            node.right = parent
            if (self.root == parent):
                self.root = node
        elif node == parent.right:
            parent.right = node.left
            node.left = parent
            if (self.root == parent):
                self.root = node
        else:
            print("This is impossible")

        if (gp != None):
            if (gp.right == parent):
                gp.right = node
            elif (gp.left == parent):
                gp.left = node

    def __str__(self) -> str:
        return str(self.root)
    
if __name__ == '__main__':
    b = SplayTree()
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