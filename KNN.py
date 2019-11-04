import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from collections import OrderedDict

def knnc(X_test, y_test, X_train, y_train, k):
    dist = {}
    y_true = []
    accuracy = 0
    
    #for every new data point
    for i in range(len(X_test)):
        
        #distance
        dx = {}
        di = {}
        
        
        #euclidian distance for x_train as the dataset
        for j in range(len(X_train)):
            #sqrt x-train x- xnewpoint x2)^2+ (x_train y - new datapoint y2)^2
            d = math.sqrt(((X_train[j][0]-X_test[i][0])**2) + ((X_train[j][1] - X_test[i][1])**2))
            #adds the distance and label
            dx.update({d:y_train[j]})
        #sorts the distances
        di = OrderedDict(sorted(dx.items()))
        #takes the sorted top k distances that are labeled
        ki = {}
        ki = list(di.items())[:k]
        labelsetosa = 0
        labelversicolour = 0
        labelvirginica = 0
        
        #goes through the top k distances and keeps the count
        xz = 0
        while xz < len(ki):
            label = ki[xz][1]
            if label == 0:
                labelsetosa = labelsetosa+1
            if label == 1:
                labelversicolour = labelversicolour+1
            if label == 2:
                labelvirginica = labelvirginica+1
            xz = xz +1
            
            

        #decides which label has the majority and stores the result into y_true
        if (labelsetosa > labelversicolour) & (labelsetosa > labelvirginica):
            y_true.append(0)
        if (labelversicolour > labelsetosa) & (labelversicolour > labelvirginica):
            y_true.append(1)
        if (labelvirginica > labelsetosa) & (labelvirginica > labelversicolour):
            y_true.append(2)
    
    #compares guessed data with real data
    for i in y_true:
        if y_true[i] == y_test[i]:
            accuracy = accuracy+1
            
    return accuracy/50 * 100
            
k = 15
accuracy = knnc(X_test, y_test, X_train, y_train, k)
print('accuracy')
print(accuracy)
