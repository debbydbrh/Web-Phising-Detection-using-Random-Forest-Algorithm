#12S17031	Debby Debora Hutajulu
#12S17058	Juanda Antonius Pakpahan
#12S17062	Venny Handayani Sormin

import joblib 
import features
import sys

def main():
    url=sys.argv[1]
    features_test=features.main(url)

    clf = joblib.load('random_forest.pkl')

    pred=clf.predict(features_test)

    if int(pred[0])==1:
        print ("Website ini aman")
    elif int(pred[0])==-1:
        print ("Website ini tidak aman!")

if __name__=="__main__":
    main()
