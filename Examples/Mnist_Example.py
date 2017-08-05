# -*- coding: utf-8 -*-
# Author: Kotobuki



############### Only add this to your code #####################
from Keras_FB import main as fb 
################################################################


import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

##data preprocess
(X_train, y_train), (_, _) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], -1) / 255.
y_train = np_utils.to_categorical(y_train, num_classes=10)
##modeling
model = Sequential()
model.add(Dense(32, input_dim=784))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
model.compile(optimizer="RMSprop",
              loss='categorical_crossentropy',
              metrics=['accuracy'])
##fitting
model.fit(X_train, y_train, epochs=2, batch_size=32,



	############### Only add this to your code #####################
	callbacks=[fb.sendmessage(savelog=True,
		fexten='TEST',
		username='PutYourUsernameIn', #facebook username
		password='PutYourPasswordIn')] #facebook password
	################################################################
	



	)
