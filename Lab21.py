#1 Write a program to convert temperature in Celsius to Fahrenheit using map function.
def f(c):
    result_temp=c*(9/5)+32
    return result_temp
c=int(input("Enter the temperature in Celsius: "))
result=list(map(f,[c]))[0]
print("Temperature in Fahrenheit: ",result)



#2. Write the above program using lambda expression.
temp = int(input("Enter the temperature in Celsius: "))
result=list(map(lambda c:(c * 9/5) + 32,[temp]))[0] #map function is iterable, so the input has to be list/tupules/dict. If a single value is given it will give a TypeError saying that int is not iterable
print("Temperature in Fahrenheit: ",result)

"""n=input("Enter the number of elements to be added to the list: ")
temp_list=[]
for i in range(int(n)):
    temp = int(input("Enter the temperature in Celsius: "))
    temp_list.append(temp)
temp_input=print("The input list is: ",temp_list)
result=list(map(lambda c:(c * 9/5) + 32,temp_list))
print("Temperature in Fahrenheit: ",result)"""



#3 Write a program to convert a tuple of angles into a list of tuples with each tuple containing the sine and cosine of an angle
import math
input_tuple=()
num=int(input("Enter the number of elements to be added to the list: "))
for i in range(num):
    input_angle=int(input("Enter the angle to be added to the list: "))
    input_tuple=input_tuple+(input_angle,)
print("Input to tuple of angles: ",input_tuple)
output_tuple=list(map(lambda value:(math.sin(math.radians(value)),math.cos(math.radians(value))),input_tuple))
print("The output tuple is: ",output_tuple)

"""output_tuple=[]
for value in input_tuple:
    rad=math.radians(value)
    sine_angle=math.sin(rad)
    cosine_angle=math.cos(rad)
    angle_pair=(sine_angle,cosine_angle)
    output_tuple.append(angle_pair)
print(output_tuple)"""



#4.Write a program to filter out the odd elements of the Fibonacci series for the first n terms.
num=int(input("Enter the number: "))
a=0
b=1
result=[]
for i in range(num):
    result.append(a)
    a,b=b,a+b
print("The Fibonacci series is: ",result)
result_odd=list(filter(lambda x:x%2,result))
print("The odd elements of the Fibonacci series for the first",num,"terms is: ", result_odd)



#5. Write a program to find the sum of all the elements in a list using lambda and reduce functions.
from functools import reduce
num=int(input("Enter the number of elements to be added to the list: "))
input_list=[]
for i in range(num):
    element=int(input("Enter the element to be added to the list: "))
    input_list.append(element)
print("The input list is: ",input_list)
sum_elements=reduce(lambda x,y:x+y,input_list) #applies the rule cumulatively to each and every element in the list
print("The sum of elements in the list is: ",sum_elements)



#6. Write a function called cell_metabolism that takes the number of glucose and oxygen molecules, that contains an inner function energy_output() to calculate ATP yield (assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP produced.
def cell_metabolism(glucose,oxygen):
    def energy_output():
        glucose_cycle=glucose//1
        oxygen_cycle=oxygen//6
        completed_cycle=min(glucose_cycle,oxygen_cycle) #for finding the limiting reactant
        total_atp=completed_cycle*38 #multiply the number cycles that the limiting reactant can take part with the total ATP yield for one cycle that is 38
        return total_atp
    if energy_output()==0:
        print("No ATP yield")
        if glucose==0:
            print("ERROR: No Glucose available")
        else:
            print("ERROR: Insufficient oxygen")
    else:
        print("Total ATP yield: ", energy_output())

glucose=int(input("Enter the number of glucose molecules: "))
oxygen=int(input("Enter the number of oxygen molecules: "))
cell_metabolism(glucose,oxygen)



#7. Write a function analyse_dna(sequence) that defines an inner function gc_content() to calculate GC% . The outer function should print whether the given DNA is AT rich or GC rich sequence.
def analyse_dna(sequence):
    sequence_split = list(sequence) #split requires a separator for them to split. Since there is no separator here we used list(sequence)
    count_gc=0
    total_count=len(sequence_split)
    if total_count==0: #exits the entire code when the sequence is empty
        print("ERROR: The DNA sequence is empty")
        return
    for i in sequence_split:
        if i=="G" or i=="C":
            count_gc=count_gc+1
    print("The total number of bases is:",total_count)
    print("The GC count is:",count_gc)
    def gc_content():
        gc_percentage=(count_gc/total_count)*100
        return gc_percentage
    print("The GC content is:",gc_content(),"%")
    if gc_content()>50:
        print("The DNA sequence is GC rich")
    elif gc_content()<50:
        print("The DNA sequence is AT rich")
    else:
        print("The DNA sequence is balanced (equally AT and GC rich)")

sequence=input("Enter a DNA Sequence: ")
analyse_dna(sequence)



#8. Write a function protein_energy_temp() with an inner function calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use random or user-input ∆H, ∆S and return stability (”stable" if ∆G < 0).
def protein_energy_temp():
    def calculate_free_energy(enthalpy,entropy,t):
        temp=t+273.15
        free_energy=enthalpy-(temp*entropy)
        return free_energy
    print("The free energy change is: ", round(calculate_free_energy(enthalpy,entropy,t),2),"kJ/mol")
    if calculate_free_energy(enthalpy,entropy,t)<0:
        print("STABLE")
    else:
        print("NOT STABLE")

enthalpy=float(input("Enthalpy change: "))
entropy=float(input("Entropy change: "))
t=float(input("Temperature: "))
protein_energy_temp()



#9. Write a function population_growth(initial,rate, time) that defines an inner function exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0 represents the initial population and N(t) is population after time t. The inner function returns the population after time, and the outer function rounds and prints it.
import math
def population_growth(initial,rate, time):
    def exponential_growth():
        population_after_time=initial+math.exp(time*rate)
        return population_after_time
    print("Population after",time,"hours: ",round(exponential_growth(),2))

initial=float(input("Initial population: "))
rate=float(input("Rate of growth: "))
time=float(input("Time: "))
population_growth(initial,rate, time)



#10. Write a program to extract all vowels in a given string using list comprehension.
string=input("Enter the string: ")
vowels=[word.lower() for word in string if word.lower() in "aeiou"]
print(vowels)

"""string=input("Enter the string: ")
vowels=[]
for words in string: #In Python, string is treated as a sequence of individual characters, not words
    if words.lower() in "aeiou":
        vowels.append(words.lower())
print(vowels)"""



#11. Write a program to concatenate a list of strings to make a sentence using reduce function.
from functools import reduce
num=int(input("Enter the number of elements to be added to the list: "))
string_list=[]
for i in range(num):
    element=input("Enter the element to be added to the list: ")
    string_list.append(element)
print("The input list of strings is: ",string_list)
result=reduce(lambda x,y: x+' '+y,string_list)
print("The sentence is: ",result)