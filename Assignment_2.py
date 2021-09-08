import numpy as np
import pandas as pd

csv_file=input("Enter the name of your data file:")
train_file=pd.read_csv(csv_file)
df=pd.DataFrame(train_file)
#print("Training file")
#print(df)

m_train=df.iloc[[0],[0]]
print("Rows in training data")
print(m_train)

features_train=df.iloc[[0],[1]]
print("Features in training data:")
print(features_train)

Y_train=df.iloc[1:,[-1]]
#print("Output of training data:")
#print(Y_train)

df.insert(loc=0,column='W0',value=1.0)
X_train=df.iloc[1:,0:-1]
#print("Input for training data:")
#print(X_train)

A=np.linalg.pinv(np.dot(X_train.T,X_train))
B=np.dot(X_train.T,Y_train)
W=np.dot(A,B)

C=np.dot(X_train,W)-Y_train
J_train=(1/m_train)*np.dot(C.T,C)
print("Weights:")
print(W)
print(W.shape)
print("Cost function of training data:")
print(J_train)

csv_file=input("Enter the name of your test file:")
test_file=pd.read_csv(csv_file)
df_test=pd.DataFrame(test_file)
#print("Test file:")
#print(df_test)

m_test=df_test.iloc[[0],[0]]
print("Rows in test data:")
print(m_test)

features_test=df_test.iloc[[0],[1]]
#print("Features in test data:")
#print(features_test)

Y_ground=df_test.iloc[1:,[-1]]

df_test.insert(loc=0,column='W0',value=1.0)
X_test=df_test.iloc[1:,0:-1]
#print("Testing input:")
#print(X_test.shape)
#print(X_test)

Y_test=np.dot(X_test,W)
print("Predicted output:")
print(Y_test)

D=np.dot(X_test,W)-Y_ground
J_test=(1/m_test)*np.dot(D.T,D)
print("Cost function of testing data:")
print(J_test)
