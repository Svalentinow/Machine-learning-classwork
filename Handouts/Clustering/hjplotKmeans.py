import matplotlib.pyplot as plt

def plotKmeans(X,mus=[],colors="white"):
    plt.scatter(X[:, 0], X[:, 1],
                c=colors, marker='o', edgecolor='black', s=50)
    if len(mus)>0:
        plt.scatter(mus[:,0],mus[:,1],c=[0,1,2],marker='+',edgecolor="white")
    plt.grid()
    plt.tight_layout()
    plt.show()

