import matplotlib.pyplot as plt

students = ['Aarav', 'Diya', 'Kabir', 'Sanya', 'Vikram']
marks = [85, 92, 78, 88, 95]

plt.plot(students, marks, marker='o', color='blue')
plt.title("Student Marks - Line Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.bar(students, marks, color='green')
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.pie(marks, labels=students, autopct='%1.1f%%', startangle=140)
plt.title("Marks Distribution - Pie Chart")
plt.show()
