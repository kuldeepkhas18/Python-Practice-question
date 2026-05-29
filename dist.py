#1.Write a program to create a dictionary and print it.
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std)

#2.Write a program to access a value using a key.
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std["age"])

#3.Write a program to print all keys of a dictionary
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std.keys())

#4.Write a program to print all values of a dictionary.
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std.values())

#3.Write a program to print all key-value pairs.
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std)

#4.Write a program to find the length of a dictionary
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(len(std))

#5.Write a program to check whether a key exists in a dictionary
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# if "name" in std:
#     print("key exists")
# else:
#     print("key not exists")

#6.Write a program to add a new key-value pair to a dictionary
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# std["city"]="morena"
# print(std)

#7.Write a program to update the value of an existing key
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# std.update({"age": 23})
# print(std)

#8.Write a program to remove a key-value pair from a dictionary
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std.pop("sub"))
# print(std)

#9.Write a program using keys() method.
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(std.keys())
# print(std.values())
# print(std.items())
# print(std.get('sub'))
# std.update({'age':23})
# print(std)
# print(std.pop("sub"))
# print(std)
# std.popitem()
# print(std)
# print(std.clear())
# print(std)
# new_std=std.copy()
# print(new_std)
# std.setdefault("age",23)
# print(std)

#10.Write a program to count the number of keys in a dictionary
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }
# print(len(std))

#11.Write a program to merge two dictionaries
# std = {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
# }

# info={
#     "add":"saraychola",
#     "city":"morena",
#     "country":"india"
# }

# std.update(info)
# print(std)

#12.Write a program to create a dictionary of squares from 1 to 10
# std = {}
# for keys in range(1,11):
#     square = keys*keys
#     std[keys] = square
# print(std)

#13.Write a program to find the key with the maximum value.
# dist={
#     1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100
# }
# print(max(dist,key=dist.get),":",max(dist.values()))

#14.Write a program to find the key with the minimum value
# dist={
#     1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100
# }
# print(min(dist,key=dist.get),":",min(dist.values()))

#15.Write a program to sum all values in a dictionary.
# dist={
#     1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100
# }
# print(sum(dist.values()))

#16.Write a program to remove duplicate values from a dictionary.
# dist={
#     1: 1, 2: 4, 3: 100, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100
# }
# new_dict = {}
# for k,v in dist.items():
#     if v not in new_dict.values():
#         new_dict[k] = v
# print(new_dict)

#17.Write a program to sort a dictionary by keys.
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# print(sorted(dist))

#18.Write a program to sort a dictionary by values
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# print(sorted(dist.values()))

#19.Write a program to reverse key-value pairs
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# new={}
# for k,v in dist.items():
#     new[v]=k
# print(new)

#31.Write a program to print all keys using a loop.
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# for i in dist.keys():
#      print(i)

#32.Write a program to print all values using a loop
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# for i in dist.values():
#     print(i,end=",")

#33.Write a program to print all key-value pairs using a loop
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# for k,v in dist.items():
#     print(k,":",v)

#Write a program to count total items using a loop.
# dist={
#     5: 25,
#     2: 4,
#     1: 1,
#     4: 16,
#     3: 9
# }
# count=0
# for i in dist.items():
#     count+=1
# print(count)

#Write a program to print only keys whose values are greater than 50
# dist={
#     5: 75,
#     2: 4,
#     1: 95,
#     4: 62,
#     3: 9
# }

# for k,v in dist.items():
#     if v>50:
#         print(k,":",v)
   
#Write a program to find the largest value using a loop
# dist={
#     5: 75,
#     2: 4,
#     1: 95,
#     4: 62,
#     3: 9
# }
# largest=0
# for k,v in dist.items():
#     if v >largest:
#        largest=v
#        print(k,":",largest)

# smallest=float('inf')
# kes=0
# for k,v in dist.items():
#     if v < smallest:
#         smallest=v
#         key=k
# print(k,":", smallest) 

#Write a program to count even and odd values in a dictionary.
# dist={
#     5: 75,
#     2: 4,
#     1: 95,
#     4: 62,
#     3: 9
# }
# key=0
# even=0
# odd =0
# for k,v in dist.items():
#     if v%2==0:
#         print("even",k,":",v)
#         #even+=v
#         key+=1
#         even+=1
#     else:
#         print("odd",k,":",v)
#         #odd+=v
#         odd+=1
# print(even)
# print(odd)

#41.Write a program to create a nested dictionary
# dist= {
#     "std1" : {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
#    },
#    "std2": {
#     "name" : "radhey",
#     "age" : "23",
#     "sub" : "science",
#     "marks" :"76"
#    }
# }

# print(dist)

#42.Write a program to access values from a nested dictionary
# dist= {
#     "std1" : {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
#    },
#    "std2": {
#     "name" : "radhey",
#     "age" : "23",
#     "sub" : "science",
#     "marks" :"76"
#    }
# }

# print(dist["std1"]["name"])
# print(dist["std2"]["marks"])

#Write a program to print all nested dictionary items
# dist= {
#     "std1" : {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
#    },
#    "std2": {
#     "name" : "radhey",
#     "age" : "23",
#     "sub" : "science",
#     "marks" :"76"
#    }
# }
# for dist,details in dist.items():
#     print(dist)
#     for k,v in details.items():
#         print(k,":",v) 
#     print()

#Write a program to count total items in a nested dictionary
# dist= {
#     "std1" : {
#     "name" : "kuldeep",
#     "age" : "21",
#     "sub" : "math",
#     "marks" :"87"
#    },
#    "std2": {
#     "name" : "radhey",
#     "age" : "23",
#     "sub" : "science",
#     "marks" :"76"
#    }
# }
# count=0
# for dist,details in dist.items():
#     for i in details.items():
#         count+=1
# print(count)


#Write a program to find the sum of all values in a nested dictionary
# dist={
#     "dist1": {
#     5: 25,
#     2: 4,
#     1: 100,
#     4: 16,
#     3: 9
#     },

#     "dist2": {
#     6: 22,
#     8: 43,
#     7: 18,
#     9: 19,
#     11: 79
#     }
# }
# total=0
# for details in dist.values():
#         total += sum(details.values())

# print(total)

#Write a program to convert two lists into a dictionary.
# keys = ["name", "age", "city"]
# values = ["Kuldeep", 21, "Morena"]
# d=dict(zip(keys,values))
# print(d)

#Write a program to create a dictionary from user input
# dist = {}
# n = int(input("how many item do you want to enter? :"))
# for i in range(n):
#     key=input("enter key: ")
#     value=input("enter value: ")
#     dist[key]= value
# print(dist)

#Write a program to count the frequency of characters in a string using a dictionary
# s = input("enetr your value :")
# dist={}
# for i in s:
#     dist[i]=s.count(i)
# print(dist)

# #Write a program to count the frequency of words in a sentence using a dictionary.
# s=input("enter your value :")
# words=s.split()
# dict={}
# for i in words:
#     dict[i]= words.count(i)
# print(dict)

#Write a program to create a student record using a dictionary (name, roll no, marks, branch)
dict={}
n=int(input("how many item do you want : ? "))
for i in range(n):
   key=input("enter your key :")
   values=input("enter your values :")
   dict[key]=values
print(dict)