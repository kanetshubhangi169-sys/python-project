#pie diagram
import numpy as np
import matplotlib.pyplot as plt

y = np.array([10,20,30,40])
plt.pie(y)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

y = np.array([10,20,30,40])
mylabels = ["apple","banana","graps","chikoo"]
plt.pie( y, labels = mylabels)
plt.show()

#line & ring diagram
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,8])
y = np.array([3,10])
plt.plot(x, y,'o')
plt.plot(x,y)
plt.show()

#line diagram
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])
plt.plot(x,y)
plt.show()

#bar chart
import numpy as np
import matplotlib.pyplot as plt

x = np.array(["a","b","c","d"])
y = np.array([3,8,1,10])
plt.bar(x,y)
plt.show()


#harizontal chart
import numpy as np
import matplotlib.pyplot as plt

x = np.array(["a","b","c","d","e","f"])
y = np.array([4,7,2,9,10,12])
plt.barh(x,y, color = "yellow", height = 0.5)
plt.show()

#bar diagram
import numpy as np
import matplotlib.pyplot as plt

x = np.array([50,60,90,70])
mylabels = ["seeta","reeta","veena","meeta"]


plt.bar(x, mylabels)
plt.show()

#adding title
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 10, 15]

plt.plot(x, y)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

#adding grid
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y)

plt.grid()

plt.show()


#apply app function
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y,
         color="green",
         linestyle="--",
         marker="o")

plt.title("Sales Graph")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid()

plt.show()

#pie chart
import matplotlib.pyplot as plt

data = [40, 30, 20, 10]
labels = ["Python", "Java", "C++", "JS"]

plt.pie(data, labels=labels)

plt.show()

import matplotlib.pyplot as plt

x = [1,2,3]

y1 = [10,20,30]
y2 = [15,25,35]

plt.plot(x, y1, label="Product A")
plt.plot(x, y2, label="Product B")

plt.legend()

plt.show()