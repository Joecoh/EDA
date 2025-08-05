import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Sender": ["John@gmail.com", "mary@gmail.com", "John@gmail.com", "Aadish@gmail.com", "Dhoncham@gmail.com"],
    "Receiver": ["mary@gmail.com", "mary@gmail.com", "Dharsham@gmail.com", "Aadish@gmail.com", "John@gmail.com"],
    "Subject": ["Meeting", "Meeting", "Meeting", "Meeting", "Meeting"],
    "Body": [
        "3pm Yes, Let's meet at 4",
        "OK, 3 pm works for me",
        "OK, let's meet at 5",
        "Let's meet?",
        "Sure, I'll be there"
    ]
}

df = pd.DataFrame(data)
sender_counts = df["Sender"].value_counts()

sender_counts.plot(kind="bar")
plt.xlabel("Sender")
plt.ylabel("Number of emails")
plt.title("Number of emails sent by each sender")
plt.show()
