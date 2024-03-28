import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import confusion_matrix,classification_report,mean_squared_error


names=['fixed acidity', 'volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','ph','sulphates','alchol','quality']

df=pd.read_csv("C:\\Users\student\Desktop\python suhail\wine+quality\winequality-red.csv",sep=';')
#print(df.head)

x=df.iloc[:,0:11]
y=df[["quality"]]
y=y.to_numpy().ravel()


#print(x)
#print(y)

#le=preprocessing.LabelEncoder()
#y=y.apply(le.fit.transform)
#print(y)

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.20)



#feature scaling

scaler=preprocessing.StandardScaler().fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

# #training and predications
# mlp=MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=1000)
# mlp.fit(X_train,Y_train.values.ravel())
# predications=mlp.predict(X_test)
# print(predications)

regr = MLPRegressor(random_state=1, max_iter=1000).fit(X_train, Y_train)
regr.predict(X_test[:2])
print(regr.score(X_test, Y_test))
predications=regr.predict(X_test)
print(mean_squared_error(Y_test,predications))
# print(classification_report(Y_test,predications))


