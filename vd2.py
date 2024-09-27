import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
data = pd.read_csv("D:\Workspace\Học máy thống kê\datavd2.csv")

x = data[['trọng lượng', 'âm lượng']]
y = data['CO2']
regr = linear_model.LinearRegression()
regr.fit(x,y)

predictedCO2 = regr.predict([[2300,1300]])
print(predictedCO2)