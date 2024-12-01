class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1  # Для AVL-дерева

class AVL_func:
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Обновить высоту узла предка
        root.height = 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))

        # 3. Получить баланс
        balance = self.get_balance(root)

        # Если дерево не сбалансировано, выполняем повороты
        # Левый левый случай
        if balance > 1 and key < root.left.val:
            return self.rotate_right(root)

        # Правый правый случай
        if balance < -1 and key > root.right.val:
            return self.rotate_left(root)

        # Левый правый случай
        if balance > 1 and key > root.left.val:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Правый левый случай
        if balance < -1 and key < root.right.val:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete_node(self, root, key):
        # 1. Выполняем стандартное удаление узла
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Узел с одним ребенком или без детей
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Узел с двумя детьми: получить порядокный преемник (наименьшее в правом поддереве)
            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)

        # 2. Обновить высоту узла предка
        root.height = 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))

        # 3. Получить баланс
        balance = self.get_balance(root)

        # Если дерево не сбалансировано, выполним необходимые повороты
        # Левый левый случай
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Левый правый случай
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Правый правый случай
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Правый левый случай
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root



    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height_of_tree(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        bal = self.height_of_tree(node.left) - self.height_of_tree(node.right)
        #print(f"balanced:{bal}")
        # return self.height_of_tree(node.left) - self.height_of_tree(node.right)
        return bal

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Выполняем поворот
        y.left = z
        z.right = T2

        # Обновляем высоты
        z.height = 1 + max(self.height_of_tree(z.left), self.height_of_tree(z.right))
        y.height = 1 + max(self.height_of_tree(y.left), self.height_of_tree(y.right))

        # Возвращаем новый корень
        #print("rotate_left")
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Выполняем поворот
        y.right = z
        z.left = T3

        # Обновляем высоты
        z.height = 1 + max(self.height_of_tree(z.left), self.height_of_tree(z.right))
        y.height = 1 + max(self.height_of_tree(y.left), self.height_of_tree(y.right))
        #print("rotate_right")
        # Возвращаем новый корень
        return y

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
# avl = AVL_func()
# root = None
# keys = [10,5,15,3,7,18]
# for key in keys:
#     #print("Обход в ширину:", avl.level_order_traversal(root))
#     #print(f"insert: {key}")
#     root = avl.insert(root,key)
# print("Обход в ширину:", avl.level_order_traversal(root))
# print("Преордерный обход:")
# avl.preorder(root)
#
# print("\nСимметричный обход:")
# avl.inorder(root)
#
# print("\nПостордерный обход:")
# avl.postorder(root)
#
# print("Обход в ширину:", avl.level_order_traversal(root))
#
# print("Изначальное дерево (в порядке возрастания):")
# avl.inorder(root)
# print("\nВысота дерева:",avl.height_of_tree(root))
# #print("\n\nПоиск :", bst.Search(10))  # True
# print("\nУдаляем узел 20:")
# root = avl.delete_node(root, 20)
# avl.inorder(root)
# print("\nВысота дерева:",avl.height_of_tree(root))
#
# keyy=50
# result = avl.search(root, keyy)
# print(f"Узел {keyy}: ","найден" if result else "не найден")
#
# print("\nУдаляем узел 30:")
# root = avl.delete_node(root, 30)
# avl.inorder(root)
# print("\nВысота дерева:",avl.height_of_tree(root))
#
# print("\nУдаляем узел 50:")
# root = avl.delete_node(root, 50)
# avl.inorder(root)
# print("\nВысота дерева:",avl.height_of_tree(root))
# keyy=50
# result = avl.search(root, keyy)
# print(f"Узел {keyy}: ","найден" if result else "не найден")
# print("Обход в ширину:", avl.level_order_traversal(root))
