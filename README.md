# Keras Messenger
![Slogan](https://raw.githubusercontent.com/kotobukki/Keras_FB/master/slogan.png)

The Python library enable Keras to send real-time training data to your Messenger account

[WTF is Keras??](https://github.com/fchollet/keras/blob/master/README.md)

Installation
-----
```
pip install Keras_FB
```
Usage
-----
Add following line for importing the library
```
from Keras_FB import main as fb 
```

Add following line in fitting process
```
callbacks=[fb.sendmessage(savelog=True,
  fexten='TEST',
	username='PutYourUsernameIn', #facebook username
	password='PutYourPasswordIn')] #facebook password
```
The fitting part's code should now looks like this
```
model.fit(X_train, Y_train, epochs=epoch, batch_size=batch,
	callbacks=[fb.sendmessage(savelog=True,
		fexten='TEST',
		username='PutYourUsernameIn', #facebook username
		password='PutYourPasswordIn')] #facebook password
)
```
Example
-----
[Mnist Example](https://github.com/kotobukki/Keras_FB/blob/master/Examples/MNIST/MNIST_Example.py)

Results:

![Results](https://raw.githubusercontent.com/kotobukki/Keras_FB/master/Examples/MNIST/Mnist_Example.jpg)

Contributions
-----
Idea by Coldwings

Original Code by QuantumLiu

Modified by Kotobukki
