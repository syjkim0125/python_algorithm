# Exercise Address https://www.acmicpc.net/problem/5639
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insertValue(self.root, data)
        return self.root is not None

    def _insertValue(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insertValue(node.left, data)
            else:
                node.right = self._insertValue(node.right, data)

        return node

    def post_order_traversal(self):
            def _post_order_traversal(root):
                if root is None:
                    pass
                else:
                    _post_order_traversal(root.left)
                    _post_order_traversal(root.right)
                    print(root.data)
            _post_order_traversal(self.root)


if __name__ == "__main__":

    array = list(map(int, input().split()))

    bst = BinarySearchTree()
    for x in array:
        bst.insert(x)
    bst.post_order_traversal()
