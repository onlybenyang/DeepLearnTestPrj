#----
#决策树
#----
from math import log
import operator


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


#---递归构建决策树---#

#----------------------------------------------------------------------
def marjorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vate not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems, key=operator.itemgetter[1], reverse=True)
    return sortedClassCount
    
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    #print(classList)
    #print(classList.count(classList[0]))
    #如果类别完全相同就停止划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return marjorityCnt(classList)
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = labels[bestFeature]
    myTree = {bestFeatureLabel: {}}
    del(labels[bestFeature])
    featValues = [example[bestFeature] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatureLabel][value] = createTree(splitDataSet(dataSet, bestFeature, value), subLabels)
    return myTree
    


if __name__  == '__main__':
    #--- 获得最佳划分数据集的特征
    dataSet, labels = createDataSet()
    bestFeature = chooseBestFeatureToSplit(dataSet)
    #print(bestFeature)
    
    #---递归创建决策树
    tree = createTree(dataSet, labels)
    print(tree)
