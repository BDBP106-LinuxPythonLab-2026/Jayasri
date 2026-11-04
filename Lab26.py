import numpy as np
#(1) Import numpy and check the version using the command print(np.__version__)
print("Current version of numpy is",np.__version__)


#(2) Array creation and manipulation exercises.
#(i) Create a 1D array from 0 to 9.
array=np.arange(10)
print("The array is:",array)

#(ii) Create a boolean array of size 3x3.
array_bool=np.random.choice([True,False],size=(3,3),p=[0.7,0.3]) #np.random.choice(choices,size of the matrix,probability of occurrence of the choices)
print(f"The boolean array is:\n",array_bool)
"""array_bool=[[1,0,1],[0,1,1],[1,0,1]]
b=np.array(array_bool,dtype=bool)
print("The boolean array is:",b)"""

#(iii)Create an array of prime numbers from 1 to 50 using a similar approach.
arr=np.array([x for x in range(2,51) if all(x%i!=0 for i in range(2,x))])
print("Array of prime numbers from 1 to 50: ",arr)

#(iv) Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print the two arrays.
array=np.random.choice(100,size=20,replace=False)# The elements are in the range of 100, with the array size=20 and no duplicates in the array
print("1D array with 20 random elements: ",array)
print(f"The reshaped array is: \n",array.reshape(4,5))

#(v) Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has only 1s. Then stack the two arrays horizontally.
a=np.arange(10)
print("1D array with numbers ranging from 0 to 9:",a)
b=np.ones(9)
print("1D array with ones only:",b)
print("The horizontally stacked array is:", np.hstack((a,b)))

a=np.arange(100)
print("1D array with first 100 numbers:",a)
b=([x for x in range(2,1000) if all(x%i!=0 for i in range(2,x))][:100]) #extracts the first 100 prime numbers
print("1D array with first 100 prime numbers",b)

#(vi) Define two 1D arrays, where array a has list of first 100 numbers, and b has first 100 prime numbers. Obtain a new array that is the intersection of these two arrays
print("The intersection of a and b is: ",np.intersect1d(a,b))

#(vii) Use the above two arrays with the aim this time to remove items from a that are in b.
print("The difference between a and b is ",np.setdiff1d(a,b))

#(viii) Use the above two arrays with the aim of getting the indices of common elements between the two arrays. (Hint: Use np.where(a==b))
overlap=np.isin(a,b) #gives a boolean array as the same size of a. If the element is in b, return TRUE else return FALSE.
print("The indices of common elements between a and b is",np.where(overlap)[0]) #np.where(condition)[0] unpacks the tuple and gives a 1D array as the output

#(ix) Extract the elements of the array a above that are greater than 5 and less than 20.
array=np.arange(30)
print("The array is: ",np.where((array>5) & (array<20))[0]) #a[(a > 5) & (a < 20)]


#(3) We know how to reverse the elements in a 1D array- a[::-1]. How would you reverse the rows in a 2D array? How would you reverse the columns in a 2D array?
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(f"The original array is:\n",a)
print(f"The array with reversed rows is:\n",a[::-1,:]) #np.flipud(arr)
print("The array with reversed columns is:\n",a[:,::-1]) #np.fliplr(arr)


#(4) Thinking along the same lines of the above question, how will you swap two columns in a 2D array? Define a 3x3 matrix with random values, and swap first and second columns in this array.
a = np.random.rand(3, 3)
print(f"The original matrix is: \n",a)
a[:,[0,1]]=a[:,[1,0]]
print(f"The array with first 2 columns swapped is:\n",a)


#(5) You are given two 1D arrays. Write a function to create a new array that contains the maximum of the respective elements in the two arrays. For example, if a=[1,2] and b=[0,5] then the new array will be c=[1,5].
a = np.array([1, 2])
b = np.array([0, 5])
result=np.maximum(a,b) #[np.max(a).item(),np.max(b).item()]
print("The new array that contains the maximum of the respective elements in the two arrays is:",result)


