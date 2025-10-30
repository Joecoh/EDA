import pandas as pd

data = {
    'Name': ['Karan', 'Sneha', 'Ravi', 'Anjali', 'Deepak'],
    'Age': [24, 29, 21, 27, 26],
    'City': ['Bengaluru', 'Hyderabad', 'Jaipur', 'Ahmedabad', 'Chandigarh'],
    'Score': [88, 92, 75, 85, 80]
}
df = pd.DataFrame(data)

print(df, "\n")

print("Access single column (City):")
print(df['City'], "\n")

print("Access multiple columns (Name and Score):")
print(df[['Name', 'Score']], "\n")

print("Students with Score > 85:")
print(df[df['Score'] > 85], "\n")

print("Students from Bengaluru or Hyderabad:")
print(df[df['City'].isin(['Bengaluru', 'Hyderabad'])], "\n")
