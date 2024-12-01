class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST_func:
    # def __init__(self):
    #     self.root = None

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def delete_node(self, root, key):
        # Базовый случай: если дерево пустое
        if root is None:
            return root

        # Рекурсивно ищем узел для удаления
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Узел с единственным дочерним узлом или без дочерних узлов
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Узел с двумя дочерними узлами: получаем наименьшее значение из правого поддерева (или наибольшее из левого)
            min_larger_node = self.get_min_value_node(root.right)
            root.val = min_larger_node.val
            root.right = self.delete_node(root.right, min_larger_node.val)

        return root

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def preorder(self, root):
        if root is not None:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')
    def height_of_tree(self, node):
        if node is None:
            return -1  # Возвращаем -1 для учета высоты при наличии узла
        else:
            left_height = self.height_of_tree(node.left)
            right_height = self.height_of_tree(node.right)
            return max(left_height, right_height) + 1

    def level_order_traversal(self, root):
        if root is None:
            return []

        result = []
        queue = [root]  # Используем список в качестве очереди

        while queue:
            current = queue.pop(0)  # Удаляем первый элемент из списка
            result.append(current.val)

            # Добавляем дочерние элементы в конец списка
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

#
#
# bst = BST_func()
# root = None
# keys = [50, 30, 20, 35, 47, 23, 55]
# keys = [10,5,15,3,7,18]
#
# for key in keys:
#     root = bst.insert(root, key)
# print("Обход в ширину:", bst.level_order_traversal(root))
# print("Изначальное дерево (в порядке возрастания):")
# bst.inorder(root)
# print("\nВысота дерева:",bst.height_of_tree(root))
# #print("\n\nПоиск :", bst.Search(10))  # True
# print("\nУдаляем узел 20:")
# root = bst.delete_node(root, 20)
# bst.inorder(root)
# print("\nВысота дерева:",bst.height_of_tree(root))
#
# keyy=50
# result = bst.search(root, keyy)
# print(f"Узел {keyy}: ","найден" if result else "не найден")
#
# print("\nУдаляем узел 30:")
# root = bst.delete_node(root, 30)
# bst.inorder(root)
# print("\nВысота дерева:",bst.height_of_tree(root))
#
# print("\nУдаляем узел 50:")
# root = bst.delete_node(root, 50)
# bst.inorder(root)
# print("\nВысота дерева:",bst.height_of_tree(root))
# keyy=50
# result = bst.search(root, keyy)
# print(f"Узел {keyy}: ","найден" if result else "не найден")

#
# print("Обход в ширину:", bst.level_order_traversal(root))
# print("Преордерный обход:")
# bst.preorder(root)
#
# print("\nСимметричный обход:")
# bst.inorder(root)
#
# print("\nПостордерный обход:")
# bst.postorder(root)