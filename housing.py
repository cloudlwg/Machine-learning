# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


a = []
def openFileAndSplit():
    #打开并且分割字符
    
    with open(r"D:\python_experiment\data\boson\housing_data.txt",'r') as f:
        
        for line in f.readlines():
            b = []
            for x in line.split():
                b.append(float(x))
            a.append(b)
    



def duoyuanxianxinghuigui():
    #多元线性回归模型
    b = []
    #分离最后一列
    for l in a:
        b.append([l.pop()])
        l.append(1)
    a1 = np.mat(a[0:449])
    a2 = np.mat(a[450:505])
    b1 = np.mat(b[0:449])
    b2 = np.mat(b[450:505])
    k = np.matmul(a1.transpose(1,0),a1).I
    k = np.matmul(np.matmul(k,a1.transpose(1,0)),b1)
    ans = np.matmul(a2,k).transpose(1,0)
    #均方差计算准确率
    accuRate = np.array(ans - b2.transpose(1,0))[0]
    print(ans)
    print("准确率：")
    print(sum(accuRate*accuRate)/len(accuRate))
    
    
def main():
    openFileAndSplit()
    duoyuanxianxinghuigui()
    
main()
