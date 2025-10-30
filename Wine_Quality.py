import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'fixed acidity': [7.4, 7.8, 7.3, 7.9, 8.2],
    'volatile acidity': [0.70, 0.88, 0.65, 0.76, 0.60],
    'citric acid': [0.00, 0.00, 0.02, 0.04, 0.30],
    'residual sugar': [1.9, 2.6, 2.3, 2.0, 1.8],
    'density': [0.9978, 0.9968, 0.9970, 0.9969, 0.9956],
    'alcohol': [9.4, 9.8, 9.5, 10.0, 11.0],
    'quality': [5, 5, 6, 6, 7]
}

wine = pd.DataFrame(data)
print("Wine Quality Dataset:\n", wine, "\n")

print("Summary Statistics:\n", wine.describe(), "\n")

print("Missing Values:\n", wine.isnull().sum(), "\n")

sns.heatmap(wine.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap - Wine Quality")
plt.show()

sns.barplot(x='quality', y='alcohol', data=wine)
plt.title("Alcohol vs Wine Quality")
plt.show()
