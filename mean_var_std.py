import numpy as np

def calculate(listt):
  
  # Ensure list is 9 long
  if len(listt) != 9:
      raise ValueError('List must contain nine numbers.')
  else:
    calculations = {}
    # Create matrix
    x = np.array(listt).reshape(3,3)
    
    # Find mean
    Mean = x.mean()
    calculations['mean'] = [(x.mean(axis=0)).tolist(),  x.mean(axis=1).tolist(), Mean]
    
    # Find Variance
    Var = x.var()
    calculations['variance'] = [(x.var(axis=0)).tolist(),  x.var(axis=1).tolist(), Var]

    # Find Standard Deviation
    STD = x.std()
    calculations['standard deviation'] = [(x.std(axis=0)).tolist(),  x.std(axis=1).tolist(), STD]
    
    # Find max
    Max = x.max()
    print(Max)
    calculations['max'] = [(x.max(axis=0)).tolist(),  x.max(axis=1).tolist(), Max]

    # Find min
    Min = x.min()
    calculations['min'] = [(x.min(axis=0)).tolist(),  x.min(axis=1).tolist(), Min]

    # Find sum
    Sum = x.sum()
    calculations['sum'] = [(x.sum(axis=0)).tolist(),  x.sum(axis=1).tolist(), Sum]


    return calculations