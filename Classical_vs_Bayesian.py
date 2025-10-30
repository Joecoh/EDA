import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Email_ID': [1, 2, 3, 4, 5, 6],
    'Sender': ['rahul@gmail.com', 'priya@yahoo.com', 'arjun@outlook.com', 'rahul@gmail.com', 'meena@rediffmail.com', 'vijay@gmail.com'],
    'Subject_Length': [25, 50, 30, 20, 60, 18],
    'Spam': ['No', 'Yes', 'No', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)
print("=== EMAIL DATASET ===\n", df, "\n")

# 2️⃣ EDA (Exploratory Data Analysis)
print("Summary Statistics:\n", df.describe(), "\n")
print("Spam Count:\n", df['Spam'].value_counts(), "\n")

# Visualization
df['Spam'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Spam vs Non-Spam Emails')
plt.xlabel('Email Type')
plt.ylabel('Count')
plt.show()

# Classical (Frequentist) Analysis
p_spam = (df['Spam'] == 'Yes').mean()
print(f"Classical Probability of Spam Email: {p_spam:.2f}")

# Bayesian Analysis
# Prior belief: 50% chance of spam before data
prior = 0.5
likelihood = p_spam

posterior = (prior * likelihood) / ((prior * likelihood) + ((1 - prior) * (1 - likelihood)))
print(f"Bayesian Updated Probability of Spam Email: {posterior:.2f}")
