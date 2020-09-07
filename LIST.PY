##Take choice from user and perform particular operation on array (1. Copy, 2. Remove duplicates, 3. Delete at kth index, 4. Search an item, 5. Display contents).
global array
array = list(map(int, input("enter elements by giving space for array").strip().split(' ')))
q = 0


def Remove_duplicates(array):
    array = list(set(array))
    return array


def Delete_at_kth_index():
    z = int(input("enter index to delete"))
    if z < len(array):
        array.pop(z)
    return array


class Search_an_item(object):
    o = int(input("enter the number to search"))
    z = array.count(o)
    while z > 0:
        for i in range(len(array)):
            if array[i] == o:
                print(i)
                z -= 1


while q == 0:
    k = int(input(
        "enter the respective number for the operation\n 1. Copy\n 2. Remove duplicates\n 3. Delete at kth index\n 4. "
        "Search an item\n 5. Display contents\n"))
    if k == 1:
        print("coppied")
    elif k == 2:
        print(Remove_duplicates(array))
    elif k == 3:
        print(Delete_at_kth_index())
    elif k == 4:
        Search_an_item()
    elif k == 5:
        print(array)
    q = int(input("enter 0 to another operation \n for exit any number"))
	

