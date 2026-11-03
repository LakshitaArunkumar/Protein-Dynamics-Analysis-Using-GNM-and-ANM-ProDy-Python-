
# Protein Dynamics Analysis Using GNM and ANM (ProDy, Python)

**Coursework Project | University of Pittsburgh**

## Project Overview

This project was completed as part of my coursework at the University of Pittsburgh. It involved analyzing protein structural dynamics using two elastic network models: the **Gaussian Network Model (GNM)** and the **Anisotropic Network Model (ANM)**.

Using Python and ProDy, the project examined predicted residue-level fluctuations, compared the results obtained from both models, and identified residues showing the largest differences in their predicted flexibility.

The analysis demonstrates how computational models can be used to investigate collective protein motions and explore relationships between protein structure and dynamics.

## Objectives

- Analyze protein structures using elastic network models.
- Calculate residue-level fluctuations using GNM and ANM.
- Compare the magnitude of predicted fluctuations between models.
- Normalize fluctuation values for comparison.
- Identify residues with the largest differences between GNM and ANM predictions.
- Retrieve residue identities and positions from protein structures.

## Tools and Technologies

| Tool | Purpose |
|------|---------|
| Python | Scientific computing and scripting |
| ProDy | Protein structure analysis and normal mode calculations |
| NumPy | Numerical calculations, normalization, and sorting |
| PDB | Protein structure data |
| sys | Command-line argument handling |

## Analysis Workflow

```text id="7f9gpm"
       Protein Structure (PDB)
                |
                v
       Extract Cα Atom Coordinates
                |
        +-------+-------+
        |               |
        v               v
   GNM Analysis     ANM Analysis
        |               |
        v               v
   Residue-Level Squared Fluctuations
                |
                v
     Compare Fluctuation Values
                |
                v
      Normalize Both Models
                |
                v
    Calculate Absolute Differences
                |
                v
   Rank Residues by Difference
                |
                v
     Report Top 10 Residues
```

## Methods

### 1. Protein Structure Processing

- Loaded protein structures using ProDy's `parsePDB()`.
- Selected alpha-carbon (Cα) atoms to represent protein residues.
- Used the resulting coordinates for elastic network modeling.

### 2. Gaussian Network Model (GNM)

- Constructed a Gaussian Network Model using `calcGNM()`.
- Calculated squared fluctuations using `calcSqFlucts()`.
- Reported the maximum predicted squared fluctuation.

GNM models protein dynamics using residue connectivity and predicts the magnitude of fluctuations without directional information.

### 3. Anisotropic Network Model (ANM)

- Constructed an Anisotropic Network Model using `calcANM()`.
- Calculated residue-level squared fluctuations.
- Reported the maximum fluctuation predicted by the model.

ANM incorporates directional information, allowing the analysis of collective protein motions in three dimensions.

### 4. Fluctuation Comparison and Normalization

- Calculated absolute differences between GNM and ANM fluctuation values.
- Normalized each model's fluctuation values by dividing by its maximum.
- Compared the normalized predictions to examine differences in relative residue flexibility.

Normalization was performed using:

```python id="0pm01a"
gnm_norm = gnm_fluct / np.max(gnm_fluct)
anm_norm = anm_fluct / np.max(anm_fluct)

abs_diff = np.abs(gnm_norm - anm_norm)
```

### 5. Residue-Level Analysis

- Ranked residues according to their absolute normalized fluctuation differences.
- Selected the ten residues with the largest differences.
- Reported their difference values, alignment indices, residue names, and residue numbers.

This analysis highlights positions where the two elastic network models produce different predictions of relative flexibility.

## Repository Contents

| File | Description |
|------|-------------|
| `7fay.pdb.gz` | Protein structure file provided with the project |
| `gnm-fluctuations.py` | Calculates maximum GNM squared fluctuation |
| `anm-fluctuations.py` | Calculates maximum ANM squared fluctuation |
| `fluctuation-diff.py` | Compares raw and normalized model fluctuations |
| `fluctuation-diff-index.py` | Reports the top 10 residues with the largest normalized differences |

## Usage

### Install Dependencies

```bash id="st3w6j"
pip install prody numpy
```

### 1. Calculate GNM Fluctuations

```bash id="w8ke7s"
python gnm-fluctuations.py 7fay
```

### 2. Calculate ANM Fluctuations

```bash id="9a7udu"
python anm-fluctuations.py 7fay
```

### 3. Compare GNM and ANM Fluctuations

```bash id="olrypl"
python fluctuation-diff.py 7fay
```

### 4. Identify Residues with the Largest Differences

```bash id="y6ysf3"
python fluctuation-diff-index.py 7fay
```

The scripts accept a PDB identifier as a command-line argument and print calculated results to the terminal.

## Outputs

| Output | Description |
|--------|-------------|
| Maximum GNM squared fluctuation | Largest fluctuation predicted by GNM |
| Maximum ANM squared fluctuation | Largest fluctuation predicted by ANM |
| Maximum absolute difference | Largest raw difference between model predictions |
| Maximum normalized difference | Largest difference after normalization |
| Top 10 residues | Residues ranked by normalized fluctuation differences |

Numerical results are printed to three decimal places.

## Limitations

- The analysis uses Cα atoms rather than full atomic coordinates.
- GNM and ANM are simplified elastic network models and do not represent all aspects of protein dynamics.
- Fluctuations are calculated using all nonzero modes returned by the models.
- Normalization allows comparison of relative fluctuation patterns but does not make the underlying models physically equivalent.
- The project does not include molecular dynamics simulations or experimental validation.

## Skills Demonstrated

- Structural bioinformatics
- Protein structure processing using ProDy
- Gaussian and Anisotropic Network Models
- Normal mode analysis
- Residue-level fluctuation calculations
- Numerical analysis and normalization using NumPy
- Protein sequence position and residue mapping
- Python command-line scripting

## Coursework Acknowledgment

This project was completed as part of coursework at the **University of Pittsburgh** and demonstrates computational approaches for studying protein flexibility and structural dynamics.

## Author

**Lakshita Arunkumar**

University of Pittsburgh

[GitHub Profile](https://github.com/LakshitaArunkumar)
