######################################## Exploring Data with Python#######################


import numpy as np

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)



print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)

print(grades.shape)
print(grades[0])
print(grades.mean())

# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
print (student_data)

# Show shape of 2D array
print (student_data.shape)

# Show the first element of the first element
print(student_data[0][0])

# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:2f}\nAverage grade: {:2f}'.format(avg_study, avg_grade))


## ##############################Exploring tabular data with Pandas################

import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                                     'StudyHours': student_data[0],
                                     'Grade': student_data[1]})
# Get the data for index Value 5 
print(df_students.loc[0])

# Get the rows with index values 0 to 5 * notice its using iloc so using 0-4 instead of 0-5
print(df_students.iloc[0:5])

print('---')
print(df_students.iloc[0, [1,2]])

print('---')
print(df_students.loc[0, 'Grade'])

#Here's another useful trick. You can use the loc method to find indexed rows based on a 
#filtering expression that references named columns other than the index, like this:
print('--- ')
print(df_students.loc[df_students['Name']=='Aisha'])

print('--- ')
print(df_students[df_students['Name']=='Aisha'])

print('------')
print(df_students.query('Name=="Aisha"'))

print('------')
print(df_students[df_students.Name == 'Aisha'])

##################################### Loading a DataFrame from a file ####################
# !wget doesnt work. you have to use cURL -0 then URL
# cURL -o grades.csv https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv

print('------')

df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
print(df_students.head())

print('------')
print (df_students.isnull())

print('------')
print (df_students.isnull().sum())

print('------')
print (df_students[df_students.isnull().any(axis=1)])

print('------')
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
print(df_students)

print('------')
df_students = df_students.dropna(axis=0, how='any')
print(df_students)


################################ Explore data in the DataFrame########################

#Get the mean study hours using to column name as index
mean_study = df_students['StudyHours'].mean()

#Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

#Print the mean study hours and mean grade
print('Average Weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# Get students who studied for the mean or more hours
print('------')
print(df_students[df_students.StudyHours > mean_study])

# What was their mean grade?
print('------')
df_students[df_students.StudyHours > mean_study].Grade.mean()

print('------')
passes = pd.Series(df_students.Grade >= 60)
df_students = pd.concat([df_students, passes.rename('Pass')], axis=1)
print(df_students)

print('------')
print(df_students.groupby('Pass').Name.count())

print('------')
print(df_students.groupby(df_students.Pass)['StudyHours', 'Grade'].mean())

print('------')
df_students = df_students.sort_values(by='Grade', ascending=False)
print(df_students)

#********************************* 
#Summary
#That's it for now!

#Numpy and DataFrames are the workhorses of data science in Python. They provide us ways to load, explore, and analyze tabular data. As we will see in subsequent modules, 
# even advanced analysis methods typically rely on Numpy and Pandas for these important roles.

