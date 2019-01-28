import time
from os import listdir
from os.path import join, isfile, dirname, realpath

import numpy as np
import pandas as pd

outputDir = dirname(realpath(__file__)) + '/output/'

def dumpFeatures(layeredOutput, data, dataLabels, isTrain):
    chunkSize = 5000
    strName = "Train" if isTrain else "Test"
    fileName = outputDir + 'MNIST_' + strName + '_FV_' + str(0) + ".csv"
    titleRow = ["Index", "Label", "Data", "Feature Vector"]
    startTime = time.time()
    totalTime = startTime
    featureDataList = list()
    for idx in range(len(data)):
        x = [data[idx]]
        featureVector = layeredOutput([x])[0]
        dataList = [idx, dataLabels[idx].tolist(), (data[idx] * 255.0).tolist(), featureVector.tolist()[0]]
        # print(dataList)
        featureDataList.append(dataList)
        if idx != 0 and (idx + 1) % chunkSize == 0:
            print("Extracted %d %s data features in [%.3f seconds]" % (idx, strName, time.time() - startTime))
            startTime = time.time()
            fileName = outputDir + 'MNIST_' + strName + '_FV_' + str(idx + 1) + ".csv"
            df = pd.DataFrame(featureDataList, columns=titleRow)
            df.to_csv(fileName)
            featureDataList.clear()
    fileName = outputDir + 'MNIST_' + strName + '_FV_' + str(idx + 1) + ".csv"
    df = pd.DataFrame(featureDataList, columns=titleRow)
    df.to_csv(fileName)
    print("Extracted total of %d %s data features in [%.3f seconds]" % (len(data), strName, time.time() - totalTime))


def getFeatureVectors(dir):
    featureFiles = [join(dir, file) for file in listdir(dir) if isfile(join(dir, file))]
    featureFiles.sort()
    # fileCount = 0
    titleRow = ["Index", "Label", "Data", "Feature Vector"]
    labelList = list()
    characterDataList = list()
    featureVectorList = list()
    for file in featureFiles:
        print("Parsing %s" % (file))
        data = pd.read_csv(file)
        dataFrame = pd.DataFrame(data, columns=titleRow)
        for i in range(len(dataFrame)):
            label = dataFrame['Label'][i].replace('[', '').replace(']', '').split(',')
            characterData = dataFrame['Data'][i].replace('[', '').replace(']', '').split(',')
            featureVector = dataFrame['Feature Vector'][i].replace('[', '').replace(']', '').split(',')

            labelList.append(label)
            characterDataList.append(characterData)
            featureVectorList.append(featureVector)

    for i in range(len(characterDataList)):
        characterDataList[i] = [int(float(value)) for value in characterDataList[i]]
        characterDataList[i] = np.array(characterDataList[i]).reshape(28, 28)
        featureVectorList[i] = [float(value) for value in featureVectorList[i]]
        labelList[i] = [float(value) for value in labelList[i]]
    return labelList, characterDataList, featureVectorList


# labelList, characterDataList, featureVectorList = getFeatureVectors('output/features/')
# k = 10
# kmeans = KMeans(n_clusters=10)
# kmeans = kmeans.fit(featureVectorList)
# labels = kmeans.predict(featureVectorList)