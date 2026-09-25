#1. Write a program to iterate over a dictionary and print the key-value pairs.
n=input("Enter the number of entries to be added to the dictionary: ")
new_dic=dict([])
for i in range(int(n)):
    key=input(f"Enter the key{i+1}: ") #f evaluates the expression that is given inside the input command
    values=input(f"Enter the value for '{key}': ")
    new_dic[key]=values
print("The dictionary is: ", new_dic)
for key,value in new_dic.items():
    print(key, ":", value)



#2. Write a program to sum all the values of a dictionary.
new_dict=dict([])
n=input("Enter the number of entries required: ")
for i in range(int(n)):
    key=input(f"Enter the key{i+1}: ")
    value=input(f"Enter the value for '{key}': ")
    new_dict[key]=value
print("The created dictionary is: ", new_dict)
sum=0
for value in new_dict:
    sum+=int(new_dict[value])
print("The sum of all the values in the created dictionary is: ", sum)



#3.Write a program to find the maximum and minimum values of a dictionary.
D={'one':4,'two':78,'three':0,'four':100,'five':55}
minimum=min(D.values())
maximum=max(D.values())
print("The minimum of the dictionary is: ", minimum)
print("The maximum of the dictionary is: ", maximum)



#4. Given a dictionary with a values list, extract the key whose value has the most unique values.
test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
max_unique=0
result=""
for key,values in test_dict.items():
    unique=len(set(values))
    if unique>max_unique:
        max_unique=unique
        result=key
print(result)



#5. Remove all duplicate words from a given sentence using a dictionary.
"""version1"""
string=input("Enter the sentence: ")
string_split=string.split()
unique=set(string_split)
dic=dict([])
for word in string_split:
    if word in unique:
        unique.remove(word) #removes the word in set so future duplicate words are ignored
        dic[word]=1 #words are added in the same order as in string_split
print("The sentence after removing the duplicate words is: "," ".join(dic.keys()))

"""version 2"""
string=input("Enter the sentence: ")
string_split=string.split()
d=dict([]) #when the elements are added to the dictionary the duplicates are automatically removed
for word in string_split:
    d[word]=1
print("The sentence after removing the duplicate words is: "," ".join(d.keys()))



#6. Write a program with a function to calculate the area of a triangle.
import math
def triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
        d = s * (s - a) * (s - b) * (s - c)
        area = math.sqrt(d)
        print("The area of the triangle is: ", area)
    else:
        print("ERROR: The sum of any two sides must be strictly greater than the the third side.")

triangle(5,5,5)



#7. Write a program with a function to find whether a given triangle with sides a, b, c is isosceles, scalene or equilateral triangle, also provide a test case output from the program.
def triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            print("The triangle is Equilateral.")
        elif a == b or b == c or a == c:
            print("The triangle is Isosceles.")
        else:
            print("The triangle is Scalene.")
    else:
        print("ERROR: The sum of any two sides must be strictly greater than the the third side.")

triangle(1,2,10)



#8. Write a program to interchange the even and odd components of an input list. The list can contain any type of variables.
L=[23,32,33,44,'BDBH101','hello','python', 15, 1e-10, True,'hit']
for i in range(0,len(L)-1,2):
    L[i],L[i+1]=L[i+1],L[i]
print("The list with the interchanged components is: ", L)



#9. Write a function to extract the codons into a list of 3-letter strings given a sequence and from what position (input as an integer) the sequence should be read.
def codon(sequence,position):
    start=position-1
    result=[]
    for i in range(start,len(sequence)-2,3):
        result.append(sequence[i:i+3])
    return result
sequence="GTTTCGATTATAACG"
print("1st position: ", codon(sequence,1))
print("2nd position: ", codon(sequence,2))



#10. Write a function called nextPrime that finds and returns the first prime number larger than some integer, n.
def isPrime(n):
    if (n<2):
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

def nextPrime(n):
    n=n+1
    while not isPrime(n):
        n=n+1
    return n
n=int(input("Enter a number: "))
print("Next prime: ", nextPrime(n))



#11. Use your function to create a main program that finds and displays all of the magic dates in the 20th century.
import calendar
def isMagicDate(date,month,year):
    year=year%100
    if date*month==year:
        return True
    else:
        return False

for year in range(1900,2001):
    for month in range(1,13):
        max_days = calendar.monthrange(year, month)[1] # calendar.monthrange(year, month)[1] returns the exact max days in that month
        for date in range(1, max_days + 1):
            if isMagicDate(date,month,year):
                print(date,"/",month,"/",year)