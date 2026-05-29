import numpy as np

a = np.array([1,2,3])

print(a + 10)


#fast numpy vectorization
arr = np.array([1,2,3,4])

print(arr * 2)

#matrix multiplication
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.dot(a,b))

#Axis Concept
arr = np.array([[1,2],[3,4]])

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

#Reshape
arr = np.array([1,2,3,4,5,6])

print(arr.reshape(2,3))

#Random Module
arr = np.random.rand(3)
print(arr)

arr = np.random.randint(1,10,5)
print(arr)

#Statistics
arr = np.array([10,20,30,40])

print(np.mean(arr))
print(np.std(arr))