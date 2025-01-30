my_list = ['B', 'A', 'N', 'G', 'L', 'A', 'D', 'E' ,'S', 'H']
print(my_list[0 : 3]) # B , A , N
print(my_list[2 : 5]) # N, G, L
print(my_list[-4 : ]) # D, E, S, H
print(my_list[-4 : -2 ])

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)

# get a list with items from index 5 to last
print("my_list[5: ] =", my_list[5: ])

# get a list from the first item to index -5
print("my_list[: -4] =", my_list[: -4])

# omitting both start and end index
# get a list from start to end items
print("my_list[:] =", my_list[:])


# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)

list1 = [2,5,3,7,8,5,9,7,5,4,]
print(list1.reverse())
print(list1.sort())
print(list1.count(5))

