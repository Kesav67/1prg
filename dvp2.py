import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Department':['CSE','ISE','ME','CE','CV'],
    'Students':[98,75,60,50,81]
}

df = pd.DataFrame(data)

plt.pie(df['data'], autopct = '%1.1f%', startangle = 120, color=['orange','lightgreen','red','blue','yellow'])
plt.title("Number of students in department",fontsize=14)
plt.label(df['Department'],color='black',fontsize=9)
plt.show()

