#importing the plotting library from the matplotlib and renaming that as plt for convenience
from operator import sub
from matplotlib import colors
import matplotlib.pyplot as plt 
import numpy as np

data={
    'English':80,
    'French':98,
    'Maths':75,
    'Physics':91,
    'Chemistry':84,
}

subjects=data.keys()
marks=data.values()

plt.bar(subjects,marks)
plt.show()

plt.bar(subjects,marks)
plt.ylim([0,100])
plt.show()


#with colors
colors_array=['red','green','purple','yellow','orange']
plt.bar(subjects,marks, color=colors_array, hatch="/")
plt.ylim([0,100])
plt.show()

#with hatches
plt.bar(subjects,marks, hatch="/")
plt.ylim([0,100])
plt.show()

#Bar Chart Options
plt.bar(subjects,marks, hatch="/", width=0.8, edgecolor='red', linewidth=2)
plt.ylim([0,100])
plt.show()


#Grouping bar charts
student_1={
    'English':80,
    'French':98,
    'Maths':75,
    'Physics':91,
    'Chemistry':84,
}

student_2={
    'English':94,
    'French':68,
    'Maths':81,
    'Physics':72,
    'Chemistry':80,
}

subjects=student_1.keys()
marks_1=student_1.values()
marks_2=student_2.values()

X=np.arange(len(subjects))
plt.bar(X+0.2,marks_2, hatch="/", width=0.4, color='green', edgecolor='black', label="Student 1")
plt.bar(X-0.2,marks_1, hatch="o", width=0.4, color='orange', edgecolor='black', label="Student 2")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Comparing and grouping two values in bar graph")
plt.xticks(X, subjects)
plt.legend()
plt.show()