def plot_alpha(itt):
    ax1.clear()
    Xax = range(N)
    ax1.bar(Xax,alpha[:,itt],0.3)
    ax1.set_ylim(0,1)
    ax1.set_xlabel('Unperturbed state (Energy sorted)')
    ax1.set_ylabel('Alpha')
    ax1.title.set_text('Projection edge state onto unperturbed basis')

    ax2.clear()
    Emin = np.min(dos)
    Emax = np.max(dos)

    EEmin = np.min(dos[:,itt])
    EEmax = np.max(dos[:,itt])

    Npoints = 300
    std = 20*(EEmax-EEmin-2*J)/Npoints
    Xax = np.linspace(Emin-3*std,Emax+3*std,Npoints)

    sdos = np.shape(dos)
    Yax = np.zeros((Npoints,))
    for E in range(sdos[0]):
        for x in range(Npoints):
            Yax[x] = Yax[x]+np.exp(-(dos[E,itt]-Xax[x])**2/std**2)

    Yax = Yax/np.max(Yax)
    ax2.plot(Xax,Yax)
    ax2.title.set_text('Density of States')
    ax2.text(Emin,0.9,'sigma/J = '+str(sigma_vec[itt]/J))
    ax2.set_ylabel('DOS (Max = 1)')
    ax2.set_xlabel('Energy')
    plt.tight_layout()

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

N = 30
J = 40
sigma_vec = range(100)
Nitt = 1000

# First generate hamiltonian without disorder (reference)
H = hamiltonian(N,J,0)

# Diagonalize
Eo,Vo = diagonalize_hamiltonian(H)

alpha = np.zeros((N,len(sigma_vec)))
dos = np.zeros((N,len(sigma_vec)))
# For each of the disorder hamiltonians compare band_edge state with reference
for ns in range(len(sigma_vec)):
    for itt in range(Nitt):
        H = hamiltonian(N,J,sigma_vec[ns])
        E,V = diagonalize_hamiltonian(H)

        # calculate overlap between band edge and unperturbed states
        alpha[:,ns] = alpha[:,ns] + np.square(np.dot(np.transpose(Vo),V[:,0]))/Nitt

        # Density of states
        dos[:,ns] = dos[:,ns] + E/Nitt

import matplotlib.animation as animation


#fig, ax = plt.subplots(figsize=(10,10))
#animator = animation.FuncAnimation(fig,plot_alpha,frames=range(len(sigma_vec)))
#plt.show()


fig, (ax1,ax2) = plt.subplots(2,1,figsize=(8,8))
animator = animation.FuncAnimation(fig,plot_alpha,frames=range(len(sigma_vec)))
plt.show()
