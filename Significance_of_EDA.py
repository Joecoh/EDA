import pandas as pd
import matplotlib.pyplot as plt

# Create a small dataset
data = {
    'Email_ID': [1, 2, 3, 4, 5, 6, 7],
    'Sender': ['A@gmail.com', 'B@yahoo.com', 'C@gmail.com', 'A@gmail.com', 'D@outlook.com', 'E@gmail.com', 'B@yahoo.com'],
    'Subject_Length': [30, 50, 10, 25, 70, 20, 55],
    'Spam': ['No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)

print("=== EMAIL DATASET ===\n", df, "\n")

# 1️⃣ EDA helps understand structure & missing values
print("=== BASIC INFO ===")
print(df.info(), "\n")

# 2️⃣ EDA helps summarize numeric data
print("=== SUMMARY STATISTICS ===")
print(df.describe(), "\n")

# 3️⃣ EDA helps find patterns
print("Spam Count:\n", df['Spam'].value_counts(), "\n")
print("Most Active Sender:\n", df['Sender'].value_counts().head(1), "\n")

# 4️⃣ Visualization: helps spot trends easily
df['Spam'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Spam vs Non-Spam Emails')
plt.xlabel('Email Type')
plt.ylabel('Count')
plt.show()

df.groupby('Spam')['Subject_Length'].mean().plot(kind='bar', color=['green', 'red'])
plt.title('Average Subject Length (Spam vs Non-Spam)')
plt.ylabel('Avg Length')
plt.show()