#(6) Explore the set_printoptions() function to print a 3x3 matrix containing random numbers up to 3 decimal places.
a = np.random.rand(3, 3) #3x3 matrix with random values
np.set_printoptions(precision=3)
print(f"The 3x3 matrix containing random numbers up to 3 decimal places is:\n",a)


#(7) Explore the set_printoptions() function to pretty-print a numpy array by suppressing the scientific notation (like 1e10).
np.set_printoptions(suppress=True)
a = np.array([0.0000001, 0.000002, 1000000, 2000000])
print(a)


#(8) Create a numpy array with any 10 numbers, and print the average, highest and lowest score, how many numbers are above 20, and the scores that are below 20.
a = np.array([45, 12, 67, 89, 23, 15, 90, 34, 10, 56])
print("Average",np.average(a)) #np.mean(a)
print("Highest score",np.max(a))
print("Lowest score",np.min(a))
print("Numbers above 20:", np.sum(a > 20))
print("Numbers below 20:", np.sum(a < 20))


#(9) Read the counts for 5 genes and store them in a numpy array. Without writing a loop, calculate the log2 of each element, rounded to 2 decimals. Also calculate without a loop,each gene’s percentage of the total count, rounded to 1 decimal.
a = np.array([100, 200, 300, 400, 500]) #gives the expression count of genes
log_values=np.round(np.log2(a),2) #calculate the log2 of each element
print("log2 of each element is ",log_values)
percentage=np.round((a/np.sum(a))*100,1) #Gene's percentage wr to the total count
print("Each gene's percentage with respect to the total count is",percentage)


#(10) A culture starts with 100 cells and doubles every 20 minutes. Use np.arange() to make an array of time points 0, 20, 40 . . . 120 minutes. Calculate the population at each time with one expression: 100*2**(t/20). Print how many times larger the final population is than the starting one. Print the time points at which the population is over 1000.
a=np.arange(0,121,20)
print("Time:",a)
population=np.array(100*2**(a/20))
print("Population:",population)
print("Final population is",population[-1] / population[0],"times the initial population")
print("Time points where population > 1000:",a[population > 1000])


#(11) One-Hot Encoding DNA Sequences: Machine learning models cannot ”read” strings like ”GATTACA”. We convert them into a matrix where each base is represented by a vector (e.g., A = [1,0,0,0], C = [0,1,0,0], etc.). The Task: Create a NumPy array for a DNA sequence where each row represents a base and each column represents A, C, G, or T.
input_sequence="GATTACA"
mapping={'A':[1,0,0,0],'T':[0,1,0,0],'G':[0,0,1,0],'C':[0,0,0,1]} #dictionary with one-hot encoding for the nucleotides
print("The one-hot encoding of the input sequence is:\n",np.array([mapping[base] for base in input_sequence]))


#(12) Analyzing Gene Expression ”Heatmaps”: You have a matrix representing the expression of 5 genes across 10 different tissue samples. Create a 5 x 10 array of random floats between 0 and 100 using np.random.rand. Subtract the mean of each gene (row) from its values so the average expression for every gene is 0. Identify which samples (columns) have a total expression (sum) greater than a specific threshold.
a=np.random.rand(5,10)*100
mean=np.mean(a,axis=1,keepdims=True) #mean of each gene(row)
b=a-mean #Subtract the mean of each gene (row) from its values
total_expression=np.sum(b,axis=0) #total expression=sum of the columns
Threshold=50
print("The matrix is:\n",a)
print("The mean of each gene is:\n",mean)
print("Mean-centred expression matrix:\n",b)
print("Total expression of each column is:\n",total_expression)
print("Samples matching threshold (>50):\n",np.where(total_expression>Threshold)[0]) #np.where(condition) gives a tuple as output. np.where(condition)[0] unpacks the tuples and gives the indices where the condition is true.
print("Expression data for matching samples:\n",b[:,total_expression>Threshold])