#vector
import numpy as np

student1 = np.array([20, 170, 65])
student2 = np.array([21, 175, 70])

result = student1 + student2

print(result)


#multiplication
import numpy as np

v = np.array([2, 3])

print(v * 2)


#Matrices
import numpy as np

students = np.array([[20,170,65],[21,175,70],[19,165,60]])

print(students)

#matrix shape
import numpy as np

students = np.array([
    [20,170,65],
    [21,175,70],
    [19,165,60]
])

print(students.shape)

#dot product
import numpy as np

A = np.array([1,2])
B = np.array([3,4])

result = np.dot(A,B)

print(result)