import numpy as np
import pandas as pd

marks = np.array([[85, 90, 78],
                  [88, 76, 92],
                  [80, 85, 88]])
print("=== NumPy Array (Marks of 3 Students in 3 Subjects) ===")
print(marks, "\n")


print("Average marks of each student:", np.mean(marks, axis=1))
print("Highest mark in each subject:", np.max(marks, axis=0), "\n")

#  Convert to Pandas DataFrame
students = ['Rohit', 'Neha', 'Imran']
subjects = ['Maths', 'Science', 'English']

df = pd.DataFrame(marks, index=students, columns=subjects)
print("=== Pandas DataFrame ===")
print(df, "\n")

# Work with DataFrame
print("Average marks per subject:\n", df.mean(), "\n")
print("Students who scored above 85 in Maths:\n", df[df['Maths'] > 85], "\n")

# Add a new column using NumPy operation
df['Total'] = np.sum(marks, axis=1)
print("=== DataFrame with Total Marks ===")
print(df)
