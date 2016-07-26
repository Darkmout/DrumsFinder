import os
import fractions
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Convolution1D, Convolution2D, MaxPooling2D
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.optimizers import SGD
import numpy as np

  
def getLSTMModel(inputShape=(1,1), outputLength=1):
    model = Sequential()
    model.add(LSTM(512, return_sequences=True, input_shape=inputShape))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(outputLength))
    model.add(Activation('sigmoid'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    
    return model

#thanks https://github.com/kaggle-novice/mnist_keras/blob/master/mnist-keras.py
def getConvModel(inputShape=(1,1), outputLength=1):
    # Sequential wrapper model
    model = Sequential()

    # convolutional layers
    model.add(Convolution2D(64, inputShape[0]/10 , inputShape[1]/10, border_mode='valid', input_shape=(1, inputShape[0], inputShape[1])))
    model.add(Activation('relu'))
    model.add(Convolution2D(32, inputShape[0]/10, inputShape[1]/10))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))


    # convert convolutional filters to flatt so they can be feed to
    # fully connected layers
    model.add(Flatten())

    # fully connected layers
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(outputLength))
    model.add(Activation('sigmoid')) #using sigmoid as softmax doesn't work for multilabel

    # setting sgd optimizer parameters
    #sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

    return model

def trainModel(model, song, maxLength):

    X_train = [[song[i] for i in range(start, start + maxLength) ] for start in range(0, len(song)-maxLength)]
    Y_train = [song[i] for i in range(maxLength, len(song))]
    
    model.fit(X_train, Y_train, nb_epoch=5, batch_size=32)
    
def testModel(model, X, Y):

    classes = model.predict_classes(X, batch_size=1)
    proba = model.predict_proba(X, batch_size=1)

    print Y
    print classes
    print proba
    print

def loadWeights(path, model):
    if os.path.isfile(path):
        model.load_weights(path)

def saveWeights(path, model):
    if os.path.isfile(path):
        model.save_weights(path)