#12S17031	Debby Debora Hutajulu
#12S17058	Juanda Antonius Pakpahan
#12S17062	Venny Handayani Sormin


import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

labels=[]
features=[]
file=open('Training Dataset.arff').read()

list=file.split('\n')

data=np.array(list)
data_new=[i.split(',') for i in data]
data_new=data_new[0:-1]
for i in data_new:
	labels.append(i[30])
data_new=np.array(data_new)

features=data_new[:,:-1]

features=features[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,22,23,24,25,27,29]]

features=np.array(features).astype(np.float)

features_train=features
labels_train=labels


print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier(min_samples_split=7, verbose=True)
clf4.fit(features_train, labels_train)
importances = clf4.feature_importances_

indices = np.argsort(importances)[::-1]

print("Perangkingan Fitur:")
for f in range(features_train.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))



joblib.dump(clf4, 'random_forest.pkl',compress=9)
