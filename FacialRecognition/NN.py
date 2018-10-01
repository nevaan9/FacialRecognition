import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
import xlrd

input_file = "dataset.csv"
k = pd.read_csv(input_file, header=0)
numpyArray = k.as_matrix()
columnSize = len(numpyArray[0])

#function to slice dataset
def cutDataSet(rowStart, rowEnd, columnStart, columnEnd, dataset):
    '''
    :param start: Start value of a dataset
    :param end: where you want to end slicing
    :param dataset: takes any numpy array. (2D array)
    :return: returns a sliced numpy array with start and ending points
    '''

    returnArray = []

    for i in range(rowStart,rowEnd):
        tempArray = []
        for j in range(columnStart, columnEnd):
            tempArray.append(dataset[i][j])
        returnArray.append(tempArray)

    return returnArray


#divide into train and test datasets
trainX1 = cutDataSet(0, 109//2, 30, len(numpyArray[0]), numpyArray)
trainX2 = cutDataSet(110, (196//2)+109, 30, len(numpyArray[0]), numpyArray)
trainX3 = cutDataSet(109+196+1, (109//2)+(109+196), 30, len(numpyArray[0]), numpyArray)
trainX4 = cutDataSet(109+196+109, (183//2)+(109+196+109), 30, len(numpyArray[0]), numpyArray)
finalTrainX = trainX1 + trainX2 + trainX3 + trainX4

testX1 = cutDataSet(109//2, 109, 30, len(numpyArray[0]), numpyArray)
testX2 = cutDataSet((196//2)+109, 110+196, 30, len(numpyArray[0]), numpyArray)
testX3 = cutDataSet((109//2)+(109+196), 109+196+1+109, 30, len(numpyArray[0]), numpyArray)
testX4 = cutDataSet((183//2)+(109+196+109), len(numpyArray), 30, len(numpyArray[0]), numpyArray)
finalTestX = testX1 + testX2 + testX3 + testX4


trainY1 = cutDataSet(0, 109//2, 1, 2, numpyArray)
trainY2 = cutDataSet(110, (196//2)+109, 1, 2, numpyArray)
trainY3 = cutDataSet(109+196+1, (109//2)+(109+196), 1, 2, numpyArray)
trainY4 = cutDataSet(109+196+109, (183//2)+(109+196+109), 1, 2, numpyArray)
trainY = trainY1 + trainY2 + trainY3 + trainY4
finalTrainY = []
for anItem in trainY:
    for anItemin in anItem:
        finalTrainY.append(anItemin)

resultY1 = cutDataSet(109//2, 109, 1, 2, numpyArray)
resultY2 = cutDataSet((196//2)+109, 110+196, 1, 2, numpyArray)
resultY3 = cutDataSet((109//2)+(109+196), 109+196+1+109, 1, 2, numpyArray)
resultY4 = cutDataSet((183//2)+(109+196+109), len(numpyArray), 1, 2, numpyArray)
ResultY = resultY1 + resultY2 + resultY3 + resultY4
finalResultY = []
for anItem in ResultY:
    for anItemin in anItem:
        finalResultY.append(anItemin)


finalTrainX = np.array(finalTrainX)
finalTrainX = finalTrainX / np.max(finalTrainX, axis=0)

finalTestX = np.array(finalTestX)
finalTestX = finalTestX / np.max(finalTestX, axis=0)

#
mlp = MLPClassifier(hidden_layer_sizes=(30,30,30))
mlp.fit(finalTrainX,finalTrainY)
#
predict = mlp.predict(finalTestX)
#
print(len(finalTestX))
print(len(finalResultY))
print()
print(len(finalTrainX))
print(len(finalTrainY))

print(mlp.score(finalTestX, finalResultY))
print(finalResultY)
print(predict)