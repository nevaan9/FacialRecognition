import random

import numpy as np

class NeuralNetwork(object):

    def __init__(self, data):
        #Define HyperParameters
        self.inputValues = 2
        self.outputValues = 1
        self.hiddenLayers = 3
        self.data = data

        #Initialize the weights of the neural network
        self.w1 = np.random.randn(self.inputValues, self.hiddenLayers)
        self.w2 = np.random.randn(self.hiddenLayers, self.outputValues)

    # Forward propagete inputs through our network
    def forward(self):
        self.z2 = np.dot(self.data, self.w1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.w2)
        yHat = self.sigmoid(self.z3)
        return yHat


    # Apply the sigmoid activation function
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))

if __name__ == '__main__':

    y = np.array(([1, 2], [4, 5], [6,7]), dtype=int)
    x = NeuralNetwork(y)
    print(x.forward())
    print('\n')

    #Cool thing about numpy is that is applies the function to each element. Like map.
    print(x.sigmoid(np.array([-1,-2,4])))





