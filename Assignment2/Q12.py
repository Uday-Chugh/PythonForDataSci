list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

sublist_6000 = list1[2][2]

index_6000 = sublist_6000.index(6000)
sublist_6000.insert(index_6000 + 1, 7000)
print(list1)
