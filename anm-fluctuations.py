import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    pdb_id = sys.argv[1].lower()

    # Suppress ProDy informational output
    prody.LOGGER._setverbosity('none')

    # Parse PDB (C-alpha atoms only)
    structure = parsePDB(pdb_id, subset='ca')

    # Calculate ANM with default arguments
    anm, atoms = calcANM(structure)

    # Compute squared fluctuations using all modes
    fluctuations = calcSqFlucts(anm[:])

    # Print the largest fluctuation
    print(f"Max ANM SqFluct: {np.max(fluctuations):.3f}")

if __name__ == "__main__":
    main()
