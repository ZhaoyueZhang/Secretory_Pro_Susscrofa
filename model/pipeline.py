# def getbestfealist(n):
    # f = open('f%s.csv'%n)
    # g = open('fealist.txt','w')
    # templine = f.readline().strip().split(',')
    # for each in templine[1:]:
        # g.write('%s\n'%each)
    # f.close()
    # g.close()
    # return 0
    
# def gettestprob(fasta_file):
    
    # f = open('%s'%fasta_file)
    # label = []
    # for eachline in f:
        # if eachline[0]=='>':
            # label.append(eachline[1])
        # else:
            # pass
    # f.close()
    
    # count = 0
    # f = open('sres.txt')
    # g = open('test_prob.txt','w')
    # for eachline in f:
        # if eachline[0:6]=='labels':
            # continue
        # else:
            # temp = eachline.strip().split(' ')
            # g.write('%s,%s,%s,%s\n'%(label[count],temp[1],temp[2],temp[0]))
            # count += 1
    # f.close()
    # g.close()
    
    # return 0
    
def gettestres(fasta_file):

    
    commands = []
    commands.append(r"python3 PseCKSAAP.py --file %s --out test_fea.csv"%fasta_file)
    commands.append(r"python3 gettest_fea.py")
    commands.append(r"python3 CSVtoSVM.py s_test.csv test_s.svm")
    commands.append(r"./libsvm/svm-scale -r f81.rule test_s.svm > test_s.scale")
    commands.append(r"./libsvm/svm-predict -b 1 test_s.scale f81.model res.txt > temp.out")
    
    for eachCmd in commands:
        os.system(eachCmd)
    
    #gettestprob(fasta_file)
    print('*****%s Prediction Finishd!*****'%fasta_file)
    print('*****Open res.txt to get the Prediction Result!*****')
    return 0


import os
import re
import sys
import pandas as pd
from sklearn import metrics
from sklearn.metrics import roc_curve, auc
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


if __name__ == '__main__':

    fasta_file = sys.argv[1]
    gettestres(fasta_file)
