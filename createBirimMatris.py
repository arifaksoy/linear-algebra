import numpy as np

def knockerDeltaFunction(i,j):
    if (i==j):
        return 1
    else:
        return 0


a=input("Satir-sutun degerini giriniz:")
a=int(a)
l=np.zeros(shape=(a,a))


for i in range(a):
    for j in range(a):
        l[i][j]=knockerDeltaFunction(i,j)
       

print("birim matris:\n",l)