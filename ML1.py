import math
import operator
import csv
'''with open("iris.data","rb") as csvfile:
    
    lines = csv.reader(csvfile)
    for row in lines:
        print ','.join(row)
   ''' 
import random
def loadDataset(filename, split , trainning_data = [], test_data = []):
    with open(filename, "rb") as csvfile:
                        lines = csv.reader(csvfile)
                        dataset = list(lines)
                        for x in range(len(dataset) - 1):
                            for y in range(4):
                                dataset[x][y] = float(dataset[x][y])
                            if random.random() < split:
                                trainning_data.append(dataset[x])
                            else:
                                test_data.append(dataset[x])
trainningset = []
testSet = []
'''
loadDataset("iris.data",0.66,trainningset, testSet)
print (len(trainningset) )
print (len(testSet))'''

distance = 0
def euclidean_distance(ins1, ins2 , length):
    distance = 0
    for x in range(length):
        distance += pow(ins1[x] - ins2[x], 2)
    return math.sqrt(distance)

print (euclidean_distance([1,2,3],[4,5,6],3))
def getNeighbours(trainningset, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainningset)):
        dist = euclidean_distance(testInstance, trainningset[x], length)
        distances.append((trainningset[x],dist))
    distances.sort(key = operator.itemgetter(1))
    neighbours= []
    for x in range(k):
        neighbours.append(distances[x][0])
    return neighbours
#to test
'''
trainset = [[2,2,2,'a'], [4,4,4,'b']]
testInstance = [5,5,5]
neighbours = getNeighbours(trainset, testInstance, 1)
print(neighbours)
'''
def getResponseVotes(neighbours): 
    classvotes = {}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classvotes:
            classvotes[response] += 1
        else:
            classvotes[response] = 1
    sortedVotes = sorted(classvotes.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]

loadDataset("iris.data",0.66,trainningset, testSet);

N = getNeighbours(trainningset, testSet[10], 3)
'''print getResponseVotes(N)'''
def getAccuracy(testSet, predictions) :
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x] :
            correct += 1
    return (correct / float(len(testSet))) * 100.0

def main():
   trainingSet = []
   Split = 0.67
   loadDataset("iris.data",Split,trainningset, testSet)
   print trainningset
   print testSet
   predictions = []
   k = 3
   for x in range(len(testSet)):
       neighbours = getNeighbours(trainningset, testSet[x],k)
       result = getResponseVotes(neighbours)
       predictions.append(result)
       print('> predicted = ' + repr(result) +', actual = '+repr(testSet[x][-1]))
   accuracy = getAccuracy(testSet, predictions)
   print("accuracy:" + repr(accuracy) + '%')
main()
    



        
