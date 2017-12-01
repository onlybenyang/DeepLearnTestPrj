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
    featureNum = len(dataSet)
    
    

if __name__  == '__main__':
    dataSet, labels = createDataSet()
    newdataSet = splitDataSet(dataSet, 0, 0)
    print(newdataSet)
    infoEntropy = getInfoEntropy(dataSet)
    #print(infoEntropy)
