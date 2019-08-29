# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def xianxingpanbiefenxi():
    #线性判别分析
    a=[]
    with open(r'D:\python_experiment\data\blood\blood_data.txt','r') as f:
        for line in f.readlines():
            b = []
            for x in line.split(','):
                b.append(int(x))
            a.append(b)
    a0 = []
    a1 = []
    u0 = []
    u1 = []
    for l in a:
        cg = l.pop()
        if cg == 0:
            a0.append(l)
        else:
            a1.append(l)
    
    a0 = np.mat(a0)
    a1 = np.mat(a1)
    #a0 = a0[:,[0,3]]
    #a1 = a1[:,[2,1]]
    u0=np.mean(a0,axis=0)
    u1=np.mean(a1,axis=0)
    wsm0=np.matmul((a0-u0).T,(a0-u0))
    wsm1=np.matmul((a1-u1).T,(a1-u1))
    Sw=wsm0+wsm1#类内散度矩阵
    
    w=np.matmul(Sw.I,(u0-u1).transpose(1,0))#确定w
    x0=np.matmul(a0,w)#投影
    x1=np.matmul(a1,w)
    y0=[0 for i in range(len(x0))]
    y1=[1 for i in range(len(x1))]
    
    #输出数据分类结果
    print(w)
    plt.plot(a0[:,3], a0[:,2], 'y*')
    plt.plot(a1[:,3], a1[:,2], 'g*')
    plt.show()
    #投影方向w绘图并输出
    plt.plot(x0, y0, 'y*')
    plt.plot(x1, y1, 'g*')
    plt.show()
def main():
    xianxingpanbiefenxi()
main()