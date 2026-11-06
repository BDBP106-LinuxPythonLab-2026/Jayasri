import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Question1
#1. Plot activity against temperature as a line with circle markers.
temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5]) #relative activity
fig, ax = plt.subplots() #plt.plot(temps,activity,marker="o",label="Effect of Temperature on Activity")
ax.plot(temps, activity, marker='o')
ax.set_xlabel('Temperature (°C)',fontsize=9)
ax.set_ylabel('Activity',fontsize=9)
ax.set_title("Effect of Temperature on Activity",fontsize=9)
#2. Find the optimum temperature with temps[np.argmax(activity)], not by reading it off the data.
opt_temp=temps[np.argmax(activity)]
act_opt=np.max(activity)
print("The optimum temperature is:",opt_temp,"°C")
x,y=opt_temp,act_opt
#3. Mark it with a dashed vertical line (ax.axvline) and a text label pointing to the peak using ax.annotate(). Your plot should show: a rise and fall with the peak, and the label, at 50oC.
plt.axvline(opt_temp,linestyle="--",color="red")
plt.annotate("Optimal Temperature=50°C",(x,y),(51,93),color="red",fontsize=8)
plt.show()


#Question2
#1. Draw control and treated bars next to each other for each gene, with a legend.
genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])
barWidth=0.25
b1=np.arange(len(genes))
plt.bar(b1-barWidth/2,control,width=barWidth,color="yellow",label="Control")
plt.bar(b1+barWidth/2,treated,width=barWidth,color="violet",label="Treated")
plt.xlabel("Genes",fontsize=9)
plt.ylabel("Expression Level",fontsize=9)
plt.title("Gene Expression: Control vs Treated",fontsize=13)
plt.xticks(b1,genes)
plt.legend(fontsize=9)
plt.show()
#2. Print the fold change (treated/control) for each gene, rounded to 2 decimals.
fold_change=treated/control
print("Fold change:",np.round(fold_change,2))
print()
#3. Which gene roughly doubled, and which halved?
for gene, fc in zip(genes, fold_change):
    if fc >= 1.9:
        print(gene, "is doubled (Upregulated)")
    elif fc <= 0.5:
        print(gene, "is halved (Downregulated)")
    else:
        print(gene, "is unchanged")


#Question3
rng = np.random.default_rng(7)
length = rng.integers(50, 800, size=100) # amino acids
weight = length * 0.11 + rng.normal(0, 3, size=100) # kDa (about 110 Da per residue)
membrane = rng.random(100) < 0.3
plt.scatter(length[membrane],weight[membrane],color="red",marker="^",label="Membrane proteins",alpha=0.6)
plt.scatter(length[~membrane],weight[~membrane],color="blue",marker="o",label="Soluble proteins",alpha=0.6) #~membrane= not membrane proteins
plt.xlabel("Protein Length (amino acids)",fontsize=9)
plt.ylabel("Molecular Weight (kDa)",fontsize=9)
plt.title("Protein Length vs Molecular Weight",fontsize=13)
plt.legend()
plt.savefig("protein_size.png",dpi=150) #saves the image at 150dpi
plt.show()
#For displaying the saved image
img = plt.imread("protein_size.png") #imread-reads the image and converts them into a NumPy array
plt.imshow(img) #imshow-takes a 2D or 3D array and converts them into an image
plt.axis("off")
plt.show()


#Question4
rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72]
figure,axes=plt.subplots(2,2,sharex=True,sharey=True)
axes = axes.flatten()
for i in range(len(organisms)):
    gc=rng.normal(mean_gc[i],4,size=1000) #To generate 1000 GC values for each organism
    axes[i].hist(gc,bins=np.arange(0,101,2),edgecolor="black")
    axes[i].axvline(mean_gc[i],color="red",linestyle="--")
    axes[i].set_title(organisms[i] +" (Mean GC = " + str(mean_gc[i]) + "%)")
axes[2].set_xlabel('GC Content (%)')
axes[3].set_xlabel('GC Content (%)')
axes[0].set_ylabel('Frequency')
axes[2].set_ylabel('Frequency')
figure.suptitle('GC Content Distribution of Different Organisms')
plt.tight_layout() #automatically adjusts spacing
plt.savefig("question_4.png",dpi=150)
plt.show()
#sharex=Forces all designated subplots to use the exact same horizontal (X) range and tick marks.
#sharey= Forces all designated subplots to use the exact same vertical (Y) range and tick marks.


#Question5
df = pd.read_csv('diabetes.csv')
#(i) Print all the column names
print("Column names:")
print(df.columns.tolist())
#(ii) Print the first 10 rows
print("\nFirst 10 rows:")
print(df.head(10))
#(iii) Print the mean of the BloodPressure column values
print("\nMean Blood Pressure:",df['BloodPressure'].mean())
#(iv) Print the first 4 rows of columns 3,4,5
print("\nSelected columns:")
print(df.iloc[:4, [3, 4, 5]])
#(v) Add another column ’NormalizedBP’ using (max-min) normalization to the dataframe
BP = df['BloodPressure']
df['NormalizedBP'] = (BP - BP.min()) / (BP.max() - BP.min())
print("\nNormalized Blood Pressure:")
print(df[['BloodPressure', 'NormalizedBP']])
#(vi) Write a function categorize_age(age) that returns ”Youth”, ”Adult” or ”Senior” based on the age brackets (1-18, 19-50, ¿50). Create a new column in the dataframe with this function called age category.
def categorize_age(age):
    if 1 <= age <= 18:
        return "Youth"
    elif 19 <= age <= 50:
        return "Adult"
    else:
        return "Senior"
df['AgeCategory'] = df['Age'].apply(categorize_age)
print("\nAge Categories:")
print(df[['Age', 'AgeCategory']])


#Question6
x = np.linspace(-20, 20, 1000)
f1 = np.log(1 / np.cos(x)**2)
f2 = np.log(1 / np.sin(x)**2)
# Plot first function
plt.plot(x, f1, label='f1(x) = ln(1/cos²x)')
# Plot second function
plt.plot(x, f2, label='f2(x) = ln(1/sin²x)')
plt.xlabel('x')
plt.ylabel('Function Value')
plt.title('Logarithmic Trigonometric Functions')
plt.legend()
plt.grid()
plt.ylim(-2, 10)
plt.savefig("question_6.png",dpi=150)
plt.show()
#Both functions are periodic with a period of π. The function f1 has vertical asymptotes at x = π/2 + kπ, while f2 has vertical asymptotes at x = kπ.
#Both functions approach positive infinity near their respective singularities.


#Question7
x = np.linspace(-8, 8, 1000)
sigmas = [1, 1.5, 2] #standard deviations
for sigma in sigmas: #Gaussian distributions
    g = (1 / (sigma * np.sqrt(2 * np.pi))) * \
        np.exp(-(x**2) / (2 * sigma**2))
    plt.plot(x, g, label='Standard deviation= ' + str(sigma))
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Normalized Gaussian Distributions')
plt.legend()
plt.grid()
plt.show()