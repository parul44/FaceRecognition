choices=[0,2.5,3.75,5,7.5,10,50,52.5,53.75,55,57.5,60]

def findClosest(K): 
    return choices[min(range(len(choices)), key = lambda i: abs(choices[i]-K))]