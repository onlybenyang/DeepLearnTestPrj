#----
# K近邻算法
#----

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


#---------------------create data set-----------------------------------------
def createDataBase():
    group = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0., 0.],
        [0., 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
    

#----------------------------------------------------------------------
def classfiy (inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)

    print(tile(inX, (dataSetSize, 1)))
    
    print(diffMat)
    
    print(sqDiffMat)
    
    print(sqDistances)
    
    distances = sqDistances ** 0.5
    sortedDistances = distances.argsort()
    
    classCount = {}
    for i in range(k):
        votelLabel = labels[sortedDistances[i]]
        classCount[votelLabel] = classCount.get(votelLabel, 0) + 1
    sortedDistances = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse  = True)
    return sortedDistances[0][0]
    
    
###  Dating Site ###

def file2Matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    lineSize = len(arrayOLines)
    returnMat = zeros((lineSize, 3))
    classLabelsVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listOfLine = line.split('\t')
        returnMat[index, : ] = listOfLine[0:3]
        classLabelsVector.append(int(listOfLine[-1]))
        index += 1
    return returnMat, classLabelsVector

#----------------------------------------------------------------------
def showDatingTable(datingMat, datingLabels):
    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.scatter(datingMat[:, 1], datingMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
    plt.show()
    
#------------------归一化特征值-----------------------------
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals = minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = dataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

    

if __name__ == '__main__':
    #ds, labels = createDataBase()
    #output = classfiy([0.0, 1.2], ds, labels, 3)
    #print(output)
    
    mat, labels = file2Matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(mat)
    #showDatingTable(mat, labels)
    print(normMat, ranges, minVals)
    #print(labels)