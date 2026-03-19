## Protein Dynamics Analysis Using GNM and ANM (ProDy, Python)

This project analyzes protein structural dynamics using elastic network models, specifically the Gaussian Network Model (GNM) and Anisotropic Network Model (ANM), implemented with ProDy. The pipeline computes residue-level fluctuations, compares modeling approaches, and identifies structurally significant regions.

---

## Project Overview

Protein dynamics play a critical role in biological function. This project models intrinsic fluctuations of protein structures using:

- GNM (Gaussian Network Model)  
- ANM (Anisotropic Network Model)  

Both approaches represent proteins as elastic networks of residues connected by springs, enabling prediction of collective motions from structure alone.

---

## Objectives

- Compute residue-level fluctuations using GNM and ANM  
- Compare fluctuation magnitudes between models  
- Normalize and quantify differences  
- Identify residues with the largest dynamic discrepancies  

---

## Scripts

- `gnm-fluctuations.py`  
  - Computes GNM-based squared fluctuations for Cα atoms  

- `anm-fluctuations.py`  
  - Computes ANM-based squared fluctuations  

- `fluctuation-diff.py`  
  - Calculates absolute and normalized differences between GNM and ANM  

- `fluctuation-diff-index.py`  
  - Identifies residues with the largest normalized fluctuation differences  

---

## Methodology

### Elastic Network Models

- GNM:
  - Uses connectivity only  
  - Produces isotropic (non-directional) fluctuations  

- ANM:
  - Includes directional information  
  - Captures anisotropic motions  

---

### Fluctuation Analysis

- Based on normal mode analysis  
- Computed for Cα atoms  
- Uses full set of modes  

---

### Normalization

- Each model scaled so maximum fluctuation = 1  
- Enables direct comparison across models  

---

### Residue Mapping

- Differences mapped to:
  - Residue index  
  - Residue name and number  

---

## Technologies Used

- Python  
- ProDy  
- NumPy  

---

## Key Features

- Automated PDB retrieval  
- Comparative modeling (GNM vs ANM)  
- Residue-level fluctuation analysis  
- Normalization for fair comparison  
- Identification of dynamically important regions  

---

## Key Skills Demonstrated

- Structural bioinformatics  
- Protein dynamics modeling  
- Normal mode analysis  
- Scientific computing in Python  
- Data normalization and comparison  
- Interpretation of structure–function relationships  

---

## Notes

- Fluctuations are computed for Cα atoms only  
- Differences between GNM and ANM arise from scaling and directional modeling  
- Output values are formatted to three decimal precision  

---

## Author

Lakshita Arunkumar
