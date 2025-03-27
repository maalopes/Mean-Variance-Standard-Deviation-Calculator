import numpy as np
#maalopes solution
def calculate(list):
    bas = list
    print(len(bas))
    if len(bas) != 9:
        raise ValueError("List must contain nine numbers.")
    matri = np.array(bas).reshape(3, 3)

    soma = np.sum(matri, axis=0).tolist()
    sima = np.sum(matri, axis=1).tolist()
    suma = np.sum(matri).tolist()

    ma = np.max(matri, axis=0).tolist()
    maxx = np.max(matri, axis=1).tolist()
    maxi = np.max(matri, axis=None).tolist()

    minim = np.min(matri, axis=0).tolist()
    minimu = np.min(matri, axis=1).tolist()
    minimo = np.min(matri, axis=None).tolist()

    media = np.mean(matri, axis=0).tolist()
    median = np.mean(matri, axis=1).tolist()
    mediaa = np.mean(matri, axis=None).tolist()

    varia = np.var(matri).tolist()
    varian = np.var(matri, axis=0).tolist()
    varianc = np.var(matri, axis=1).tolist()

    stand = np.std(matri, axis=0).tolist()
    standD = np.std(matri, axis=1).tolist()
    standDev = np.std(matri, ddof=0).tolist()

    calculations = {'mean': [media, median, mediaa],
                    'variance': [varian, varianc, varia],
                    'standard deviation': [stand, standD, standDev],
                    'max': [ma, maxx, maxi],
                    'min': [minim, minimu, minimo],
                    'sum': [soma, sima, suma]}


    print(calculations)
    return calculations