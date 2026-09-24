"""Question1_Lab15"""
import math

result1=2.7/2 #Normal division, gives the quotient
print (result1)
result2=2.7//2 # // is floor division - output is integer less than or equal to quotient
print (result2)
result3=10+5j/2 # based on precedence --> 10+(5j/2) -- (5/2=2.5)-- Answer: (10+2.5j)
print (result3)
result4=complex(2.2, 5.3).conjugate().imag # complex ()= 2.2+5.3j; .conjugate()= 2.2-5.3j; .imag()- -5.3
print (result4)
result5=round(2.5) #python rounds half to even --> round(2.5)=2
print (result5)
result6=round(-2.5) #rounds half to even --> round (-2.5)=-3
print (result6)
result7=2//4-1 #(2//4)-1
print (result7)
result8=3*2**2 #3*(2**2)
print (result8)
result9=3**2*2 #(3**2)*2
print (result9)
result10=7//4 # 7/4=1.75 so 7//4=1
print (result10)
result11=7%4 # % gives the remainder
print (result11)
result12=-7%4 # a % b = a - (a // b) * b
print (result12)

"""Question2_Lab15"""
a=1
b=2
c=4
print (bool (a and b))
print (bool (not a<b or c>b))
print(bool (type(complex(a,b+c).real) is int)) #complex (real,imaginary), and .real=real value
# o/p = type (4.0)= 4.0 -- The o/p is not int, it is float-- Boolean= FALSE

"""Question3_Lab15"""
n=int(input("Enter the number: "))
k=int(input("Enter the number: "))
if n > 0:
        Addition = n + k
        Subtraction = n - k
        Multiplication = k * n
        division = k / n
print("Addition= ", Addition)
print("Subtraction= ", Subtraction)
print("Multiplication= ", Multiplication)
print("Division= ", division)

"""Question4_Lab15"""
a=float(input("Enter the number (a): "))
b=float(input("Enter the number (b): "))
c=float(input("Enter the number (c): "))
d= (b*b)- 4*a*c
e= math.sqrt(d)
result1= (-b+e) / (2*a)
result2= (-b-e) / (2*a)
print ("Result 1= ", result1)
print ("Result 2= ", result2)
