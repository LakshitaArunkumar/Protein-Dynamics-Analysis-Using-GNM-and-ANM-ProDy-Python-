import sys
import numpy as np
import prody
from prody import *

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    pdb_id = sys.argv[1].lower()
    prody.LOGGER._setverbosity('none')

    # Parse PDB file (C-alpha atoms)
    structure = parsePDB(pdb_id, subset='ca')

    # --- GNM ---
    gnm, atoms_gnm = calcGNM(structure)
    gnm_fluct = calcSqFlucts(gnm[:])

    # --- ANM ---
    anm, atoms_anm = calcANM(structure)
    anm_fluct = calcSqFlucts(anm[:])

    # --- Normalize each (max = 1) ---
    gnm_norm = gnm_fluct / np.max(gnm_fluct)
    anm_norm = anm_fluct / np.max(anm_fluct)

    # --- Compute absolute difference ---
    abs_diff = np.abs(gnm_norm - anm_norm)

    # --- Get residue info ---
    residues = structure.getResnames()
    resnums = structure.getResnums()

    # --- Sort by largest differences ---
    sorted_indices = np.argsort(abs_diff)[::-1]  # descending order

    # --- Print top 10 ---
    for i in range(10):
        idx = sorted_indices[i]
        print(f"{abs_diff[idx]:.3f} {idx} {residues[idx]}{resnums[idx]}")

if __name__ == "__main__":
    main()
