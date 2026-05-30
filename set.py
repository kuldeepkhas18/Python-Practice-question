#1.Write a program to create a set and print all elements.
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# for i in my_set:
#    print(i,end=",")


#2.Write a program to find the length of a set
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# print(len(my_set))

#3.Write a program to add an element to a set
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# print(my_set.add(10))
# print(my_set)

#4.Write a program to add multiple elements using update()
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# my_set.update([10,11,12,13])
# print(my_set)

#5.Write a program to remove an element using remove()
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# my_set.remove(3)
# print(my_set)

#6.Write a program to remove a element using discard()
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# my_set.discard(5)
# print(my_set)

#7.Write a program to remove a random element using pop()
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# my_set.pop()
# print(my_set)

#8.Write a program to clear all elements from a set
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# my_set.clear()
# print(my_set)

#9.Write a program to check whether an element exists in a set
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# n = int(input("enter your name :"))
# if n in my_set:
#     print("exist")
# else:
#     print("not exist")

#10.Write a program to print all elements of a set using a loop
# my_set={ 1,2,3,4,5,6,7,7,8,9}
# for i in my_set:
#     print(i)

##Set Method Practice Questions
#questions?
# Write a program using add() method.
# Write a program using update() method.
# Write a program using remove() method.
# Write a program using discard() method.
# Write a program using pop() method.
# Write a program using clear() method.
# Write a program using copy() method.
# Write a program using union() method.
# Write a program using intersection() method.
# Write a program using difference() method.

#answer
#my_set={ 1,2,3,4,5,6,7,7,8,9}
# my_set.add(10)
# print(my_set)

# my_set.update([10,11])
# print(my_set)

# my_set.remove(9)
# print(my_set)

# my_set.discard(5)
# print(my_set)

# my_set.pop()
# print(my_set)

# my_set.clear()
# print(my_set)

# new_set=my_set.copy()
# print(my_set)
# print(new_set)

# my_set2={1,2,3,11,12,13}
# set1 =my_set.union(my_set2)
# print(set1)

# my_set2={1,2,3,11,12,13}
# set1 =my_set.intersection(my_set2)
# print(set1)

# my_set2={1,2,3,11,12,13}
# set1 =my_set.difference(my_set2)
# print(set1)
