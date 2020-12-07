#import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation,Dropout
from tensorflow.keras.constraints import max_norm
#from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report,confusion_matrix

#import csv and read from web url (kaggle.com)
df = pd.read_csv('https://storage.googleapis.com/kagglesdsdata/datasets/907215/1538467/Parkinsson%20disease.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201207%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201207T032536Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=5c02bd30f6908f2fb7b8f41c8a1edf61acc754f8b4091d216d3625fba7078f075c2e89b02ede39af341edec0acb73a8e9eb814cc5eb6924a9303e4df11bd272aca9ab6261d52b88f9b844b7833f05ec027bbd884ee385800d0e58216c2c8e81053386346048df8bb438efd7da33209a3892910ab30222207709e3b307cd78f2ec197a8b8546adc83b2383c5448a193eb73a26f885b505b8d45d6625ee8bbe1b156fbfaff23f309b1898357a81b3a8d644eb6cb3ea92b0ffa19bc6bb26c502643ecbbf166ebb419cc3c80b935f646c1f57730ff2ec3578f6769299ee3fb82bf87560b2f575603152d98d0be55e5e8a3ac3a2bc43806e366fe755859f436366319')
df=df.drop('name',axis=1)
#display correlation between other varialles/features to status of Parkinson's
df.corr()['status'].sort_values()[:-1].plot(kind='bar')

#set features data and status data
X = df.drop('status',axis=1).values
y = df['status'].values

#split training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)

#normalise data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#prevent overfit
early_stop=EarlyStopping(monitor='val_loss',mode='min',patience=15,verbose=1)

#build deep learning model layers and compile model
model = Sequential()

# input layer
model.add(Dense(22,  activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(18, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.2))

# hidden layer
model.add(Dense(5, activation='relu'))
model.add(Dropout(0.2))

# output layer
model.add(Dense(units=1,activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam')

#fit model
model.fit(x=X_train, 
          y=y_train, 
          epochs=400,
          batch_size=64,
          validation_data=(X_test, y_test),
          callbacks=[early_stop]
          )

#plot loss during fitting of model
losses = pd.DataFrame(model.history.history)
losses[['loss','val_loss']].plot()

#display accuracy report of model
predictions = model.predict_classes(X_test)
print(classification_report(y_test,predictions))

#confusion matrix between predictioned status from model and true status
print(confusion_matrix(y_test,predictions))