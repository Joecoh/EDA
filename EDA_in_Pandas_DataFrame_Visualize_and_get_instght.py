import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Email_ID': [1, 2, 3, 4, 5, 6],
    'Sender': ['A@gmail.com', 'B@yahoo.com', 'C@gmail.com', 'A@gmail.com', 'D@outlook.com', 'A@gmail.com'],
    'Subject_Length': [30, 45, 15, 25, 60, 20],
    'Spam': ['No', 'Yes', 'No', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
print(df)

print(df.describe(), "\n")
print("Most Active Sender:\n", df['Sender'].value_counts().head(1), "\n")

# Visualization 1: Spam vs Non-Spam
df['Spam'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Spam vs Non-Spam Emails')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Visualization 2: Avg subject length by spam status
df.groupby('Spam')['Subject_Length'].mean().plot(kind='bar', color=['green', 'red'])
plt.title('Average Subject Length (Spam vs Non-Spam)')
plt.ylabel('Avg Length')
plt.show()
