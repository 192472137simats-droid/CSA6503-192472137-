import matplotlib.pyplot as plt

subjects = ['OS', 'DAA', 'NLP', 'RL']
marks = [85, 90, 78, 88]
plt.bar(subjects, marks, color='skyblue')
plt.title("Marks by Subject")
plt.show()
