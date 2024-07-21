my_dict={str("Victor"): int(1992), str("Julia"): int(1992), str("Anna"): int(2015)}
print(my_dict)
print(my_dict.get("Victor"))
print(my_dict.get("Masha", "Такого ключа нет"))
my_dict.update({str("Sasha") : int(1989), str("Sveta") : int(1967)})
a=my_dict.pop("Anna")
print(a)
print(my_dict)



my_set={str("V"), int(1), int(1), int(3), int(3), str("V"), int(2)}
print(my_set)
my_set.add(int(100)), my_set.add(str("J"))
my_set.remove(1)
print(my_set)
