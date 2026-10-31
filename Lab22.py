#Question1
def greet_decorator(func):
    def wrapper():
        print("Start.....")
        func()
        print("End.....")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator.")

message()


#Question2
def before_after(func):
    def wrapper():
        print("Function is starting....")
        func()
        print("Function has finished!")
    return wrapper

@before_after
def calculate():
    print("Calculating...")

calculate()


#Question3
def count_calls(func):
    calls=0
    def wrapper():
        func()
        nonlocal calls
        calls+=1
        print("Call count:",calls)
    return wrapper

@count_calls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()


#Question4
def check_positive(func):
    def wrapper(n):
        if n>0:
            result=func(n)
            print("The output of the function is: ",result)
            return result
        else:
            if n<0:
                print("The number is negative. It has to be positive.")
                return None
            else:
                print("The input has to be non-zero.")
                return None
    return wrapper

@check_positive
def main_function(n):
    number=n*n
    return number

n=int(input("Enter a number: "))
main_function(n)
print(main_function.__name__)


#Question5
import time
def measure_time(func):
    def wrapper(n):
        start_time = time.perf_counter() #time.perf_counter() reads a monotonic clock—a counter that continually ticks forward at a fixed rate based on CPU frequency cycles.
        result=func(n)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("The run time of the function is:", run_time,"seconds")
        return result
    return wrapper

@measure_time
def factorial(n):
    count=1
    for i in range(1,n+1):
        count=count*i
    print("Factorial:",count)

n=int(input("Enter a number: "))
factorial(n)


#Question6&7
import math
import time
def measure_time(func):
    def wrapper(initial, rate, time_period):
        start_time = time.perf_counter()
        result = func(initial, rate, time_period)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("The run time of the function is:", run_time, "seconds")
        return result
    return wrapper

def population_growth(initial, rate, time_period):
    def exponential_growth():
        population_after_time = initial * math.exp(time_period * rate)
        return population_after_time
    return round(exponential_growth(), 2)

@measure_time
def run_million_iterations(initial, rate, time_period):
    for _ in range(1_000_000):
        result = population_growth(initial, rate, time_period)
    print("Population after", time_period, "hours:", result)

initial = float(input("Initial population: "))
rate = float(input("Rate of growth: "))
time_period = float(input("Time: "))
run_million_iterations(initial, rate, time_period)


#Question8&9
def log_function_call(func):
    def wrapper():
        print("Running DNA analysis....")
        result = func()
        print("Result after running the function(GC content): ", result, "%")
        print("Analysis complete!")
        return result
    return wrapper

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
    #print("The total number of bases is:",total_count)
    #print("The GC count is:",count_gc)
    @log_function_call #-----------------------#
    def gc_content():
        gc_percentage=(count_gc/total_count)*100
        return gc_percentage
    per = gc_content()
    #print("The GC content is:", per, "%")
    if per > 50:
        print("The DNA sequence is GC rich")
    elif per < 50:
        print("The DNA sequence is AT rich")
    else:
        print("The DNA sequence is balanced (equally AT and GC rich)")

sequence=input("Enter a DNA Sequence: ")
analyse_dna(sequence)

