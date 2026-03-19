import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    # Read PDB ID argument
    pdb_id = sys.argv[1].lower()

    # Suppress ProDy messages logs
    prody.LOGGER._setverbosity('none')

    # Parse PDB & keep only CA atoms
    structure = parsePDB(pdb_id, subset='ca')

    # Calculate Gaussian Network Model (GNM)    
    gnm, atoms = calcGNM(structure)

    # Compute squared fluctuations 
    fluctuations = calcSqFlucts(gnm[:]) #variance is predicted for all residues

    # Print maximum squared fluctuation
    print(f"Max GNM SqFluct: {np.max(fluctuations):.3f}")

if __name__ == "__main__":
    main()
