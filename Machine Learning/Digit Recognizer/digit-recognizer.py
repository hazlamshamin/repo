import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation,Dropout
from tensorflow.keras.constraints import max_norm
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report,confusion_matrix

#import and read csv from kaggle.com 
df = pd.read_csv('https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/3004/861823/compressed/train.csv.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1607606756&Signature=Uu8xFbsHrqkkKur9Tr4XLjnniDKYYp%2FzbEjSYf18azHZ5ASQQ%2BlloDyXDNZaqttm%2BmnceRcnfWQmMUxW2pDMtFsVvSV%2BF5U1Qdq31ANHTzxL9Lfv%2BeNusQ7akpGRMd36KeihiKlPH7ijB1QVzVKaJrdRrY%2FZ2mA39O0AttBlghqW8Qt2Ya0BhSTZavRgedgpJoglcTZXo8d8KHk6xSfR5lgMGfbBdv3ZPg7EZK4hruEpRE3fW1ra%2F29yTeKke%2BohbHg7es%2Bu3NkvMMHJs70IZk1p25MrGIV9vcw0CCxn2vzzkOF0GLP%2Bra5JrpASVEfSLbC27j6n8DDPbgGCi05aDA%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.csv.zip')

df.head()

#set features data and categorical data
X = df.drop('label',axis=1).values
y = df['label'].values

#split data into training set and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

#normalise data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#prevent overfitting
early_stop=EarlyStopping(monitor='val_loss',mode='min',patience=10,verbose=1)

#build model layers
model = Sequential()

# input layer
model.add(Dense(784,  activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(250, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(120, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(60, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(18, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.2))

# output layer
model.add(Dense(units=10,activation='softmax')) #10 different classes, 0-9

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam') #multiple class classification

#fit the model
model.fit(x=X_train, 
          y=y_train, 
          epochs=100,
          batch_size=128,
          validation_data=(X_test, y_test),
          callbacks=[early_stop]
          )

#plot loss progression during model fitting
losses = pd.DataFrame(model.history.history)
losses[['loss','val_loss']].plot()

#plot accuracy report
predictions = model.predict_classes(X_test)
print(classification_report(y_test,predictions))

#plot confusion matrix
confusion_matrix(y_test,predictions)