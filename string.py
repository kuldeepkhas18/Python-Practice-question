#que1.Write a program to count the number of characters in a string
# str = ("kuldeep")
# count = 0
# for i in str:
#         count += 1
# print(count)

#Que2.Write a program to count words in a sentence.
# str = input("enter your string :")
# count = str.count("e")
# print(count)

#Oue3.Write a program to print only vowels from a string.
# s = input("enter your str :")
# count = 0
# for i in s:
#     if i in "aeiouAEIOU":
#         count += 1
# print("total vowel =",count)

#Que.4 Write a program to check whether a string is palindrome or not
# str = input("enter your value :")

# if str == str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#Que.5 Write a program to reverse a string
# str = input("enter your value :")
# print(str[::-1])

#Que.6 Write a program to convert a string into uppercase and lowercase
# s = ("kuldeep")
# print(s.upper())
# print(s.lower())

#Que.7 Write a program to count how many times a character appears in a string
# s = input("enter your value :")
# print(s.count('e'))

#Que.8 Write a program to remove spaces from a string
# s = ("     my name   is     kuldeep  khas    ")
# print(" ".join(s.split()))

#Que.9 Write a program to replace a word in a string with another word.
# s =(" my name is radhey")
# print(s.replace("radhey","kuldeep"))

#Que.10 Write a program to find the length of a string without using len()
# s = ("kuldeep")
# count=0
# for i in s:
#     count += 1
# print("length of str : ",count)

#Que.11.Write a program to check whether a character is present in a string or not.
# s = input("enter your value")
# m = input("enter your value")
# if m in s:
#     print("chr is present")
# else:
#     print("not present")

#Que.12.Write a program to find duplicate characters in a string

# s = input("enter your value :")
# d = ""
# for i in s:
#     if s.count(i)>1 and i not in d:
#         print(i)
#         d+=i

#Que.13.Write a program to count words in a sentence
# s = input("enter your value :")
# print(len(s.split()))

#Que.14.Write a program to print only vowels from a string.
# s = input("enter your value  :")
# for i in s:
#     if i in 'aeiouAEIOU':
#      print(i)

#Que.15.Write a program to print the first non-repeating character in a string
# s = input("enter your value :")
# for i in s:
#     if s.count(i) == 1 :
#         print (i)
        
#Que.16.Write a program to sort characters of a string alphabetically
# s = input("enter your value :")
# print("".join(sorted(s)))

#Que.17.Write a program to remove duplicate characters from a string
# s=input("enter you value :")
# d = ""
# for i in s:
#     if i not in d:
#         d+=i
# print(d)

#Que.18.Write a program to check if two strings are anagrams.
# s1=input("enter your value :")
# s2=input("enter your value :")
# if sorted(s1)==sorted(s2):
#     print("anagrams")
# else:
#     print("not anagrams")

#Que.19.Write a program to capitalize the first letter of sentence.
# s=input("enter your value :")
# print(s.capitalize())

#Que.20.Write a program to capitalize the first letter of every word
# s=input("enter your value :")
# print(s.title())

#Que.21.Write a program to find the ASCII value of each character in a string
# s=input("enter a string :")
# for i in s:
#     print(i,"=",ord(i))

#Que.22.Write a program to find the longest word in a sentence
# s=input("enter your value :")
# words = s.split()
# longest = max(words,key=len)
# print("longest word is :", longest)