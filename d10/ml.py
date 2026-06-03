#Supervised learning(regression)
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3,4]).reshape(-1,1)
y = np.array([10,20,30,40])

model = LinearRegression()
model.fit(x,y)

prediction = model.predict([[5]])
print("predicted marks:",prediction[0])


#classification
from sklearn.tree import DecisionTreeClassifier

x = [[1],[2],[3],[4],[5],[6]]
y = ["fail","fail","fail","pass","pass","pass"]

model = DecisionTreeClassifier()
model.fit(x,y)
prediction = model.predict([[7]])
print("prediction:",prediction[0])

#Unsupervised Learning
from sklearn.cluster import KMeans
import numpy as np

x = np.array([[20,2000],[22,2500],[15,15000],[55,17000]])

model = KMeans(n_clusters=2, random_state=42)
model.fit(x)
print(model.labels_)

#Reinforcement Learning
score = 0
action = "correct"

if action == "correct":
    score += 10
    print("reward +10")
else:
    score -= 5
    print("penalty -5")

print("score:",score)


#linear regression
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3,5,6]).reshape(-1,1)
y = np.array([10,20,30,50,60])

model = LinearRegression()
model.fit(x,y)
prediction = model.predict([[4]])
print(prediction[0])

#logistic regression
from sklearn.linear_model import LogisticRegression
import numpy as np

x = np.array([1,2,3,4,5,6,8,9,]).reshape(-1,1)
y = np.array([0,0,0,1,1,1,1,1])

model = LogisticRegression()
model.fit(x,y)

prediction = model.predict([[7]])
print("predicted:",prediction[0])
