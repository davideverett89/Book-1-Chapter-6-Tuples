zoo = ("Kangaroo", "Bear", "Giraffe", "Lion", "Tiger", "Penguin", "Seal", "Hyena", "Pig", "Snake", "Elephant")
animalIndex = zoo.index("Lion")
print(animalIndex)

animal_to_find = "Kangaroo"
if animal_to_find in zoo:
    print('This animal is in your zoo!')
else:
    print('Animal was not found')

(animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10, animal11) = zoo

print(animal1)
print(animal2)
print(animal3)
print(animal4)
print(animal5)
print(animal6)
print(animal7)
print(animal8)
print(animal9)
print(animal10)
print(animal11)

tuple_to_list = list(zoo)
print(tuple_to_list)

tuple_to_list.extend(["Parrot", "Badger", "Beaver"])
print(tuple_to_list)
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)