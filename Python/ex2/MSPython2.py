
import pandas as pd
import numpy as np
import matplotlib


# Load data from a text file
#!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv
df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

# Calculate who passed, assuming '60' is the grade needed to pass
passes  = pd.Series(df_students['Grade'] >= 60)

# Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)


# Print the result out into this notebook
print(df_students)

#Ensure plots are displayed inline in the notebook
#%matplotlib inline


from matplotlib import pyplot as plt

#create a bar plot of name vs grade
#plt.bar(x=df_students.Name, height=df_students.Grade)

#Display the plot

#print(plt.show())

#create a bar plot of name vs grade
plt.bar(x=df_students.Name, height=df_students.Grade, color='orange')

# customize the chart
plt.title('Student Grades')
plt.xlabel('Student Name')
plt.ylabel('Grade')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(rotation=90)

#Display the plot

print(plt.show())