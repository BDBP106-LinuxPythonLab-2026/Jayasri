#To print 2D array of list of lists
with open("stringmatrix.dat.txt","r") as f:
    grid=[line.split() for line in f]
print("2D array of list of lists is:")
print(grid)

#To find the number of rows and columns in the matrix
rows=len(grid)
columns=len(grid[0])
print("Number of rows= ",rows)
print("Number of columns= ",columns)

#To print a list that contains lists of columns of the above matrix
column_lists=[]
for i in range(columns):
    col=[]
    for j in range(rows):
        col.append(grid[j][i])
    column_lists.append(col)
print("List that contains lists of columns of the matrix is:")
print(column_lists)

#To print a list that prints the diagonal elements read in one direction
diagonal=[]
for k in range(rows+columns-1):
    diag=[]
    for i in range(rows):
        j=k-i
        if 0<=j<columns:
            diag.append(grid[i][j])
    diagonal.append(diag)
print("Diagonal elements of the matrix is:")
print(diagonal)
