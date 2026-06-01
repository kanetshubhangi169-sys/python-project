#mean
import numpy

num = [99,20,14,30,20,80]

x = numpy.mean(num)
print(x)

#median
import numpy

num = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(num)
print(x)

#variance
import numpy

num = [32,111,138,28,59,77,97]

x = numpy.var(num)
print(x)

#Standard deviation
import numpy

num = [32,111,138,28,59,77,97]

x = numpy.std(num)
print(x)


#correlation
import pandas as pd

study_hours = [1, 2, 3, 4, 5, 6]
marks = [20, 35, 50, 65, 80, 95]

df = pd.DataFrame({'Hours': study_hours,'Marks': marks})

correlation = df['Hours'].corr(df['Marks'])

print("Correlation =", correlation)



import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
marks = [20, 35, 50, 65, 80, 95]

plt.scatter(study_hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()



speed = [20, 40, 60, 80, 100]
time = [10, 5, 3.3, 2.5, 2]

df = pd.DataFrame({
    'Speed': speed,
    'Time': time
})

print(df['Speed'].corr(df['Time']))