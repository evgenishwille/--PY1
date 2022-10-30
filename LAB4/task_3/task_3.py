def delete(list, index):
    list.pop(index)
    return list

list_1 = [0, 0, 1, 2]      #index = 0
list_2 = [0, 1, 1, 2, 3]    #index = 1
list_3 = [0, 1, 2, 3, 4, 4] #index = none


print(delete(list_1, 0))
print(delete(list_2, 1))
print(delete(list_3, -1))
