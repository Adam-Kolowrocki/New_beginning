table = [
    ['Dorota', 'Wellman', 'journalist']
    ]
print(table)
tuple_1 = (1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5)
print(tuple_1)
set_1 = set(tuple_1)
print(set_1)

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}
print(L_test, T_test, S_test)
print('--------------------------------------------------')
tuple_2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
tuple_3 = ('l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'x', 'y', 'z')
list_1 = []
for i in range(0, len(tuple_2)):
    if i % 2 != 0:
        list_1.append(tuple_2[i])
for i in range(0, len(tuple_3)):
    if i % 2 == 0:
        list_1.append(tuple_3[i])
print('Lista wygląda tak -> ', list_1)
set_2 = set(list_1)
print('Set wygląda tak -> ', set_2)
