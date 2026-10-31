with open("stringmatrix.dat.txt","w") as f:
    for i in range(65,77,4):
        print(chr(i),chr(i+1),chr(i+2),chr(i+3),file=f)
