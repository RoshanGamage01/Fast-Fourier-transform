import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    
    even_indexed = fft(x[0::2])
    odd_indexed = fft(x[1::2])
    
    combined = np.zeros(N, dtype=complex)

    for k in range(N // 2):
        exp = np.exp(-2j * np.pi * k / N) * odd_indexed[k]
        combined[k] = even_indexed[k] + exp
        combined[k + N // 2] = even_indexed[k] - exp
    
    return combined

def ifft(x):
    N = len(x)

    if( N <= 1 ):
        return x
    
    even_indexed = ifft(x[0::2])
    odd_indexed = ifft(x[1::2])

    combined = np.zeros(N, dtype=complex)

    for k in range(N // 2):
        exp = np.exp(2j * np.pi * k / N) * odd_indexed[k]
        combined[k] = even_indexed[k] + exp
        combined[k + N // 2] = even_indexed[k] - exp

    return combined