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


##Intermediate Set Questions
#21.Write a program to remove duplicate values from a list using a set
# lst=[1,2,3,3,4,5,5,6,7,8,8,9]
# print(list(set(lst)))

#22.Write a program to find common elements between two sets
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# my_set=set1.intersection(set2)
# print(my_set)

# #23.Write a program to find elements present in the first set but not in the second set
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# for i in set1:
#     if i in set1 and i not in set2:
#         print(i)


#24.Write a program to find elements present in the second set but not in the first set
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# print(set1.difference(set2))
# print(set2.difference(set1))

#25.Write a program to merge two sets
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# print(set1.update(set2))
# print(set1)

#26.Write a program to check whether two sets are equal.
# set1={1,2,3,4,5,6,7,8,9}
# set2={1,2,3,4,5,6,7,9}
# if set1==set2:
#     print("both are equal")
# else:
#     print("not equal")

#27.Write a program to find the union of two sets.
# set1={1,2,3,4,5,6,7,8,9}
# set2={21,12,33,14,51,16,27,39}
# set3=set1.union(set2)
# print(set3)

#28.Write a program to find the intersection of two sets
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# set3=set1.intersection(set2)
# print(set3)

#29.Write a program to find the difference of two sets
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# set3=set1.difference(set2)
# print(set3)

#30.Write a program to find the symmetric difference of two sets.
# set1={1,2,3,4,5,6,7,7,8,9}
# set2={12,2,3,4,55,67,87}
# set3=set1.symmetric_difference(set2)
# print(set3)


##Loop Based Set Questions
#31.Write a program to print all elements of a set using a for loop
# set1={1,2,3,4,5,6,7,7,8,9}
# for i in set1:
#     print(i)

#32.Write a program to count total elements in a set without using len().
# set1={1,2,3,4,5,6,7,7,8,9}
# count=0
# for i in set1:
#     count+=1
# print(count)

# #33.Write a program to print only even numbers from a set
##34.Write a program to print only odd numbers from a set
# set1={1,2,3,4,5,6,7,7,8,9}
# for i in set1:
#     if i%2==0:
#       print("even",i)
#     else:
#        print("odd",i)

##35.Write a program to find the sum of all elements in a set.
# set1={1,2,3,4,5,6,7,7,8,9}
# total=0
# for i in set1:
#     total+=i
# print(total)

##36.Write a program to find the maximum element in a set.
# set1={1,2,3,4,55,6,7,7,8,9}
# largest=0
# for i in set1:
#     if i>largest :
#         largest=i
# print(largest)

##37.Write a program to find the minimum element in a set
# set1={1,2,3,4,55,6,7,7,8,9}
# smallest=float('inf')
# for i in set1:
#     if i < smallest:
#         smallest=i
# print(smallest)

##38.Write a program to count positive and negative numbers in a set.
# set1={1,2,-3,4,55,-6,7,8,-9}
# positive =0
# negative=0
# for i in set1:
#     if i > 0:
#         positive+=1
#     else:
#         negative+=1
# print("positive",positive)
# print("negative",negative)

##39.Write a program to print elements greater than 50.
# set1={1,62,-3,4,55,-6,73,82,-9}
# for i in set1:
#     if i >50:
#         print(i)

##40.Write a program to multiply all elements of a set
# set1={1,6,3,4,5,6,3,2,9}
# mult=1
# for i in set1:
#     mult*=i
# print(mult)

##Advanced Set Questions
#1Write a program to check whether one set is a subset of another.
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# if set1.issubset(set2):
#     print("set1 is the subset of set2")
# else:
#     print("set1 is not subset of set2")

#2.Write a program to check whether one set is a superset of another
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# if set1.issuperset(set2):
#     print("set1 is superset of set2")
# else:
#     print("set1 is not superset of set2")


#3.Write a program to check whether two sets are disjoint
# set1 = {1, 2, 3}
# set2 = { 4, 5}
# if set1.isdisjoint(set2):
#     print("both are disjoint")
# else:
#     print("both are not disjoin")

#4.Write a program to create a frozen set (frozenset).
# fs =frozenset({1,2,3,5,6,7,8})
# print(type(fs),fs)
# for i in fs:
#     print(i)

#5.Write a program to compare two sets.
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# if set1==set2:
#     print("both are equal")
# else:
#     print("not equal")


#6.Write a program to convert a list into a set.
# lst=[1,2,3,4,5,6,7,8,9]
# print(set(lst))

#7.Write a program to convert a tuple into a set
# tpl=(1,2,3,4,5,5,6,7,8,9)
# print(set(tpl))

#8.Write a program to convert a string into a set
# s=("1,2,3,4,4,5,5,6").split(",")
# print(set(s))

#9.Write a program to create a set of vowels from a string
# s=("my name is kuldeep")
# v=set()
# for i in s:
#     if i in "aeiouAEIOU":
#         v.add(i)   
# print(v)
    
#10.Write a program to find unique words in a sentence using a set
# s =("my name is kuldeep my name is student").split()
# print(set(s))
