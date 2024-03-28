import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import metrics

names=['sepal-length','sepal-width','petal-length','petal-width','Class']

df=pd.read_csv("C:\\Users\student\Desktop\python suhail\iris\iris.data",names=names)
print(df.head)

x=df.iloc[:,0:4]

y=df[["Class"]]
# #print(x)
# #print(y)

#le =prefit_processing.LabelEncoder()
# y=y.apply(le.transform)
# #print(y)

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.20)

# #feature scaling
# scaler=preprocessing.StandardScaler().fit(X_train)
# X_train=scaler.transform(X_train)
# X_test=scaler.transform(X_test)

# #training and predications
# mlp=MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=1000)
# mlp.fit(X_train,Y_train.values.ravel())
# predications=mlp.predict(X_test)
# print(predications)


# print(confusion_matrix(y_test,predications))
# print(classification_report(y_test,predications))

