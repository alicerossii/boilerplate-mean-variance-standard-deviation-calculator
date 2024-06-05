import numpy as np

def calculate(list):
    if len(list)!= 9: 
        raise ValueError('List must contain nine numbers.')
    array= np.array(list).reshape((3,3))

    mean0, mean1, mean= np.mean(array, axis=0), np.mean(array, axis=1), np.mean(array)
    list_mean=   [mean0.tolist()] + [mean1.tolist()] + [mean]

    variance0, variance1, variance= np.var(array, axis=0), np.var(array, axis=1), np.var(array)
    list_variance= [variance0.tolist()]+[variance1.tolist()]+[variance.tolist()]

    stdev0, stdev1, stdev= np.std(array, axis=0), np.std(array, axis=1), np.std(array)
    list_std=[stdev0.tolist()]+[stdev1.tolist()]+[stdev]

    max0, max1, maximumm= np.max(array, axis=0), np.max(array, axis=1), np.max(array)
    list_max=[max0.tolist()]+[max1.tolist()]+[maximumm]

    min0, min1, minimum= np.min(array, axis=0), np.min(array, axis=1), np.min(array)
    list_min=[min0.tolist()]+[min1.tolist()]+[minimum]

    sum0, sum1, sumtot= np.sum(array, axis=0), np.sum(array, axis=1), np.sum(array)
    list_sum=[sum0.tolist()]+[sum1.tolist()]+[sumtot]
    
    calculations= {'mean': list_mean , 
                   'variance': list_variance ,
                   'standard deviation': list_std ,
                   'max': list_max,
                   'min': list_min ,
                   'sum': list_sum }

    return calculations