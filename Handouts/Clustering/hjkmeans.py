
from hjplotKmeans import plotKmeans

import numpy as np
import matplotlib.pyplot as plt

def kmeans(X,k=3,max_iter=200,printOut=False):
    global plotKmeans
    mu = np.mean(X,axis=0)
    mus = np.array([mu+np.random.randn(X.shape[1])*2 for i in range(k)])
    oldmus = mus.copy()
    colors=np.array([((X-mus[i])**2).sum(axis=1) for i in range(k)]).argmin(axis=0)
    for j in range(max_iter):
        for i in range(k):
            bools = (colors == i)
            if bools.sum()>0:
                mus[i] = X[bools].sum(axis=0)/(bools*1).sum()
            else:
                mus[i] = mu+np.random.randn(X.shape[1])*2
        colors=np.array([((X-mus[i])**2).sum(axis=1) for i in range(k)]).argmin(axis=0)
        if printOut:
            plt.scatter(X[:, 0], X[:, 1],
                        c=colors, marker='o', edgecolor='black', s=50)
            if len(mus)>0:
                plt.scatter(mus[:,0],mus[:,1],c=[0,1,2],marker='P',edgecolor="white",s=100)
            plt.grid()
            plt.tight_layout()
            plt.show()
        if np.isclose(mus,oldmus).all():
            break
        #print(mus,oldmus,np.isclose(mus,oldmus))

        oldmus=mus.copy()
    return mus,j

