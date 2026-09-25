import matplotlib.pyplot as plt
import numpy as np

def SIGNALgenerate(N=100, signal='delta', params=None):
    n=np.arange(N)

    if signal == 'delta':
      k = params if params is not None else 0
      x = np.zeros(N)
      if 0 <= k < N:
        x[k] = 1

    if signal == 'step':
        k = params if params is not None else 0
        x = np.zeros(N)
        if 0 <= k < N:
          x[k:] = 1

    if signal == 'exp':
      a = params.get('a', 0.9) if isinstance(params, dict) else 0.9
      k = params.get('k', 0) if isinstance(params, dict) else 0
      x = np.zeros(N)
      x[k:] = a**(n[k:] - k)


    if signal == 'osc':
      P   = params.get('P', 10) if isinstance(params, dict) else 10
      phi = params.get('phi', 0) if isinstance(params, dict) else 0
      wo  = 2*np.pi/P
      x = np.sin(wo*n + phi)

    if signal == 'random':

        if params == 'uniform':
            x = np.random.uniform(-1, 1, N)
        else:
            x = np.random.normal(0, 1, N)

    return np.array(x)

def SIGNALdelay(x, n):
    '''
    Slows a signal down by k samples
    '''
    result = np.zeros(len(x))
    result[n:] = x[:len(x) - n]

    return result

def SIGNALplot(x):
    fig, ax = plt.subplots()
    ax.stem(x, 'r')
    # figureFormat(ax, fig, tight=True)
    plt.show()