#Question1
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    showroom = "NewAge"

    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name
    @staticmethod
    def show_intro_message():
        print("This class represents a car and its attributes.")

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

toyota_camry = Car("Toyota", "Camry", 2022, "Red")
ford_mustang = Car("Ford", "Mustang", 2022, "Black")

#Question1---(a)
print("Toyota Camry:")
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
print(toyota_camry.started)
print(toyota_camry.speed)
print(toyota_camry.max_speed)

#Question1---(b)
print("\nFord Mustang:")
print(ford_mustang.__dict__)

#Question1---(c)
print("\nCar make:", toyota_camry.make)
#print(Car.make)--Error:type object 'Car' has no attribute 'make'

#Question1---(d)
print("\nClass dictionary:")
print(Car.__dict__)

#Question1---(e)
Car.change_showroom("Toyota Showroom")
print("\nUpdated class dictionary:")
print(Car.__dict__)
print("\nShowroom:", Car.showroom)

#Question1---(f)
print("\nInstance dictionary:")
print(toyota_camry.__dict__)

#Question1---(g)
print("\nString representation:")
print(str(toyota_camry))
print(str(ford_mustang))

#Question1---(h)
print("\nStatic method:")
Car.show_intro_message()


#Question2
import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

class LinearAlgebra:
    def __init__(self):
        self.A = self.get_matrix("A")
        self.B = self.get_matrix("B")

    def get_matrix(self, name):
        rows = int(input(f"Enter rows of matrix {name}: "))
        cols = int(input(f"Enter columns of matrix {name}: "))
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive!")
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = int(input(f"Enter {name}[{i}][{j}]: "))
                row.append(value)
            matrix.append(row)
        return matrix

    @property
    def matrices(self):
        return self.A, self.B

    @matrices.setter
    def matrices(self, new_matrices):
        A, B = new_matrices
        if not A or not B:
            raise ValueError("Matrices cannot be empty!")
        if any(not row for row in A) or any(not row for row in B):
            raise ValueError("Matrix rows cannot be empty!")
        if any(len(row) != len(A[0]) for row in A):
            raise ValueError("Matrix A must be rectangular!")
        if any(len(row) != len(B[0]) for row in B):
            raise ValueError("Matrix B must be rectangular!")
        if len(A[0]) != len(B):
            raise ValueError("Matrix multiplication is not possible!")

        self.A = A
        self.B = B

    # Matrix multiplication
    @calculate_time
    def multiply(self):
        if not self.A or not self.B:
            raise ValueError("Matrices cannot be empty!")
        if len(self.A[0]) != len(self.B):
            raise ValueError("Matrix multiplication is not possible!")
        result = []
        for i in range(len(self.A)):
            row = []
            for j in range(len(self.B[0])):
                total = 0
                for k in range(len(self.B)):
                    total += self.A[i][k] * self.B[k][j]
                row.append(total)
            result.append(row)
        return result

obj = LinearAlgebra()
print("\nMatrix A:", obj.matrices[0])
print("Matrix B:", obj.matrices[1])
result = obj.multiply()
print("\nResultant Matrix:")
for row in result:
    print(row)

""""Testing with 50 x 50 matrices
A = [[1 for j in range(50)] for i in range(50)]
B = [[2 for j in range(50)] for i in range(50)]
obj.matrices = (A, B)
result = obj.multiply()
print("\n50 x 50 Resultant Matrix:")
for row in result:
    print(row)"""


#Regular expressions
import re
#3. Write a regular expression that is accepting a 3-digit integer between 000 and 255. Implement this in a script and test it for various possibilities
pattern=r'^(00[0-9]|0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
tests=["000","009","099","100","256","999","12","025"]
for value in tests:
    if re.match(pattern,value):
        print(value,"Valid")
    else:
        print(value,"Invalid")


#4. Write a regular expression that matches integers from 0 to 255.
pattern=r'^[0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]$'
test=["0","9","10","99","100","199","200","255","256","025","-1","4567"]
for value in test:
    if re.fullmatch(pattern,value):
        print(value,"Valid")
    else:
        print(value,"Invalid")


#5. Write a Python script to check if a given string contains an email address or not.
string_input=input("Enter a string: ")
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
if re.search(pattern,string_input):
    print("Email address found.")
