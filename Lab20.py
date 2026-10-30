#1.Ask the user for an integer. Print whether it is positive, negative or zero. If it is non-zero, also print whether it is even or odd. If it is divisible by both 3 and 5, print "FizzBuzz number!".
a=int(input("Enter the integer:"))
if a>0:
    print("The number is positive")
elif a<0:
    print("The number is negative")
else:
    print("The number is zero")
if a>0 or a<0:
    if a%2==0:
        print("The number is even")
    else:
        print("The number is odd")
if a>0 or a<0:
    if a%3==0 and a%5==0:
        print("FizzBuzz number!")
    else:
        print("Not a FizzBuzz number!")



#2. Read a sentence. Count the vowels, consonants, digits and spaces. Ignore case and punctuation.
L=[]
vowel=consonant=spaces=digits=special_chars=0
sen=input("Enter the string: ")
sen_lower=sen.lower()
for i in sen_lower:
    L.append(i)
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        vowel=vowel+1
    elif i.isalpha():
        consonant=consonant+1
    elif i.isdigit():
        digits=digits+1
    elif i==" ":
        spaces=spaces+1
    else:
        special_chars = special_chars + 1
print("Vowels: ",vowel)
print("Consonants: ",consonant)
print("Digits: ",digits)
print("Spaces: ",spaces)
print("Special Characters: ", special_chars)



#3. Store a secret number between 1 and 50. Keep asking the user to guess until they get it right. After each wrong guess, print "Too high" or "Too low". When they get it, print how many attempts it took. As a bonus, stop after 7 attempts and reveal the number.
secret_number=int(input("Enter the secret number: "))
num=0
if secret_number in range(1,51):
    print("The number is between 1 and 50")
    for attempt in range(1,8):
        num = int(input("Guess the number: "))
        print("Attempt ",attempt)
        if num==secret_number:
            print("Congratulations! You guessed the number")
            print("Number of attempts taken: ",attempt)
            break
        elif num>secret_number:
            print("The input number is too high compared to the secret number")
        elif num<secret_number:
            print("The input number is too low compared to the secret number")
    if num!=secret_number: #initialize the number as zero to avoid getting num as undefined
        print("Attempt limit exceeded")
        print("The correct secret number is ",secret_number)
else:
    print("The number is not between 1 and 50")



#4. Multiplication Table Grid
n=int(input("Enter the number: "))
print("    ",end="")
for i in range(1,n+1): #for printing the header row
    print(f"{i:4}", end="")
print() #used to move the cursor to the next line
for i in range(1,n+1): #creates each row of the table
    print(f"{i:4}", end="")
    for j in range(1,n+1): #runs for every column in each row
        print(f"{i*j:4}", end="")
    print() #used to move the cursor to the next line



#5. Shopping List Manager
L=[]
num=input("Enter the number of items to be added to the list: ")
for i in range(0,int(num)):
    item=input("Enter the item to be added to the list: ")
    if item.lower() not in L:
        L.append(item.lower())
print("The input list is: ", L)
while True:
    print("The menu has the following operations: 1. Add item 2. Remove item 3. View list 4. Sort list 5. Quit")
    pick = int(input("Enter the operation that you want to perform on the list: "))
    if pick==1:
        add_item=input("Enter the item to be added to the list: ")
        L.append(add_item.lower())
        print("The modified list is: ",L)
    elif pick==2:
        remove_item = input('Enter the item to be removed from the list: ')
        if remove_item.lower() in L:
            L.remove(remove_item.lower())
            print("The modified list is: ", L)
        else:
            print("The item is not in the list")
        if len(L)==0:
            print("The list is empty")
    elif pick==3:
        print("The list is: ",L)
    elif pick==4:
        sort_list=sorted(L)
        print("The sorted list is: ",sort_list)
    elif pick==5:
        print("Thank you for shopping. You chose to QUIT the program")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")



#6. Student Grade Report
students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total=0
top_name=students[0][0]
top_score=students[0][1]
bottom_name=students [0][0]
bottom_score=students [0][1]
for i in students:
    if i[1]>top_score:
        top_score=i[1]
        top_name=i[0]
    if i[1]<bottom_score:
        bottom_score=i[1]
        bottom_name=i[0]
    total=total+i[1]
    if i[1]>=90:
        print(i[0], "scored GRADE A")
    elif i[1]>=80:
        print(i[0], "scored GRADE B")
    elif i[1]>=70:
        print(i[0], "scored GRADE C")
    elif i[1]>=60:
        print(i[0], "scored GRADE D")
    else:
        print(i[0], "FAILED")
print("Class average: ", total/len(students))
print("TOP SCORER: ", top_name,"scored" , top_score)
print("BOTTOM SCORER: ", bottom_name,"scored" , bottom_score)



#7. Word Frequency Counter
input_string=input("Enter the string: ")
word=input_string.split() #initially split the string with all the punctuations
final_input=[]
for words in word:
    final_input.append(words.strip(".,!?;:").lower()) #strip the punctuations in the words that were split and make them lower case
final_dict={}
for item in final_input: #takes the first word in the list
    count_words = 0
    for match in final_input: #compares the first word in the list with all other words in the list
        if match==item: #if there is a match increase count by one
            count_words=count_words+1
    final_dict[item]=count_words #final_dict[key]=value
print("Count of how often each word appears is: ", final_dict)
sorted_dict={}
for word in sorted(final_dict.keys()):
    sorted_dict[word]=final_dict[word]
print("The sorted dictionary with respect to the keys is: ", sorted_dict)
max_frequency=max(sorted_dict.values())
most_frequent_words=[]
for keys,values in sorted_dict.items():
    if values==max_frequency:
        most_frequent_words.append(keys)
