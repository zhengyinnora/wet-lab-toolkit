**Protocol: In Silico Establishment of Alveolar Macrophage Chemotaxis Baseline**

**Date:** 2025-12-18 **Author:** Nora

**Context:** Validation of steady-state receptor expression profile to distinguish "Sessile" vs. "Migratory" Alveolar Macrophages (AMs).

### 1. Objective

To establish the baseline gene expression signature of chemotactic receptors (e.g., *Ccr2, Cxcr4, Fpr*) in steady-state Alveolar Macrophages (AMs) using public single-cell RNA sequencing (scRNA-seq) data. This protocol confirms the **non-migratory phenotype** of healthy AMs, serving as a negative control for subsequent CNT-induced migration studies.

### 2. Database & Tool Configuration

To reproduce the analysis, use the following settings:

* **Platform:** [CZI CellxGene Discovery](https://cellxgene.cziscience.com/)
* **Mode:** Explorer (UMAP/Embedding View) -> Datasets
* **Filters:**
* **Organism:** *Mus musculus*
* **Tissue:** Lung
* **Dataset:** *Tabula Muris Senis* (or *Mouse Lung Atlas* by Angelidis et al.) - **Must ensure dataset is "Healthy" or "Naive" (Non-fibrotic/Non-infected).**



### 3. Gene Panel Selection (The "Why")

The following genes were selected to construct a logical gate for AM chemotaxis potential.

| Gene Symbol | Protein (CD) | Cell Type Target | Role in Strategy |
| --- | --- | --- | --- |
| **Siglecf** | - | AMs | **Identity Marker.** The definitive marker for murine AMs; used to anchor the population of interest. |
| **Mrc1** | CD206 | AMs (M2-like) | **Identity Marker.** Co-localization with *Siglecf* confirms the population as Resident AMs. |
| **Ccr2** | CD192 | Monocytes | **Negative Control (Chemotaxis).** Recruitment signal. Should NOT overlap with steady-state AMs. |
| **Cxcr4** | CD184 | Migrating Cells | **Negative Control (Chemotaxis).** Homing signal. Absence indicates "sessile" (non-moving) state. |
| **Fpr1/2** | - | Neutrophils/Mono | **Negative Control (Chemotaxis).** Bacterial sensing. Absence indicates lack of acute activation. |
| **C5ar1** | CD88 | Myeloid cells | **Negative Control.** Complement receptor. Low/Negative in resting AMs. |

### 4. Step-by-Step Reproduction Guide

Follow these steps to visualize the phenotype separation:

1. **Initialize Dataset:** Open the CZI CellxGene "Explorer" interface for the mouse lung dataset (Healthy).
2. **Input Gene List:** In the right-hand "Genes" search bar, enter the following list:
* `Siglecf`
* `Mrc1`
* `Ccr2`
* `Cxcr4`
* `Fpr1`
* `Fpr2`
* `C5ar1`


3. **Visualization (Color by Gene):**
* Click the "droplet" icon next to `Siglecf` -> Identify the high-expression cluster (AMs).
* Click the "droplet" icon next to `Cxcr4` / `Ccr2` -> Note the location of these expressing cells (likely Monocytes/B cells).


4. **Co-localization Check (The Logic):**
* **Crucial Step:** Verify that the `Siglecf` high cluster **DOES NOT** overlap with `Cxcr4` or `Ccr2` high clusters.
* *Observation:* The AM cluster should appear "cold" (blue/grey) for chemotactic receptors.



### 5. Validation of "Sessile" Baseline (Findings)

Based on the *in silico* separation observed above, the following baseline is established:

* **Phenotype Definition:** Steady-state AMs are defined as **Siglecf(High) / Mrc1(+) / Ccr2(-) / Cxcr4(-) / Fpr(-)**.
* **Biological Interpretation:**
* The lack of overlap confirms that healthy AMs are "sessile" (tissue-resident and non-migratory).
* Any detection of these receptors in future experimental groups (e.g., CNT-treated) can be attributed to **induced activation**, not baseline expression.


* **Experimental Implication:**
* **For FACS:** A "Shift" in geometric mean fluorescence intensity (gMFI) for CXCR4/CCR2 on Siglecf+ cells is required to prove migration potential. The baseline gMFI should be low (comparable to FMO control).
