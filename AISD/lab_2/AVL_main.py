from AVL import AVL_func

import matplotlib.pyplot as plt
avl = AVL_func()
root = None
keys = [10,5,15,3,7,18]
for key in keys:
    #print("Обход в ширину:", avl.level_order_traversal(root))
    #print(f"insert: {key}")
    root = avl.insert(root,key)

j = 300
k = []
k.append(j)
he = []
ma = []
for i in range(j):
    for ii in range(2):
        p = (-1) ** ii
        s = i % 2

        pp = i + ii
        j_x = j + p * pp

        # print('\n\nk: ',k)
        avl = AVL_func()
        root = None
        for key in k:
            root = avl.insert(root, key)
        ma.append(len(k))
        #print("Симметричный обход:")
        #avl.inorder(root)
        hei = avl.height_of_tree(root)
        #print("Высота дерева:", hei)
        k.append(j_x)
        he.append(hei)
# print(ma)
# print(he)
# Создание графика
plt.plot(ma, he)

# Добавление заголовка и меток осей
plt.title('Простой график')
plt.xlabel('x')
plt.ylabel('y')

# Показать график
plt.grid()
plt.show()