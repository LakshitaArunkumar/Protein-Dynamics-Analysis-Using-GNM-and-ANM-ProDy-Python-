import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    pdb_id = sys.argv[1].lower()

    # Suppress ProDy log messages
    prody.LOGGER._setverbosity('none')

    # Parse structure (C-alpha atoms only)
    structure = parsePDB(pdb_id, subset='ca')

    # --- GNM ---
    gnm, atoms_gnm = calcGNM(structure)
    gnm_fluct = calcSqFlucts(gnm[:])

    # --- ANM ---
    anm, atoms_anm = calcANM(structure)
    anm_fluct = calcSqFlucts(anm[:])

    # --- Absolute difference before normalization ---
    abs_diff = np.abs(gnm_fluct - anm_fluct)
    max_diff = np.max(abs_diff)
    print(f"Max Abs Difference: {max_diff:.3f}")

    # --- Normalize each to have max = 1 ---
    gnm_norm = gnm_fluct / np.max(gnm_fluct)
    anm_norm = anm_fluct / np.max(anm_fluct)

    # --- Absolute difference after normalization ---
    abs_norm_diff = np.abs(gnm_norm - anm_norm)
    max_norm_diff = np.max(abs_norm_diff)
    print(f"Max Abs Norm Difference: {max_norm_diff:.3f}")

if __name__ == "__main__":
    main()