else:
    print("Email address not found.")
#test_cases: contact me at hello@gmail.com; @gmail.com; hello@gmail


#6. Write a Python script that accepts a line of CSV and checks if the 3rd field contains exactly an email address or not, given that there are more than 3 fields.
import csv
#Create te csv file
with open("csv_file.csv","w") as csv_file:
    print('"Smith, Jane",1234,jane.smith@domain.co.uk,Active,2026',file=csv_file)
#Read the csv file
with open("csv_file.csv","r") as csv_file:
    csv_reader = list(csv.reader(csv_file))[0]
print("The csv file contains:",csv_reader)
pattern_email = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
if len(csv_reader)<3:
    print("Error: The CSV line must contain at least 3 fields.")
if len(csv_reader)>=3:
    if re.search(pattern_email,csv_reader[2]):
        print("Email address found.")
    else:
        print("Email address not found.")
#test_case1=John,Doe,john@gmail.com,Developer
#test_case2=Jane,Smith,not-an-email,Manager,LA
#test_case3='"Smith, Jane",1234,jane.smith@domain.co.uk,Active,2026'


#7. Write a Python script that scans through a given piece of text and extracts all unique email addresses from it.
text=input("Enter a text:")
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails=re.findall(pattern,text)
print("Unique email addresses:",set(emails))


#8. Write a Python script that reads in a piece of text and prints it out masking out email addresses. Thus and email address ”helloworld@python.com” should become ”h********d@python.com”.
text=input("Enter the text:")
pattern_email=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
match=re.search(pattern_email,text)
email=match.group()
name,domain=email.split("@")
masked_name=name[0]+"*"*(len(name)-2)+name[-1]
print("The masked email address is",masked_name+"@"+domain)
#test_case=My email address is helloworld@python.com


#9. Test if a DNA sequence contains an EcoRI restriction site using regular expressions. dna= ”ATCGCGAATTCAC” pattern = GAATTC
dna_sequence="ATCGCGAATTCAC"
pattern=r'GAATTC'
if re.search(pattern,dna_sequence):
    print("The DNA sequence contains an EcoRI restriction site.")
else:
    print("The DNA sequence does not contain an EcoRI restriction site.")


#10. Check for the presence of an AvaII recognition site, which can have two different sequences: GGACC and GGTCC. Use regular expressions. dna = ”ATCGCGAATTCAC” pattern = GGACC and GGTCC
dna_sequence="ATCGCGAATTCAC"
pattern=r'GG[AT]CC' #searches for A or T in the position.
if re.search(pattern,dna_sequence):
    print("The DNA sequence contains an AvaII restriction site.")
else:
    print("The DNA sequence does not contain an AvaII restriction site.")


#11. Check for the presence of a BisI restriction site using regular expression character groups:A character group is a pair of square brackets with a list of characters inside them. dna= ”ATCGCGAATTCAC” pattern = GCNGC, where N represents any base, i.e. A,T,G,C
dna_sequence="ATCGCGAATTCAC"
pattern=r'GC[ATGC]GC'
if re.search(pattern,dna_sequence):
    print("The DNA sequence contains an BisI restriction site.")
else:
    print("The DNA sequence does not contain an BisI restriction site.")


#12. Take a DNA sequence and determine whether or not it contains any ambiguous bases i.e. any bases that are not A, T, G or C. If there is a non-ambiguous base, print the non-ambiguous bases. dna = ”ATCGCGYAATTCAC”
dna_sequence="ATCGCGYAATTCAC"
pattern=r'[^ATGC]' #matches any character other than ATGC
if re.search(pattern,dna_sequence):
    print("Ambiguous bases found in DNA sequence.")
    non_ambiguous=re.sub(pattern,'',dna_sequence)
    print("The non-ambiguous DNA sequence is",non_ambiguous)


#13. Write a regular expression to split the DNA string wherever we see a base that isn’t A,T,G or C. if the dna = ”ACTNGCATRGCTACGTYACGATSCGAWTCG”, the output should be [’ACT’, ’GCAT’, ’GCTACGT’, ’ACGAT’, ’CGA’, ’TCG’]
dna_sequence="ACTNGCATRGCTACGTYACGATSCGAWTCG"
pattern=r'[^ATGC]'
print("The output is:",re.split(pattern,dna_sequence))