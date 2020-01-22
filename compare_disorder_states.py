def plot(itt):
    ax.clear()
    ax.bar(Xax,alpha[:,itt],0.3)
    ax.text(20,0.1,str(itt))

def diagonalize_hamiltonian(H):
    import numpy as np
    [E,V] = np.linalg.eig(H)

    # Sort eigenvectors based on energy
    t = E.argsort()
    E = E[t]
    V = V[:,t]

    return E,V

from hamiltonian import hamiltonian
import matplotlib.pyplot as plt
import numpy as np

N = 20
J = 20
sigma_vec = range(100)
Nitt = 300

# First generate hamiltonian without disorder (reference)
H = hamiltonian(N,J,0)

# Diagonalize
Eo,Vo = diagonalize_hamiltonian(H)

alpha = np.zeros((N,len(sigma_vec)))
# For each of the disorder hamiltonians compare band_edge state with reference
for ns in range(len(sigma_vec)):
    for itt in range(Nitt):
        H = hamiltonian(N,J,sigma_vec[ns])
        E,V = diagonalize_hamiltonian(H)

        # calculate overlap between band edge and unperturbed states
        alpha[:,ns] = alpha[:,ns] + np.square(np.dot(np.transpose(Vo),V[:,0]))/Nitt

import matplotlib.animation as animation
Xax = range(N)
fig, ax = plt.subplots(figsize=(10,10))
animator = animation.FuncAnimation(fig,plot,frames=range(len(sigma_vec)))
plt.show()
