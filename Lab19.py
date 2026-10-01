# 1. (i) Create a list spanning 1 to 50 using list comprehension method. Call this list a.
a=[i for i in range(51)]
print(a)
"""
a=[]
for i in range(0,51):
    a.append(i)
print(a)
"""

#1. (ii) Slicing with positive step:
print(a[1:5]) #o/p:[1, 2, 3, 4]
print(a[3:20:2]) #o/p:[3, 5, 7, 9, 11, 13, 15, 17, 19]
print(a[::2]) #o/p:[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
print(a[::]) #o/p:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print(a[10::2]) #o/p:[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
print(a[1:1:1]) #o/p:Empty list; Because the start index and stop index are equal, the slice stops before including any elements, producing an empty result.
print(a[:0:]) #o/p:Empty list; Because the start index and stop index are equal, the slice stops before including any elements, producing an empty result.
print(a[-7::1]) #o/p:[44, 45, 46, 47, 48, 49, 50]
print(a[-6:]) #o/p:[45, 46, 47, 48, 49, 50]
print(a[-10:-4]) #o/p:[41, 42, 43, 44, 45, 46]

#1. (iii) Slicing with negative step:
print(a[::-1]) # o/p: [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a[::-3]) #o/p: [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2]
print(a[:1:-2]) #o/p: [50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
print(a[-1:-1:-1]) #o/p:Empty list; Because the start index and stop index are equal, the slice stops before including any elements, producing an empty result.
print(a[:-5:-1]) #o/p:[50, 49, 48, 47]
print(a[:0:-1]) #o/p;[50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[:-1:-1]) #o/p:Empty list; Default negative-step start index and the stop index (-1) both point to the last element
print(a[0:-5:-1]) #o/p:Empty list; slice starts at index 0 and attempts to move backward (step = -1)
print(a[-1:5:-1]) #o/p:[50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
print(a[2:2:-1]) #o/p:Empty list; Because the start index and stop index are equal, the slice stops before including any elements, producing an empty result.
print(a[2:1:-1]) #o/p:[2]
print(a[0:-5]) #o/p:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

#1. (iv) Modification of lists using list slicing:
#(a) Create a list of even numbers from a using list slicing technique.
even=a[::2]
print(even)

#(b) Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50.
b=a[:11]
c=a[36:51:2]
b.extend(c)
print("The new list is: ", b)

#2. (i) Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
#using do loop
a=[i for i in range(51)]
i=0
total_sum=0
length=len(a)
while i<length:
    total_sum=total_sum+a[i]
    i=i+1
print("SUM=",total_sum)

#list comprehension
total = sum([x for x in a])
print("SUM=",total)

#2. (ii) Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b=[n for n in a if n>1 and all(n%i!=0 for i in range(2,n))]
print("The prime numbers are: ",b)

#2. (iii) Using a do loop structure, collect all the common numbers in a and b into a new list c.
c=[x for x in a for y in b if x==y]
print("The common numbers are: ",c)
'''
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)'''

#3.List comprehension with strings Use list comprehension technique you learnt in class to do the following
#(i) (a) Create a string by joining the numbers in the above list a using the comma.
print(','.join(map(str,a)))
#(i) (b) Create a string by joining the numbers in the above list a using the period.
print('.'.join(map(str,a)))
#(i) (c) Create a string by joining the numbers in the above list a using the ‘—’.
print('-'.join(map(str,a)))
#(i) (d) Create a new string by first creating a list of squares of the elements in a,then listing them alongside the elements of a line by line.
print('\n'.join([str(x) + ' ' + str(x**2) for x in a]))

#(ii) Make a list of 10 people you know, and do the following:
#(a) Convert each element in the list to upper case using list comprehension
names = [
    "jayasri sundaram",
    "ridha marva",
    "sai sathya",
    "adithi joshi",
    "jeeba saji",
    "adyesha pattanayak"
]
upper_case=[people.upper() for people in names]
print("The list is: ", upper_case)

#(b) Swap the first name and surname of each element in the list
new_list=[' '.join(people.split()[::-1]) for people in names]
print("The swapped list is: ", new_list)

#(c) Join the first name and surname in each element as ’First.Last’. Note that the first letter of the first name and first letter of the surname should be upper case.
name_append=[name.title().replace(" ",".") for name in names]
print(name_append)

#(iii) Find the longest word in this sentence using list comprehension: ”She sells sea shells that she collects from the sea floor”.
sentence="She sells sea shells that she collects from the sea floor"
words=sentence.split()
longest=[word for word in words if len(word)==max([len(x) for x in words ])]
print("The longest word is: ",longest[0])

#(iv) Create a list of the words that are repeated in the above sentence.
sentence="She sells sea shells that she collects from the sea floor"
words=sentence.lower().split()
repeated=[word for word in words if words.count(word)>1]
print(list(set(repeated)))