from .subdirs import templateDir

choices=templateDir()

def findClosest(K): 
    return choices[min(range(len(choices)), key = lambda i: abs(choices[i]-K))]