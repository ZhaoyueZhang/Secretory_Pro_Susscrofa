# coding=utf-8

import sys, os
import pandas as pd

##get model features
def getfeaturelist(featurefile):
    f = open(featurefile,'r')

    featurelist = []
    for eachfeature in f:
        featurelist.append(eachfeature.strip())

    f.close()
    return featurelist
    
def Sorted_fre(featurelist):
    reader =pd.read_table('test_fea.csv',sep=',')
    data = pd.DataFrame(reader)
    new_data = data[featurelist]
    #print(featurelist)
    #print(new_data.columns.values)
    print('*****Feature Generating*****')
    
    #print('Sorted_fre.shape:%s'%new_data.shape)
    new_data.to_csv('s_test.csv')


if __name__=='__main__':
    featurelist = getfeaturelist('fealist.txt')
    #os.system('python3 PseCKSAAP.py --file test.fasta --out test_fea.csv')
    Sorted_fre(featurelist)


