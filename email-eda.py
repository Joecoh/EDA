import pandas as pd
import matplotlib.pyplot as plt

# Create a small sample email dataset
data = {
    'Email_ID': [1, 2, 3, 4, 5],
    'Sender': ['A@gmail.com', 'B@yahoo.com', 'C@gmail.com', 'A@gmail.com', 'D@outlook.com'],
    'Subject_Length': [30, 45, 15, 25, 60],
    'Spam': ['No', 'Yes', 'No', 'No', 'Yes']
}

# Load into a pandas DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Sample Email Dataset:\n", df, "\n")

# Basic EDA
print("Basic Info:")
print(df.info(), "\n")

print("Summary Statistics:")
print(df.describe(), "\n")

print("Spam Count:\n", df['Spam'].value_counts(), "\n")

# Simple visualization
df['Spam'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Spam vs Non-Spam Emails')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()
