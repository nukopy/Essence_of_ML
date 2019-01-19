from linearreg import LinearRegression
import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split


# load input
wine_data = []
with open(file='input/winequality-red.csv', mode='r', encoding='utf-8') as f:
    for row in csv.reader(f, delimiter=';'):
        wine_data.append(row)
labels = wine_data[0]

for i, label in enumerate(labels):
    labels[i] = label.replace(' ', '_')

df = pd.DataFrame(data=wine_data[1:], columns=labels, dtype=np.float64)
X = df.values[:, :-1]
y = df.values[:, -1]


# split data to train & test
random_state = 0
X_test, X_train, y_test, y_train =\
    train_test_split(X, y, test_size=0.25, random_state=random_state)

# train
model = LinearRegression()
model.fit(X_train, y_train)

# test
pre_y = model.predict(X_test)

for i in range(5):
    print('Ans: {:1.0f}, Predict: {:5.3f}'.format(y_test[i], pre_y[i]))
print()

# RMSE: Root of Mean Square Error
# RMSE is often used to evaluate predicted-value.
rmse = np.sqrt(((y_test - pre_y)**2).mean())
print('RMSE: {}'.format(rmse))
