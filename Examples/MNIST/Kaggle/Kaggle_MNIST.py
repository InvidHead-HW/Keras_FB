import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import pandas
from Keras_FB import main as fb 
#loading data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], -1) / 255. 
X_test = X_test.reshape(X_test.shape[0], -1) / 255.   
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)
#print X_train
k = pandas.read_csv("/Users/abc/Downloads/test.csv",header=None,low_memory=False).as_matrix() 

##################################Start
model = Sequential()
model.add(Dense(100, input_dim=784))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
model.compile(optimizer='RMSprop',
          loss='categorical_crossentropy')

model.fit(X_train, y_train, epochs=1, batch_size=32,
	callbacks=[fb.sendmessage(savelog=True,
		fexten='TEST',
		username='shoucf', #facebook username
		password='TestingtesterTestin2333333')] #facebook password
	)
loss, accuracy = model.evaluate(X_test, y_test)

print('test loss: ', loss)
print('test accuracy: ', accuracy)
i = 1
b = 1
while i <= 28001:
	b = b + 1
	result = model.predict(k[i:b])
	
	ni = 0
	while ni <= 9:
		if result[0][ni] == 1:
			print i,",",ni 
			break
		ni = ni +1
		if ni == 10:
			print "error"

	i = i + 1