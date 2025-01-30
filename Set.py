summer_fruit = {"Mango", "Lichi", "Jackfruit", "Banana", "Jam"}
winter_fruit = ["Lemon", "Guava", "Pepeya" , "Banana"]
summer_fruit.update(winter_fruit)
print(summer_fruit)

#Python enumarate
list1 = ["Lima", "Apon", "Jiya", "Alal"]
for count, name in enumerate(list1):
    print(count, name)

grocery = ["lemon", "rice", "Potato"]
for count, item in enumerate(grocery, 100):
  print(count, item)


# Program to get a substring from the given string 

py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3) 
print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn


#my own creation
myStrings = "Bangladesh"
print(len(myStrings))
sliced_object = slice(2,9,3)
print(myStrings[sliced_object])

