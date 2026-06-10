#logistic regression
from sklearn.linear_model import LogisticRegression
import numpy as np

x = np.array([1,2,3,4,5,6,8,9,]).reshape(-1,1)
y = np.array([0,0,0,1,1,1,1,1])

model = LogisticRegression()
model.fit(x,y)

prediction = model.predict([[7]])
print("predicted:",prediction[0])


#linear regression
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3,5,6]).reshape(-1,1)
y = np.array([10,20,30,50,60])

model = LinearRegression()
model.fit(x,y)
prediction = model.predict([[4]])
print(prediction[0])



