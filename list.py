# Que.1 . Write a program to find the largest and smallest elements in a list.  
# a = [41,42,35,64,86]

# largest = max(a)
# smallest =min(a)

# print("Largest element",largest)
# print("smallest element", smallest)

#Que.2.. Write a program to remove duplicate elements from a list.
# a=[54,65,65,54,36,36]
# print(set(a))

#Que.3.Write a program to reverse a list without using built-in reverse functions. 
# a = [41,42,35,64,86]
# len(a)
# print(len(a))

#Que.4  Write a program to count even and odd numbers in a list. 
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# even = sum(num%2==0 for num in a)
# odd = sum(num%2!=0 for num in a)

# print("even number",even)
# print("odd number",odd)

#Que.5. Write a program to merge two lists and sort the final list. 
# a =  [41,42,35,64,86]
# b =  [54,65,65,54,36,36]
# merge = a + b
# print(merge)

#Que.6 Write a program to find the second largest element in a list.
# b =  [54,65,65,54,36,36]
# b = list(set(b))
# b.sort()
# second_largest = b[-2]
# print("second_largest elemnt:",second_largest)

#Que.7.. Write a program to check whether an element exists in a tuple.
# my_tup=(54,65,65,54,36,36)
# a=int(input("enter your element :"))
# element=a
# if element in my_list:
#     print("element is exists")
# else:
#     print("element not exists")

#Que.8. Write a program to count the occurrence of an element in a tuple. 
# my_tup=(54,65,65,54,36,36)
# element=int(input("enter your element :"))
# count=my_tup.count(element)
# print("The element occurs",count,"times in the tuple.")

#que.9. Write a program to sort a list of tuples based on tuple values.  
# my_list = [(3, 5), (1, 2), (4, 1), (2, 3)]
# sorted_list = print("sorted list of tuples :\n",sorted(my_list))

#Que.10. Write a program to convert a tuple into a list and a list into a tuple. 
# my_list=[35,65,76,45,35,54,65]
# converted_list = tuple(my_list)
# print("Tuple:",converted_list)

# my_tuple=(35,65,76,45,56,76,87)
# converted_tuple = list(my_tuple)
# print("list :", converted_tuple)


#1.Write a program to create a list and print all elements
# l=[2,5,7,8,9]
# i=l
# print(i)

#2.Write a program to print the first and last element of a list.
# my_list=[23,86,95,45,96,35,75,62]
# print(my_list[0])
# print(my_list[-1])

#3.Write a program to find the length of a list.
# my_list=[23,86,95,45,96,35,75,62]
# print(len(my_list))

#4.Write a program to find the largest element in a list.
# my_list=[23,86,95,45,96,35,75,62]
# print(max(my_list))

#5.Write a program to find the smallest element in a list
# my_list=[23,86,95,45,96,35,75,62]
# print(min(my_list))

#6.Write a program to find the sum of all elements in a list
# my_list=[23,86,95,45,96,35,75,62]
# print(sum(my_list))

#7.Write a program to count even and odd numbers in a list
# lst=[23,86,95,45,96,35,75,62]

# even =0
# odd= 0
# for i in lst:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1

# print("even numbers count = ", even)
# print("odd numbers count = ", odd)

#8.Write a program to reverse a list
# lst=[23,86,95,45,96,35,75,62]
# print(lst.reverse())
# print(lst)

#9.Write a program to sort a list in ascending order
# lst=[23,86,95,45,96,35,75,62]
# lst.sort()
# print(lst)

#10.Write a program to sort a list in descending order
# lst=[23,86,95,45,96,35,75,62]
# lst.sort()
# lst.reverse()
# print(lst)

#11.Write a program to add an element using append()
# lst=[23,86,95,45,96,35,75,62]
# lst.append(75)
# print(lst)

#12.Write a program to insert an element at a specific position using insert()
# lst=[23,86,95,45,96,35,75,62]
# lst.insert(2,50)
# print(lst)

#13.Write a program to add multiple elements using extend()
# lst=[23,86,95,45,96,35,75,62]
# lst.extend([56,84,89,65,74])
# print(lst)

#14.Write a program to remove an element using remove()
# lst=[23,86,95,45,96,35,75,62]
# lst.remove(86)
# print(lst)

#15.Write a program to remove the last element using pop()
# lst=[23,86,95,45,96,35,75,62]
# lst.pop(1)
# print(lst)

#16.Write a program to clear all elements from a list using clear()
# lst=[23,86,95,45,96,35,75,62]
# lst.clear()
# print(lst)

#17.Write a program to count how many times an element appears using count()
# lst=[23,86,95,35,96,35,75,62]
# print(lst.count(35))

#18.Write a program to find the index position of an element using index()
# lst=[23,86,95,35,96,35,75,62]
# print(lst.index(35))


#19.Write a program to copy one list into another using copy()
# lst=[23,86,95,35,96,35,75,62]
# print(lst.copy())

#20.Write a program to reverse a list using reverse()
# lst=[23,86,95,35,96,35,75,62]
# print(lst.reverse())
# print(lst)

#21.Write a program to remove duplicate elements from a list
# lst=[23,86,95,35,96,35,75,62]
# d=[]
# for i in lst:
#     if i not in d:
#         d.append(i)
# print(d)
#print(list(set(lst)))

#22.Write a program to search an element in a list
# lst=[23,86,95,35,96,35,75,62]
# n=(int(input("enter your number :")))
# if n in lst:
#     print("number are present")
# else:
#     print("not present")
# print(lst)

#23.Write a program to merge two lists
# lst1=[23,86,95,35,96,35,75,62]
# lst2=[23,84,71,24]
# print(lst1.extend(lst2))
# print(lst1)

#24.Write a program to find common elements between two lists
# lst1=[23,86,95,35,96,35,75,62]
# lst2=[23,84,75,24]
# for i in lst1:
#     if i in lst2:
#         print(i)

#25.Write a program to find the second largest element in a list
# lst=[23,86,95,35,96,35,75,62]
# lst.sort()
# print(lst[-2])

#26.Write a program to separate positive and negative numbers from a list.
# lst=[23,86,-95,35,96,-35,-75,62]
# for i in lst:
#     if i >=0:
#         print("positive",i)
#     else:
#         print("negative",i)

#27.Write a program to create a new list with square of each number.
# lst=[2,3,4,5,6,7,8]
# for i in lst:
#      print(i*i)

#28.Write a program to check whether a list is palindrome or not
# lst=[2,3,4,5,4,3,2]
# lst1 = lst.copy()
# lst1.reverse()

# if lst == lst1:
#     print("palindrome")
# else:
#     print("not palindrome")

#29.Write a program to count positive, negative, and zero elements in a list.
# lst=[23,86,-95,35,96,-35,-75,62]
# posit =0
# nega =0
# zero =0
# for i in lst:
#     if i>0:
#        posit+=1
#     elif i<0:
#         nega+=1
#     else:
#         zero+=1
# print("Positive numbers:", posit)
# print("Negative numbers:", nega)
# print("Zero numbers:", zero)

#30.Write a program to swap first and last elements of a list.
# lst=[23,86,-95,35,96,-35,-75,62]
# lst[0],lst[-1]=lst[-1],lst[0]
# print(lst)