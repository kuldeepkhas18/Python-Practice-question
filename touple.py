#1.Write a program to create a tuple and print all elements
# tpl =(51,42,63,28,95,65,75,62)
# print(type(tpl))

#2.Write a program to find the length of a tuple
# tpl =(51,42,63,28,95,65,75,62)
# print(len(tpl))

#3.Write a program to access the first and last element of a tuple.
# tpl =(51,42,63,28,95,65,75,62)
# print(tpl[0])
# print(tpl[7])

#4.Write a program to check whether an element exists in a tuple
# tpl =(51,42,63,28,95,65,75,62)
# print(28 in tpl)

#5.Write a program to count how many times an element appears in a tuple.
# tpl =(51,42,63,28,95,65,75,62)
# print(tpl.count(28))

#6.Write a program to find the index position of an element in a tuple
# tpl =(51,42,63,28,95,65,75,62)
# print(tpl.index(95))

#7.Write a program to print all elements of a tuple using loop.
# tpl =(51,42,63,28,95,65,75,62)
# for i in tpl:
#     print(i)

#8.Write a program to find the maximum,,min and sum element in a tuple.
# tpl =(51,42,63,28,95,65,75,62)
# print(max(tpl))
# print(min(tpl))
# print(sum(tpl))

#9.Write a program to convert list into tuple
# lst =[51,42,63,28,95,65,75,62]
# print(tuple(lst))
# print(list(lst))

#10.Write a program to concatenate two tuple
# tpl1 =(51,42,63,28,95,65,75,62)
# tpl2 =(62,53,95,76)
# print(tpl1 +tpl2)

#11.Write a program to repeat tuple elements using * operator
# tpl1 =(51,42,63,28,95,65,75,62)
# print(tpl1*3)

#12.Write a program to slice a tuple
# tpl=(51,42,63,28,95,65,75,62)
# print(tpl[1:4])

#13.Write a program to reverse a tuple
# tpl=(51,42,63,28,95,65,75,62)
# print(tpl[::-1])

#14.Write a program to sort tuple elements
#tpl=(51,42,63,28,95,65,75,62)
# lst=list(tpl)
# list.sort(lst)
# lst=tuple(lst)
# print(lst)

#print(tuple(sorted(tpl)))

#21.Write a program to find even and odd numbers in a tuple
# tpl=(51,42,63,28,95,65,75,62)
# for i in tpl:
#     if i%2==0:
#         print("even number",i)
#     else:
#         print("odd number",i)

#22.Write a program to count positive and negative numbers in a tuple
# tpl=(-65,-35,86,43,-74,-43,78,62)
# positive=0
# negative=0
# for i in tpl:
#     if i>0:
#         print("positive",positive)
#         positive+=1
#     else:
#         print("negative",negative)
#         negative+=1
# print(positive)
# print(negative)

#23.Write a program to remove duplicate elements from a tuple
# tpl=(51,42,63,28,95,62,75,62)
# print(tuple(set(tpl)))

#24.Write a program to find the second largest element in a tuple
# tpl=(51,42,63,28,95,62,75,62)
# print(tuple(sorted(tpl)))
# print(tpl[-3])

#25.Write a program to merge two tuples
# tpl1=(51,42,63,28,95,62,75,62)
# tpl2=(-65,-35,86,43,-74,-43,78,62)
# tpl=tpl1+tpl2
# print(tpl)

#26.Write a program to check whether a tuple is palindrome or not.
# tpl=(45,65,45,56)
# if tpl==tpl[::-1]:
#     print("pelindorme")
# else:
#     print("not")

#27.Write a program to swap first and last elements of a tuple
# tpl=(51,42,63,28,95,62,75,62)
# lst=list(tpl)
# lst[0], lst[-1] = lst[-1],lst[0]
# tpl=tuple(lst)
# print(tpl)

#28.Write a program to create a new tuple with square of each number.
# tpl=(51,42,63,28,95,62,75,62)
# square=0
# for i in tpl:
#     print(i*i,)
#     square+=i
# print(square)

