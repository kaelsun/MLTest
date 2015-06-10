
from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 1.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inx, dataset, labels, k):
    dataSetSize = dataset.shape[0]
    diffMat = tile(inx, (dataSetSize,1)) - dataset
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    array0Lines = fr.readlines()
    numberOfLines = len(array0Lines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in array0Lines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0 : 3]
        classLabelVector.append(int(round(float(listFromLine[-1]))))
        index += 1
    return returnMat, classLabelVector
