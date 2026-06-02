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



#probability
red_balls = 3
blue_balls = 5

total = red_balls + blue_balls

probability_red = red_balls/blue_balls

print("probability of red balls:",probability_red)
print("percentage:",probability_red * 100,"%")


#Bayes theorem
cricketers = 20
non_cricketers = 80

jersey_cricketers = 18
jersey_non_cricketers = 8

total_jersey = jersey_cricketers + jersey_non_cricketers

probability = jersey_cricketers / total_jersey

print("Probability of being a cricketer if wearing jersey:")
print(probability)
print(probability * 100, "%")