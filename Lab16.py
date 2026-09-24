# 1. Write a python script to accept a string from the user and print it in title-case.
string=input("Enter the string: ")
print(string.title()) #title() prints first letter of every word to uppercase and changes all other letters to lowercase.



# 2. Write a program to find the simple interest and the amount with simple interest included.
principal=int(input("Enter the principal amount (in rupees): "))
roi=int(input("Enter rate of interest per annum (in percentage): "))
time=int(input("Enter the time (in years): "))
SI=(principal*time*roi)/100
Amount=principal+SI
print("The simple interest is: ", SI)
print("Amount with simple interest included: ", Amount)



# 3. Write a program that asks for a person’s age and prints whether the person is eligible to vote or note.
Age=int(input("Enter the age (in years): "))
if Age<18:
    print("The person is not eligible for voting")
else:
    print("The person is eligible for voting")



# 4. Write a python script to take an input angle in degrees and print the values of all the 6 trigonometric functions for this angle.
import math
angle=int(input("Enter the angle (in degrees): "))
radian=math.radians(angle) # degree*(pi/180) also converts degree to radian
print("Angle in radians:", radian)
print("sin (angle): ", math.sin(radian))
print("cos (angle): ", math.cos(radian))
print("tan (angle): ", math.tan(radian))
print("cosec (angle): ", 1/math.sin(radian))
print("sec (angle): ", 1/math.cos(radian))
print("cot (angle): ", 1/math.tan(radian)) #asin, acos and atan gives the functional inverse and not the multiplicative inverse



# 5. Write a program to find the roots of a quadratic equation.
import cmath #import cmath for -ve sqrt calc.
a=float(input("Enter the number (a): "))
b=float(input("Enter the number (b): "))
c=float(input("Enter the number (c): "))
d= (b*b)- 4*a*c
e=cmath.sqrt(d)
result1= (-b+e) / (2*a)
result2= (-b-e) / (2*a)
print ("Root 1= ", result1)
print ("Root 2= ", result2)



# 6. Write a program to print the sum of the digits in a number.
num=int(input("Enter the number: "))
sum=0
while num>0:
    remainder=num%10
    sum=sum+remainder
    num=num//10
print(sum)



# 7. Write a script to check if a number is palindrome or not.
s1=input("Enter the number: ")
s2=s1[::-1] #reverse s1
if s1==s2:
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")



#8. Write a program to tell which quadrant a given point lies in the first, second, third or fourth quadrant
point=[]
for i in range(2):
    element=int(input())
    point.append(element)
print("The point is: ", point)
if point[0]>0 and point[1]>0:
    print("The point is in the first quadrant.")
elif point[0]<0 and point[1]>0:
    print("The point is in the second quadrant.")
elif point[0]<0 and point[1]<0:
    print("The point is in the third quadrant.")
elif point[0]>0 and point[1]<0:
    print("The point is in the fourth quadrant.")
elif point[0]==0 and point[1]==0:
    print("The point lies at the origin.")
else:
    print("The point lies on the axis.")



# 9. Write a program to reverse a number and print the reversed number.
num=input("Enter the number: ")
reversed_num=num[::-1]
print("The reversed number is: ", reversed_num)



# 10 Write a program to find whether a number is even or odd.
num=int(input("Enter the number: "))
if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")



# 11. Write a program to check if an input letter is a vowel or consonant
letter=input("Enter the letter: ")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("The given input is a vowel.")
else:
    print("The given input is a consonant.")



# 12. Write a program to check if an input string is palindrome
string=input("Enter the string: ")
rev_string=string[::-1]
if string==rev_string:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")



# 13. Write a program to print the factorial of a number
num=int(input("Enter the number: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(factorial)



# 14. Write a code to get the Fibonacci numbers beginning with f0 = 0 and f1 = 1 up to f25.
n=int(input("Enter the number: "))
a=0
b=1
result=()
for i in range(n):
    result= result + (a, )
    a,b=b,a+b
print(result)



# 15. Write a program to find the distance between 2 points, input is coordinates for the two points.
import math
L1=[]
for n in range(2):
    n1=int(input())
    L1.append(n1)
L2=[]
for n in range(2):
    n2=int(input())
    L2.append(n2)
print("The first point is: ", L1)
print("The second point is: ", L2)
d=((L2[0]-L1[0])**2)+((L2[1]-L1[1])**2)
distance=math.sqrt(d)
print("The distance between the input points are: ", distance)



# 16. Write a program to find whether a given triangle is equilateral isosceles or scalene. User input is length of sides.
a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("ERROR: The sum of any two sides must be strictly greater than the the third side.")

