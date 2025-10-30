import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Email_ID': [1, 2, 3, 4, 5, 6],
    'Sender': ['A@gmail.com', 'B@yahoo.com', 'C@gmail.com', 'A@gmail.com', 'D@outlook.com', 'E@gmail.com'],
    'Subject_Length': [30, 45, 15, 25, 60, 20],
    'Spam': ['No', 'Yes', 'No', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)


print(df.describe(), "\n")
print("Spam Count:\n", df['Spam'].value_counts(), "\n")

# Bayesian Analysis (simple version)
# Prior: assume 50% chance of spam before seeing data
prior = 0.5
# Likelihood: observed proportion (from data)
likelihood = p_spam
# Posterior (updated belief) = (prior * likelihood) / normalization
posterior = (prior * likelihood) / ((prior * likelihood) + ((1 - prior) * (1 - likelihood)))
print(f"Bayesian Updated Probability of Spam Email: {posterior:.2f}")
