# Que.1. Write a program to check whether a year is a leap year or not.
# a=int(input("enter year : "))
# if a%4==0:
#     print("leap year")
# else:
#     print("not leap year")

#Que.2. Write a program to find the largest among three numbers using nested conditional statements. 

# a = int(input("enter frist num :"))
# b = int(input("enter second num :"))
# c = int(input("enter third num :"))
# if a>b:
#     if a>c:
#      print(" A is greater ")
#     else:
#       print(" C is greater ")
# else:
#     if b>c:
#       print("B is greater")
#     else:
#        print("C is greater")
       
# Que.3. Write a program to check whether a character is an uppercase letter, lowercase letter, digit, or 
#special character.
# a =input("enter your value :")
# if "a"<= a <="z":
#     print ("Lowercase")
# elif "A"<= a <="Z":
#     print("Uppercase")
# elif "0"<= a <="9":
#     print("digit")
# else:
#     print("special character")

#Que.4. Write a program to calculate electricity bill using different unit slabs.
#unit = float(input("consume unit:"))
# if unit<=100:
#     bill=unit*1.5
# elif unit<=200:
#     bill=(unit*1.5)+((unit-100)*2.5)
# elif unit<=300:
#     bill=(unit*1.5)+(unit*2.5)+((unit-200)*4)
# else:
#     bill=(unit*1.5)+(unit*2.5)+(unit*4)+((unit-300)*6)
# print("Electricity bill = rs,",round(bill,2))

#Que.5.  Write a program to determine whether a triangle is Equilateral, Isosceles, or Scalene. 

# a=int(input("enter side 1 : "))
# b=int(input("enter side 2 : "))
# c=int(input("enter side 3 : "))

# if a==b==c :
#     print("Equilateral")
# elif a==b or a==c or b==c:
#     print("isosceles")
# else:
#     print("scalene")

# Que.6. Write a program to create a simple calculator using if-elif-else.
# a = float(input("enter your frist number :"))
# operator =input("enter operator(+,-,*,/): ")
# b = float(input("enter your second number :"))

# if operator =="+":
#     print("add",a+b)
# elif operator =="-":
#     print("sub",a-b)
# elif operator =="*":
#     print("mult",a*b)
# elif operator =="+":
#     print("divide",a/b)
# else:
#     print("invalid operator")

# que.7. Write a program to calculate income tax according to salary ranges

# a=int(input("enter your salary :"))
# if a<=50000:
#     tax =0
# elif 50000<a<=90000:
#     tax = (a*2.5)
# elif 90000<a<=150000:
#     tax = (90000*2.5)+((a-90000)*4)
# elif 150000<a<=200000:
#      tax = (90000*2.5)+((a-90000)*4)+((a-150000)*6)
# else:
#      tax = (90000*2.5)+((150000-90000)*4)+((200000-150000)*6)+((a-200000)*8)

#      print("income tax",round(tax,2))


#Que.8. Write a program to check login authentication using username and password conditions. 
# a = input("enter your username :")
# b = input("enter your pass :")
# if ( a =="kuldeepkhas" ) :
#     print("valid username")
#     if ( b =="kuldeep@123" ) :
#        print("valid pass")
#     else: 
#        print("invalid pass")
# else: 
#     print("invalid username")

#Que.9 Write a program to determine whether a point lies in First quadrant, Second quadrant, Third 
#quadrant, Fourth quadrant, On axis, or At origin. 
# x = int(input("enter your x : "))
# y =int(input("enter your y :"))
# if x > 0 and y > 0:
#     print("frist quadrant")
# elif x > 0 and y < 0:
#     print("seconq uadrant")
# elif x < 0 and y < 0:
#     print("thirtd uadrant")
# elif x < 0 and y > 0:
#     print("forth uadrant")
# else:
#     print("pont lie at origin")
   
#10. Write a program to assign grades based on marks and display distinction for high scores. 

hindi =int(input("hindi :"))
eng=int(input("eng :"))
math =int(input("math:"))
science =int(input("science :"))
com =int(input("com :"))
sum=hindi+eng+math+science+com
print (sum)
per=sum/5
print(per)
if per>=90:
    print("Grade: A+\n distinction ")
elif per>=75:
    print("Grade: B+")
elif per>=50:
    print("Grade: C+")
elif per>=35:
    print("Grade: D+")
else:
    print("fail")