#29.Write a program to find common elements between two tuples.
# tpl1=(51,42,63,28,95,62,75,62)
# tpl2=(54,42,64,28,98,61,72,62)

# for i in tpl1:
#     if i in tpl2:
#         print()

#30.Write a program to search an element in a tuple
# tpl1=(51,42,63,28,95,62,75,62)
# print(tpl1.index(42))

#31.Write a program to print tuple elements using for and while loop
# tpl=(51,42,63,28,95,62,75,62)
# # for i in tpl:
# #     print(i)
# i=0
# while i < len(tpl):
#     print(tpl[i])
#     i+=1

#32.Write a program to print only even elements from a tuple
# tpl=(51,42,63,28,95,62,75,62)
# for i in tpl:
#     if i%2==0:
#      print(i)

#33.Write a program to print only odd elements from a tuple.
# tpl=(51,42,63,28,95,62,75,62)
# for i in tpl:
#     if i%2!=0:
#         print(i)

#34.Write a program to print elements greater than 50.
# tpl=(51,42,63,28,95,62,75,62)
# for i in tpl:
#     if i >50:
#         print(i)

# #35.Write a program to count elements without using len().
# tpl=(51,42,63,28,95,62,75,62)
# count=0
# for i in tpl:
#         count+=1
# print("total elements =",count)

#36.Write a program to print elements at even index positions.
# tpl=(-51,42,-63,28,95,62,-75,62)
# for i in range(len(tpl)):
#     if i%2==0:
#         print(tpl[i],i)

#37.Write a program to print elements at odd index positions.
# tpl=(-51,42,-63,28,95,62,-75,62)
# for i in range(len(tpl)):
#     if i%2!=0:
#         print(i,tpl[i])

#38.Write a program to multiply all tuple elements.
# tpl=(2,5)
# mult=1
# for i in tpl:
#     mult*=i
# print(mult)

#39.Write a program to find maximum and minimum elements using loop
# tpl=(51,42,63,28,95,62,75,62)
# max=tpl[0]
# mini=tpl[0]
# for i in tpl:
#     if i > max:
#         max=i
#     elif i < mini:
#         min=i
# print(max)
# print(mini)


# #40.Write a program to create a nested tuple.
# tpl=((51,24,62),(45,65,43))
# print(tpl)

#41.Write a program to access elements from nested tuple.
# tpl=((51,24,62),(45,65,43))
# print(tpl[0])
# print(tpl[1])

# #42.Write a program to print all nested tuple elements.
# tpl=((51,24,62),(45,65,43))
# for i in tpl:
#     for j in i:
#         print(j,end=" ")

#43.Write a program to count total elements in nested tuple
# tpl=((51,24,62),(45,65,43))
# count=0
# for i in tpl:
#     for j in i:
#         #print(j,end=" ")
#         count+=1
#         print(count)

#44.Write a program to find sum of all elements in nested tuple
# tpl=((51,24,62),(45,65,43))
# sum=0
# for i in tpl:
#     for j in i:
#         sum += j
# print(sum)

#46.Write a program to take tuple input from user
# tpl=tuple(input("enter your values : ").split())
# print(tpl)

#47.Write a program to convert string into tuple
# str=("23,56,85,96,42,63")    
# tpl=tuple(str.split(","))
# print(tpl)

#48.Write a program to create tuple of vowels from a string
# str="my name is kuldeep "
# v=[]
# for i in str:
#     if i in "aeiouAEIOU":
#         v.append(i)
# print(tuple(v))

#49.Write a program to create tuple of squares from 1 to 10.
# tpl=(1,2,3,4,5,6,7,8,9,10)
# square=[]
# for i in tpl:
#     square.append(i*i)
# print(tuple(square))

# #50.Write a program to compare two tuples
# tpl=(1,2,3,4,5,6,7,8,9,10)
# tpl1=(51,42,63,28,95,62,75,46,42,63)
# if tpl==tpl1:
#     print("tuple are equal")
# else:
#     print("tuple are not ")