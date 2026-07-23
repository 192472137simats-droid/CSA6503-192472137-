import matplotlib.pyplot as plt

labels = ['CS', 'EEE', 'MECH', 'CIVIL']
sizes = [40, 25, 20, 15]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Department Distribution")
plt.show()
