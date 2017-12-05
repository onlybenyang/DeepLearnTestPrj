#----
#决策树
#----
from math import log


#---信息熵---
#创建信息熵数据集
def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 0, 'no'],
        [0, 0, 'no']]
    labels = ['no serfacing', 'flippers']
    return dataSet, labels

#获得熵
def getInfoEntropy(dataSet):
    dataCount = len(dataSet)
    labelsOfSet = {}
    entropy = 0.0
    for vector in dataSet:
        label = vector[-1]
        if(label not in labelsOfSet):
            labelsOfSet[label] = 0
        labelsOfSet[label] += 1
    
    for key in labelsOfSet:
        prob = float(labelsOfSet[key]) / dataCount
        entropy -= prob * log(prob, 2) #2为底求对数
    return entropy

# 根据特征抽离数据集
def splitDataSet(dataSet, axes, value):
    newDataSet = []
    for vector in dataSet:
        if vector[axes] == value :
            reduceVec = vector[:axes]
            reduceVec.extend(vector[axes+1:])
            newDataSet.append(reduceVec)
    return newDataSet
    
def chooseBestFeatureToSplit(dataSet):
    featureNum = len(dataSet[0]) - 1
    baseEntroy = getInfoEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(featureNum):
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntroy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntroy += prob * getInfoEntropy(subDataSet)
        infoGain = baseEntroy - newEntroy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


if __name__  == '__main__':
    dataSet, labels = createDataSet()
    #newdataSet = splitDataSet(dataSet, 0, 0)
    bestFeature = chooseBestFeatureToSplit(dataSet)
    print(bestFeature)
    #infoEntropy = getInfoEntropy(dataSet)
    #print(infoEntropy)
