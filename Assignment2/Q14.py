d1 = {"a": 100,
      "b": 200,
      "c": 300}

list_1 = list()

for item in d1:
    list_1.append(d1[item])

for element in list_1:
    if element != 200:
        pass
    else:
        print("The value of 200 exists in given dictionary.")
