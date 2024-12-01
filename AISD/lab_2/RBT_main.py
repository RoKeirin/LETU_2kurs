from RBT import RBT_func
rbt = RBT_func()
keys = [10,5,15,3,7,18]
for key in keys:
    rbt.insert(key)

import matplotlib.pyplot as plt

j = 30
k = []
k.append(j)
he = []
ma = []
for i in range(j):
    for ii in range(2):
        p = (-1) ** ii
        s = i % 2

        pp = i + ii+1
        j_x = j + p * pp

        #print('\n\nk: ',k)
        rbt = RBT_func()
        for ke in k:
            root = rbt.insert(ke)
        ma.append(len(k))
        print("\nСимметричный обход:")
        rbt.inorder(rbt.root)
        hei = rbt.height_of_tree(rbt.root)
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