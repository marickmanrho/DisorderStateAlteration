def hamiltonian(N,J,sigma):
    import numpy as np

    diag = np.random.randn(N)*sigma
    off_diag = np.ones((N-1))*J
    H = np.diag(off_diag,1) + np.diag(off_diag,-1) + np.diag(diag,0)

    return H

if __name__ == '__main__':
    hamiltonian(4,10,10)
