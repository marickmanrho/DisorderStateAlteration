# Compare disorder states
This code allows you to see how the band_edge or band_middle states change over time.

## Use
run `python compare_disorder_states.py`

## How it works
The Hamiltonian is a simple Frenkel Hamiltonian. We only include nearest neighbour interactions and employ open boundary conditions.

First we calculate the delocalized basis (Vo) when there is no disorder. Then we itteratively increase disorder. For each itteration we diagonalize the Hamiltonian and project the lower band-edge state onto Vo. The coëficients are then plotted in the animated bar chart.

## Contact
For questions please contact us at m.manrho@rug.nl
