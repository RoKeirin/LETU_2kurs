class Node:
    def __init__(self, key, color="red", left=None, right=None, parent=None):
        self.key = key
        self.color = color  # "red" or "black"
        self.left = left
        self.right = right
        self.parent = parent


class RBT_func:
    def __init__(self):
        self.TNULL = Node(key=None, color="black")  # Sentinel node
        self.root = self.TNULL

    def search(self, key):
        current = self.root
        while current != self.TNULL and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key=key, color="red", left=self.TNULL, right=self.TNULL)
        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, key):
        node = self.search(key)
        if node == self.TNULL:
            return  # Node not found

        y = node
        y_original_color = y.color
        if node.left == self.TNULL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.TNULL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == "black":
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def preorder(self, root):
        if root is not None:
            if root.key == None:
                print('', end='')
            else:
                print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            if root.key == None:
                print('', end='')
            else:
                print(root.key, end=' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            if root.key==None:print('',end='')
            else: print(root.key, end=' ')
    def level_order_traversal(self, root):
        if root is None:
            return []

        result = []
        queue = [root]  # Используем список в качестве очереди

        while queue:
            current = queue.pop(0)  # Удаляем первый элемент из списка
            result.append(current.key)

            # Добавляем дочерние элементы в конец списка
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        result1 = []
        for i in result:
            if i!=None: result1.append(i)
        return result1
    def height_of_tree(self, node):
        if node is None:
            return -1  # Возвращаем -1 для учета высоты при наличии узла
        else:
            left_height = self.height_of_tree(node.left)
            right_height = self.height_of_tree(node.right)
            return max(left_height, right_height) + 1

# # Пример использования
# rbt = RBT_func()
# keys = [10,5,15,3,7,18]
# for key in keys:
#     rbt.insert(key)
#
#
# print("Inorder traversal after insertions:")
# rbt.inorder(rbt.root)
# print("Обход в ширину:", rbt.level_order_traversal(rbt.root))
#
#
# print("\nInorder traversal after deletion:")
# rbt.inorder(rbt.root)
# print("Обход в ширину:", rbt.level_order_traversal(rbt.root))
# print("Преордерный обход:")
# rbt.preorder(rbt.root)
#
# print("\nСимметричный обход:")
# rbt.inorder(rbt.root)
#
# print("\nПостордерный обход:")
# rbt.postorder(rbt.root)
#
# print("\nВысота дерева:",rbt.height_of_tree(rbt.root))