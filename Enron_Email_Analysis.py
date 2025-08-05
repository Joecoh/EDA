import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("emails.csv")

def cleanemail(email_text):
    return ' '.join([line.strip() for line in email_text.splitlines()][15:])

df['email_body'] = df['message'].apply(cleanemail)

print(df.head())

df['folder_name'] = df['file'].apply(lambda x: x.split('/')[1] if '/' in x else x)

folder_counts = df['folder_name'].value_counts().reset_index()
folder_counts.columns = ['folder_name', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(x='count', y='folder_name', data=folder_counts.iloc[:20], palette="Blues_d")
plt.title("Top 20 folders")
plt.xlabel("Count")
plt.ylabel("Folder Name")
plt.show()

df['Employee_name'] = df['file'].apply(lambda x: x.split('/')[0] if '/' in x else x)

employee_counts = df['Employee_name'].value_counts().reset_index()
employee_counts.columns = ['Employee_name', 'Counts']

plt.figure(figsize=(10, 8))
sns.barplot(y="Employee_name", x="Counts", data=employee_counts.iloc[:20], palette="Blues_d")
plt.title("Top 20 highest email sender employee")
plt.xlabel("Count")
plt.ylabel("Employee name")
plt.show()
