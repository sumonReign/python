# cars = ["Volvo", "Mercedes", "Toyota"]
# for car in cars:
#     print(car)

# countryName = "Bangladesh"
# for i in countryName:
#     if i=='d': break;
#     print(i)

#print numbers untill the user input 0
# num = int(input("Enter your number as you wish: "))
# while num != 0:
#     print(f"You have entered {num}")
#     num = int(input("Enter the number: "))
# print("End")


#else can be used with while 
# counter = 0
# while counter  <  2:
#     print('This is inside loop')
#     counter = counter + 1
# else:
#     print('This is inside else block')


#fibonacci sequence
# def fibonacci_less_than(n):
#     a , b = 0, 1
#     fibonacci_sequence = []
#     while a < n:
#         fibonacci_sequence.append(a)
#         a , b = b, a+b
#     return fibonacci_sequence
# fibonacci_less_than(20)

#Python number, Random
import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print((random.random()))