print("The most frequent words is/are: ",most_frequent_words)
#input:The cat sat on the mat. The cat was happy!



#8. Course Enrollment Analysis
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
both_classes=[]
for stud in python_class:
    for student in java_class:
        if stud==student and student not in both_classes:
            both_classes.append(student)
print("Students taking both python and java classes: ",both_classes)
only_python=[]
for stud in python_class:
    if stud not in java_class and stud not in only_python:
            only_python.append(stud)
print("Students taking only python class: ",only_python)
only_one_course=[]
all_students=list(set(python_class+java_class))#set makes a unique list of all the students
for stud in all_students:
    if (stud in python_class and stud not in java_class) or (stud in java_class and stud not in python_class):
        only_one_course.append(stud)
print("Students taking exactly one course: ", only_one_course)
print("Sorted list of all students: ",sorted(all_students))

"""#8. Course Enrollment Analysis (using set operations)
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
python_set=set(python_class)
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
java_set=set(java_class)
print("Students taking both python and java classes: ",python_set.intersection(java_set)) # or use: python_set & java_set
print("Students taking only python class: ",python_set.difference(java_set))
print("Students taking exactly one course: ", python_set^java_set)
print("Sorted list of all students: ",sorted(set(list(python_class+java_class))))"""

name=input("Enter the name: ")
if name in python_class:
    if name in java_class:
        print(name,"is enrolled in python and java classes.")
    else:
        print(name, "is enrolled in python class.")
elif name in java_class:
    print(name,"is enrolled in java class")
else:
    print("ERROR: The student is not enrolled.")



#9. Password Validator
while True:
    pw = input("Enter the password: ")
    is_valid=True #overall check
    is_upper=False
    is_lower=False
    is_digit=False
    is_special = False
    is_space = False
    for char in pw:
        if char.isupper():
            is_upper=True
        if char.islower():
            is_lower=True
        if char.isdigit():
            is_digit=True
        if char in {"!", "@", "#", "$", "%", "&", "*"}:
            is_special = True
        if char in " ":
            is_space = True
    if len(pw)<8:
        print("ERROR: Password needs at least 8 characters.")
        is_valid=False
    if not is_upper:
        print("ERROR: Password needs at least one uppercase letter.")
        is_valid=False
    if not is_lower:
        print("ERROR: Password needs at least one lowercase letter.")
        is_valid=False
    if not is_digit:
        print("ERROR: Password needs at least one digit.")
        is_valid=False
    if not is_special:
        print("ERROR: Password needs at least one special character.")
        is_valid=False
    if is_space:
        print("ERROR: Password should not have any spaces.")
        is_valid=False
    if "password" in pw.lower():
        print("ERROR: The password should not be PASSWORD")
        is_valid=False
    if is_valid:
        print("The entered password is correct.")
        break
    else:
        print("Try again!!!")



#10. Inventory and Billing System
inventory = {"pen": (10.0, 50), "notebook": (45.0, 20), "eraser": (5.0, 100), "marker": (30.0, 15)} # (price,stock)
cart={}
while True:
    entry=input("Enter(item,stock): ")
    if entry.lower()=="done":
        print ("You chose to EXIT the program.")
        break
    entry_split=entry.split()
    if len(entry_split)!=2:
        print("ERROR: Enter both item and the quantity of the item required: ")
        continue
    item,quantity=entry_split[0].lower(),entry_split[1] #store item name in "item" and item quantity in stock in "quantity"
    if item not in inventory:
        print(f"ERROR: {item} not in stock.")
        continue
    if not quantity.isdigit() or int(quantity)<=0:
        print("ERROR: Give correct input.")
        continue
    qty=int(quantity)
    price,stock=inventory[item] #inventory[item] calls the value assigned to the key
    if qty>stock:
        print(f"ERROR: The stock is not enough. Only {stock} left.")
        continue
    cart[item]=cart.get(item,0)+qty #updates cart with item,quantity requested so far; dictionary.get(key, default_value) is used for reducing the KeyError
    print(cart)
    inventory[item]=price,stock-qty #updates the inventory
    print("The updated inventory is: ",inventory)
#To print receipt
print(f"\nReceipt")
sub_total=0
if not cart:
    print("SORRY! The cart is empty. The receipt cannot be printed.")
else:
    print("-" * 47)
    print(f"{'Item':<10}{'Quantity':>10}{'Unit Price':>15}{'Total':>12}")# left-align (<) and right-align (>)
    print("-" * 47)
    for item,qty in cart.items():
        unit_price=inventory[item][0]
        line_total=qty*unit_price
        sub_total=sub_total+line_total
        print(f"{item:<10}{qty:>10}{unit_price:>15.2f}{line_total:>12.2f}")
print("-" * 47)
print(f"{'Sub-Total':<35}{sub_total:>12.2f}")
if sub_total > 500:
    discount_amount = sub_total*0.10
    grand_total = sub_total - discount_amount
    print(f"{'Discount':<35}{discount_amount:>12.2f}")
    print("-" * 47)
    print(f"{'Grand-Total':<35}{grand_total:>12.2f}")
print("-" * 47)
#to print the inventory with stock availability
print(f"\nUpdated inventory with stock availability")
print("-" * 45)
print(f"{'Item':<10}{'Price':>10}{'Stock':>10}{'Availability':>15}")
print("-" * 45)
for key,value in inventory.items():
    if inventory[key][1]<10:
        availability="LOW STOCK"
    else:
        availability="AVAILABLE"
    print(f"{key:<10}{inventory[key][0]:>10}{inventory[key][1]:>10}{availability:>15}")
print("-" * 45)












