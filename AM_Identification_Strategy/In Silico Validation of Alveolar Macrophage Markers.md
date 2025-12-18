# Protocol: In Silico Validation of Alveolar Macrophage Markers

**Date:** 2025-12-17
**Author:** Nora
**Context:** Validation of *Siglecf*-Cre/tdTomato reporter specificity.

## 1. Objective
To establish a reproducible gene signature for distinguishing Alveolar Macrophages (AMs) from Eosinophils and Interstitial Macrophages (IMs) using public single-cell RNA sequencing (scRNA-seq) data. This protocol defines the gene panel used to guide wet-lab antibody selection (FACS/IF).

## 2. Database & Tool Configuration
To reproduce the analysis, use the following settings:

* **Platform:** [CZI CellxGene Discovery](https://cellxgene.cziscience.com/)
* **Mode:** Explorer (UMAP/Embedding View)
* **Filters:**
    * **Organism:** *Mus musculus*
    * **Tissue:** Lung
    * **Dataset:** *Tabula Muris Senis* (or *Mouse Lung Atlas* by Angelidis et al.)

## 3. Gene Panel Selection (The "Why")

The following genes were selected to construct a logical gate for AM identification.

| Gene Symbol | Protein (CD) | Cell Type Target | Role in Strategy |
| :--- | :--- | :--- | :--- |
| **Itgax** | CD11c | AMs, DCs | **Baseline Marker.** Defines the broad myeloid population in the lung airspace. |
| **Mrc1** | CD206 | AMs | **Positive Selector.** Highly specific to AMs; used to confirm *Siglecf*-Cre targets. |
| **Fcgr1** | CD64 | Macrophages (AM + IM) | **Lineage Gate.** Distinguishes Macrophages from Dendritic Cells (DCs). |
| **Cd68** | CD68 | Pan-Macrophage | **Broad Control.** Confirming general macrophage identity (though less specific than Mrc1). |
| **Prg2** | - | Eosinophils | **Negative Selector.** Major Basic Protein. Used to identify the "Exclude" population. |
| **Ccr3** | CD193 | Eosinophils | **Negative Selector.** Confirming Eosinophil identity alongside Prg2. |

## 4. Step-by-Step Reproduction Guide

Follow these steps to visualize the cluster separation:

1.  **Initialize Dataset:** Open the CZI CellxGene "Explorer" interface for the mouse lung dataset.
2.  **Input Gene List:** In the right-hand "Genes" search bar, enter the following list:
    * `Mrc1`
    * `Prg2`
    * `Itgax`
    * `Ccr3`
    * `Fcgr1`
    * `Cd68`
3.  **Visualization (Color by Gene):**
    * Click the "droplet" icon next to **`Prg2`** -> Note the location of the Eosinophil cluster.
    * Click the "droplet" icon next to **`Mrc1`** -> Note the location of the AM cluster.
    * *Observation:* These two clusters should be distinct and non-overlapping.
4.  **Co-localization Check (The Logic):**
    * Verify that **`Itgax`** and **`Fcgr1`** overlap significantly with the `Mrc1` cluster.
    * Verify that **`Ccr3`** strictly overlaps with the `Prg2` cluster.

## 5. Translation to Wet Lab (Experimental Logic)

Based on the *in silico* separation observed above, the following antibody strategy is validated:

* **For FACS:**
    * Gate: `CD45+` -> `Lin-` -> `CD64+` (to match *Fcgr1* expression) -> `Siglecf+` / `CD206+`.
* **For Histology (IF):**
    * **Primary Target:** **CD206 (Anti-Mrc1)**.
    * **Justification:** *Mrc1* shows the cleanest separation from *Prg2*+ Eosinophils in the dataset, providing a higher signal-to-noise ratio than *Cd68* or *Fcgr1* for morphological identification.

---
*Note: This analysis utilizes wild-type (WT) public data to establish the baseline phenotype. The actual reporter mouse (Cre+) should mimic the Mrc1+ population identified here.*
