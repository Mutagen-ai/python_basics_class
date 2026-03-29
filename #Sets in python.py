#Sets in python
#Creating a set
fruits = {"apple", "banana", "orange"}
print(fruits)
#No duplicates
numbers = {1,2,2,3,3,3,4,4,5,6,7,6}
print(numbers)
#Creating an empty set
empty_set ={}
print(empty_set)

#Add items in set
fruits = {"apple", "banana", "orange"}
fruits.add("grape")
print(fruits)

#Remove items in a set
fruits = {"apple", "banana", "orange"}
fruits.remove("banana")
print(fruits)

#Check if items exist in a set
fruits = {"banana", "orange", "mango"}
print("apple" in fruits)
print("banana" in fruits)

#Iterate through a set/Loop
fruits ={"apple", "banana", "orange"}
for fruit in fruits:
    print(fruit)

#Set Operations
#Union
set1 = {1,2,3,4}
set2 = {4,3,5, 6}
print(set1.union(set2))

#Intersection in set
print(set1.intersection(set2))

#Difference in set
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))


#Programming puzzle
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)
my_list.append(4)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)