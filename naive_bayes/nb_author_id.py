#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################

from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()

classifier.fit(features_train,labels_train)

t0=time()

labels_pred = classifier.predict(features_test)

t1=time()
#print("time taken",t1-t0)
print "training time:", round(time()-t0, 3), "seconds"


from sklearn.metrics import accuracy_score

print(accuracy_score(labels_test,labels_pred))

#########################################################


