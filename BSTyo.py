
class node:
    def __init__(self, val=None):
        self.val = val
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, cur_node):
        if val < cur_node.val:
            if cur_node.left_child == None:
                cur_node.left_child = node(val)
            else:
                self._insert(val, cur_node.left_child)
        elif val > cur_node.val:
            if cur_node.right_child == None:
                cur_node.right_child = node(val)
            else:
                self._insert(val, cur_node.right_child)
        else:
            print ("Value already in tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.val))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def search(self, val):
        if self.root != None:
            return self._search(val, self.root)
        else:
            return False

    def _search(self, val, cur_node):
        if val == cur_node.val:
            return True
        elif val<cur_node.val and cur_node.left_child!=None:
            return self._search(val, cur_node.left_child)
        elif val>cur_node.val and cur_node.right_child != None:
            return self._search(val, cur_node.right_child)
        return False

def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)



tree.print_tree()

print ("Tree height: "+str(tree.height()))

print (tree.search(10))
print (tree.search(30))
