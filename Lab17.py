# 1. Write a script to convert the binary number B into decimal.
B=int(input("Enter the binary number: "))
Blist=list(map(int,str(B))) #The code converts the number to a string ("123"), uses map() to convert each character back into an individual integer, and stores the results inside a new list
decimal=0
j=len(Blist)-1
for i in range(0,len(Blist)):
    decimal=decimal+(Blist[i]*(2**j))
    j=j-1
print("The decimal is: ",decimal)
#B=input("Enter the binary number: ")
#decimal=int(B,2)
#print(decimal)



# 2. Write a script that computes power - raise base to the n-th power.
base=int(input("Enter the base: "))
power=int(input("Enter the power: "))
output=pow(base,power)
print(output)



# 3. Write a script to check if a given number, N, is prime or not
num=int(input("Enter the number: "))
if num<2:
    print("The number is not prime.")
else:
    is_prime = 1
    for i in range(2,num):
        if num%i==0:
            is_prime=0
            break
    if is_prime==1:
        print("The number is prime.")
    else:
        print("The number is not prime.")



# 4. Write a script to print individual digits of a number, N.
num=input("Enter the number: ")
num_list=list(num)
for i in range(0,len(num_list)):
    print(num_list[i])



# 5. Write a script to print the first half of a string, S.
string=input("Enter the string: ")
half=len(string)//2
print("The first half of the given string is: ", string[:half])



# 6. Write print alternate characters of a string, S
string=input("Enter the string: ")
alternate=""
for i in range(0,len(string)):
    if i%2==0:
        alternate += string[i]
print(alternate)  # print(string[::2])



# 7. Write a script to trim leading whitespace characters from a string, S.
string=input("Enter the string: ")
string_list=list(string)
leading_spaces_done = False
new_string=""
for i in range(0,len(string_list)):
    if string_list[i]==" " and not leading_spaces_done:
        continue
    else:
        leading_spaces_done = True
        new_string+=string_list[i]
print(new_string)
#trimmed_string = string.lstrip()



# 8. Write a script to count the number of occurrences of a word, W, in a sentence, S.
S=input("Enter the sentence: ")
W=input("Enter the word: ")
S=S.lower()
W=W.lower()
word_list=S.split()
count=0
for word in word_list:
    cleaned_word = word.strip(".,!?;:\"'")
    if cleaned_word==W:
        count=count+1
print("Occurrences: ", count)
#Example sentence: The quick brown fox jumps over the lazy dog. The dog didn't even bark.



# 9. Write a script to check if two strings are anagrams of each other
S1=input("Enter the first string: ")
S2=input("Enter the second string: ")
if sorted(S1)==sorted(S2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")



# 10. Write a program to find the even numbers in a list, L.
numbers=[56,89,76,43,21,10,88,44,20]  #numbers=list(range(1, 15))-- using the list in-built function
even=[]
for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        even.append(numbers[i])
print("The even numbers in the list is: ", even)



# 11. Write a program to print the duplicate elements in a list, L.
L=["hello","world","hii","world","beautiful","hello","tree","nature","mountains","soil","sand","tree","tree"]
duplicates=[]
for i in range(0,len(L)):
    for j in range(0,i):
        if L[i]==L[j] and L[i] not in duplicates:
            duplicates.append(L[i])
print(duplicates)



# 12. Write a program to subtract two matrices, m1 and m2, using a list of lists.
m1=[[10, 8, 6],
    [5, 9, 7],
    [4, 3, 2]]
m2 = [[2, 3, 1],
    [1, 4, 2],
    [3, 1, 0]]
result=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j]=m1[i][j]-m2[i][j]
print("The matrix is: ", result)



# 13. Write a program to extract elements of a list, if it occurs more than k times.
L = [1, 3, 5, 3, 2, 3, 5, 5, 4, 3, 1, 5, 5]
k=int(input("Enter the number of occurrences: "))
result=[]
for i in L:
    if L.count(i)>k and i not in result:
        result.append(i)
print("The duplicate elements that occur more than k times are: ", result)



# 14. Write a program to remove all occurrences of an element from a list, L.
L=[1, 1, 2, 3, 4, 5, 1, 2]
e=int(input("Enter the element that has to be removed form the list: "))
new_string=[]
for i in range(0,len(L)):
    if L[i]!=e:
        new_string.append(L[i])
print("The new string with all occurrences of element 'e' removed form the list: ", new_string)



# 15. Write a program to extract words from a string list, L whose first character is k.
L=["Kangaroo", "apple", "koala", "kiwi", "banana", "Kitchen", "mango"]
k=input("Enter the starting character: ")
result=[]
for n in L:
    if n[0].lower()==k.lower():
        result.append(n)
print(result)

