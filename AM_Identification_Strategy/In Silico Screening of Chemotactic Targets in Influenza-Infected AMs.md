### **Protocol: In Silico Screening of Chemotactic Targets in Influenza-Infected AMs**

**Date:** 2025-12-18

**Author:** Nora

**Context:** Utilization of **Influenza-infected mouse lung data** as a biological proxy to identify inducible chemotactic receptors on Alveolar Macrophages (AMs) under acute lung injury conditions.

#### **1. Objective & Rationale (Why Influenza?)**

To identify potential chemotactic receptors (e.g., *Fpr1/2, Cxcr4*) that are upregulated in AMs upon inflammatory activation.

* **Scientific Justification:** Carbon Nanotube (CNT) exposure induces sterile inflammation, cell necrosis, and tissue repair requirements similar to the **post-viral injury phase** (e.g., Influenza Day 7-14).
* **Strategic Goal:** Since steady-state AMs are "sessile" (receptor-negative), the Influenza model serves as a **Positive Control** to demonstrate that specific receptors (*Fpr1/2*) are **inducible** and biologically relevant for AM motility in a damaged environment.
* Due to the lack of public fibrosis models with single-cell resolution, Influenza-induced lung injury serves as a biologically relevant surrogate to identify inducible chemotactic programs in AMs. The emphasis is not on replicating CNT per se, but on identifying potential receptors responsive to necrosis or inflammation.

#### **2. Database & Tool Configuration**

To reproduce the analysis, use the following settings:

* **Platform:** [CZI CellxGene Discovery](https://cellxgene.cziscience.com/)
* **Mode:** Explorer (UMAP/Embedding View) -> Datasets
* **Filters:**
* **Organism:** *Mus musculus*
* **Tissue:** Lung
* **Disease:** **Influenza** (Must exclude "Normal" to focus on activated state).
* **Timepoint (Optional):** Focus on Day 7+ (Repair/Resolution phase) if available.



#### **3. Gene Panel Selection (The "Screening List")**

The following genes were selected to screen for inducible migration markers based on the "Inflammation-Repair" hypothesis.

| Gene Symbol | Protein (CD) | Role in Strategy & Expected Outcome |
| --- | --- | --- |
| **Siglecf** | - | **Identity Marker.** Anchors the AM population. |
| **Mrc1** | CD206 | **Identity Marker.** Confirms AM identity (co-expressed with *Siglecf*). |
| **Fpr1** | - | **Primary Hit (Confirmed).** Pattern recognition receptor for bacterial peptides and mitochondrial DAMPs (released by necrosis). **Significantly overlaps with AMs in Influenza model.** |
| **Fpr2** | - | **Primary Hit (Confirmed).** Functional homolog to *Fpr1*. Indicates sensing of cellular damage. |
| **Cxcr4** | CD184 | **Candidate (Check).** Homing receptor for CXCL12 (tissue repair). Checked for potential upregulation. |
| **Ccr2** | CD192 | **Candidate (Check).** Monocyte recruitment signal. Checked to distinguish recruited Monocytes vs. resident AMs. |
| **Ccr5** | CD195 | **Candidate (Check).** Inflammatory chemokine receptor (CCL3/4/5). Often associated with viral response ("Cytokine Storm"). |

#### **4. Step-by-Step Reproduction Guide**

Follow these steps to visualize the phenotype switching:

1. **Initialize Dataset:** Load the **Influenza** infected mouse lung dataset.
2. **Input Gene List:** Enter `Siglecf`, `Mrc1`, `Fpr1`, `Fpr2`, `Cxcr4`, `Ccr2`, `Ccr5`.
3. **Visualization (Color by Gene):**
* Locate the **Siglecf+ / Mrc1+** cluster (Activated AMs).
* Toggle **Fpr1** and **Fpr2**.


4. **Co-localization Check (The Discovery):**
* **Observe:** Unlike in the Healthy baseline, the Influenza-AM cluster shows distinct **positive expression (Heatmap signal)** for *Fpr1/2*.
* **Compare:** Check *Cxcr4* and *Ccr2*. If overlap is minimal, conclude that the migration mode is likely **short-range chemotaxis (via Fpr)** rather than distant homing (via Cxcr4).



#### **5. Conclusion & Translation to Wet Lab**

* **In Silico Conclusion:** AMs possess an **inducible** chemotactic program. Specifically, **Fpr1/2** are upregulated in response to lung injury (Influenza), while *Ccr2/Cxcr4* remain low/negative.
* **Hypothesis for CNT Project:** CNT-induced necrosis (mitochondrial release) likely mimics the "danger signal" landscape of Influenza, triggering the same **Fpr-dependent** motility mechanism.
* **Action Plan:**
* **Target:** Focus wet-lab migration assays on **FPR agonists (fMLP, WKYMVm)**.
* **Control:** Use *Cxcr4* as a likely negative control for this specific migration mode.
