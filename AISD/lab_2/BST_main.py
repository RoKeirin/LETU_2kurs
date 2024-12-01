from BSTree import BST_func
import matplotlib.pyplot as plt

j = 20
k = []
k.append(j)
he = []
ma = []
for i in range(j):
    for ii in range (2):
        p = (-1)**ii
        s = i%2
        pp=i+ii
        j_x = j + p*pp

        #print('\n\nk: ',k)
        bst = BST_func()
        root = None
        for key in k:
            root = bst.insert(root, key)
        ma.append(len(k))
        print("Симметричный обход:")
        bst.inorder(root)
        hei=bst.height_of_tree(root)
        print("Высота дерева:", hei)
        k.append(j_x)
        he.append(hei)
print(ma)
print(he)



# Создание графика
plt.plot(ma, he)

# Добавление заголовка и меток осей
plt.title('Простой график')
plt.xlabel('x')
plt.ylabel('y')

# Показать график
plt.grid()
plt.show()
