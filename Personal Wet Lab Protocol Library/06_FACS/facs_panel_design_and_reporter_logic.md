# FACS Panel Design and Reporter Logic for Mouse Lung Myeloid / Reporter-Line Analysis

## Purpose

This document summarizes the rationale behind a surface flow cytometry panel designed for mouse whole-lung single-cell suspensions. The panel is intended to map endogenous reporter signals, such as GFP and tdTomato, onto major lung immune and non-immune cell compartments.

The main goal is not only to detect whether a reporter signal is present, but to determine:

1. **Reporter efficiency**: What percentage of a defined cell population is reporter-positive?
2. **Reporter specificity / composition**: What cell types make up the reporter-positive population?

This logic is especially useful for validating reporter mouse lines before using them for lineage tracing, localization, or functional studies.

---

## Core Concept

The panel contains two types of information:

1. **Identity markers**
   These define the cell populations.

2. **Reporter signals**
   These indicate which cells are labeled by the reporter mouse line.

In other words:

```text
Identity markers tell us who the cells are.
Reporter signals tell us which cells the mouse line labels.
```

The analysis should therefore proceed by first defining cell populations using surface markers, and then overlaying the endogenous reporter signal onto those defined populations.

---

## Example Panel

| Marker / Signal | Example Fluorophore / Channel   | Main Purpose                               |
| --------------- | ------------------------------- | ------------------------------------------ |
| Live/Dead dye   | FVS620 / PE-Dazzle-like channel | Exclude dead cells                         |
| CD45            | BV421                           | Immune vs CD45-negative cells              |
| CD11c           | APC                             | AMs and DC-like cells                      |
| CD11b           | BV605                           | Myeloid cells                              |
| F4/80           | BV650                           | Macrophage-associated marker               |
| Ly6G            | AF700                           | Neutrophils                                |
| CD64            | BV711                           | Macrophage identity                        |
| MerTK           | PE-Cy7                          | Mature / resident macrophage identity      |
| MHCII           | PerCP-based channel             | DC-like and antigen-presenting populations |
| GFP             | FITC-like channel               | Endogenous reporter signal                 |
| tdTomato        | PE-like channel                 | Endogenous reporter signal                 |

This is an example panel and should be adapted to the available cytometer configuration, antibody clones, fluorophore brightness, and compensation performance.

---

## Reporter Channel Logic

### GFP

GFP is an endogenous fluorescent reporter and is typically detected in a FITC-like channel.

Therefore:

* Do not assign important antibody markers to FITC / AF488-like channels when GFP is used as a reporter.
* GFP should be analyzed using appropriate GFP-positive and GFP-negative controls.
* Autofluorescence must be considered, especially in lung macrophages.

### tdTomato

tdTomato is an endogenous fluorescent reporter and is typically detected in a PE-like channel.

Therefore:

* Do not assign important antibody markers to PE-like channels when tdTomato is used as a reporter.
* tdTomato should be analyzed using tdTomato-positive and tdTomato-negative controls.
* Compensation with nearby channels, especially PE-tandem or PE-related channels, should be checked carefully.

### Important distinction

GFP and tdTomato are not antibody stains in this setup.

They should be listed as:

```text
GFP: endogenous reporter, detected in FITC-like channel
tdTomato: endogenous reporter, detected in PE-like channel
```

No anti-GFP or anti-tdTomato antibody is required unless signal amplification is specifically intended.

---

## Marker Rationale

### CD45

CD45 is used to separate immune cells from CD45-negative cells.

| Gate          | Interpretation                            |
| ------------- | ----------------------------------------- |
| CD45-positive | Immune cells                              |
| CD45-negative | Non-immune / structural-enriched fraction |

The CD45-negative fraction should not be discarded automatically, especially when analyzing reporter lines that may label structural, stromal, epithelial, endothelial, or fibroblast-like compartments.

---

### SiglecF-related interpretation

In mouse lung, SiglecF is useful for identifying alveolar macrophages, but it is not sufficient by itself because eosinophils can also be SiglecF-positive.

Therefore, SiglecF should be interpreted together with CD11c, CD11b, SSC, and macrophage markers.

General distinction:

| Population           | Typical pattern                             |
| -------------------- | ------------------------------------------- |
| Alveolar macrophages | CD45+ SiglecF+ CD11c+ CD11b low/−           |
| Eosinophils          | CD45+ SiglecF+ CD11b+ CD11c low/−, SSC high |

This distinction is especially important when validating SiglecF-associated reporter lines.

---

### CD11c

CD11c is expressed by alveolar macrophages and dendritic-cell-like populations.

Therefore, CD11c alone should not be interpreted as an AM-specific marker.

It is useful in combination with:

* SiglecF for AMs
* MHCII for DC-like populations
* CD64 / MerTK to support macrophage identity

---

### CD11b

CD11b helps identify myeloid populations, including eosinophils, neutrophils, monocytes, interstitial macrophage-like cells, and other CD11b-positive myeloid cells.

It is particularly useful for distinguishing AMs from eosinophils:

```text
AMs: SiglecF+ CD11c+ CD11b low/−
Eosinophils: SiglecF+ CD11b+ CD11c low/−
```

---

### F4/80

F4/80 supports macrophage identity, but it should not be used alone to define macrophages.

It is most useful when combined with CD64, MerTK, SiglecF, CD11b, and CD11c.

---

### Ly6G

Ly6G is used to identify neutrophils.

Typical neutrophil gate:

```text
CD45+ Ly6G+ CD11b+
```

Including Ly6G helps prevent neutrophils from being incorrectly included in broader CD11b-positive myeloid gates.

---

### CD64

CD64 is a strong macrophage identity marker and helps distinguish macrophages from dendritic-cell-like populations.

It is especially useful for:

* Supporting AM identity
* Identifying macrophage-like / interstitial macrophage-like populations
* Distinguishing macrophages from CD11c+ DC-like cells

Example:

```text
Macrophage-like cells: CD45+ CD64+ F4/80+ MerTK+
DC-like cells: CD45+ CD11c+ MHCII+ CD64 low/−
```

---

### MerTK

MerTK supports mature or resident macrophage identity.

It is useful together with CD64 and F4/80 to define macrophage-like populations more confidently.

Because MerTK may be conjugated to PE-Cy7 or another tandem dye, compensation should be checked carefully.

---

### MHCII

MHCII helps identify antigen-presenting and DC-like populations.

It is useful for distinguishing:

* DC-like cells
* MHCII-positive interstitial macrophage-like cells
* Other antigen-presenting immune populations

MHCII should be interpreted together with CD11c, CD64, MerTK, SiglecF, and CD11b.

---

## Why Ly6C May Be Optional

Ly6C is useful for identifying monocytes, especially inflammatory or recruited monocytes.

However, for a reporter-line characterization panel focused primarily on AMs, eosinophils, neutrophils, macrophage-like cells, DC-like cells, and CD45-negative cells, Ly6C may be omitted to simplify the panel.

If Ly6C is not included, monocyte-related conclusions should be written conservatively.

Instead of saying:

```text
monocytes
```

it may be safer to write:

```text
CD11b+ Ly6G− SiglecF− myeloid-like cells
```

or:

```text
non-neutrophil CD11b+ myeloid-like cells
```

depending on the available markers.

Ly6C or CCR2 can be added in a separate inflammatory myeloid panel if monocyte recruitment becomes a central question.

---

## Suggested Gating Strategy

A general gating order is:

```text
All events
→ FSC/SSC to remove debris
→ Singlets
→ Live cells
→ CD45+ vs CD45−
→ Define major lung populations
→ Overlay GFP / tdTomato reporter signal
```

---

## Example Population Definitions

These are example definitions and should be adapted to staining quality, cytometer configuration, and biological context.

| Population                      | Example gating logic                                        |
| ------------------------------- | ----------------------------------------------------------- |
| Alveolar macrophages            | CD45+ SiglecF+ CD11c+ CD11b low/− F4/80+ CD64+              |
| Eosinophils                     | CD45+ SiglecF+ CD11b+ CD11c low/−, SSC high                 |
| Neutrophils                     | CD45+ Ly6G+ CD11b+                                          |
| Macrophage-like / IM-like cells | CD45+ CD11b+ F4/80+ CD64+ MerTK+ SiglecF−                   |
| DC-like cells                   | CD45+ CD11c+ MHCII+ CD64 low/−                              |
| CD45-negative fraction          | CD45− live singlets; non-immune / structural-enriched cells |

When a marker combination is incomplete, the population name should be conservative. For example, use “macrophage-like” or “DC-like” rather than definitive cell-type labels if the panel does not fully support the identity.

---

## Reporter Analysis

### 1. Reporter efficiency

Reporter efficiency asks:

```text
Within a defined cell population, what percentage of cells are reporter-positive?
```

Example:

```text
Among AMs, what percentage is tdTomato-positive?
Among CD45-negative cells, what percentage is GFP-positive?
```

This is:

```text
Cell type → Reporter
```

---

### 2. Reporter specificity / composition

Reporter specificity asks:

```text
Among all reporter-positive cells, what cell types are represented?
```

Example:

```text
Among all tdTomato-positive lung cells, what percentage are AMs?
Among all GFP-positive lung cells, what percentage are CD45-negative cells?
```

This is:

```text
Reporter → Cell type
```

Both readouts are needed.

A reporter line can show high efficiency in a target population but still lack specificity if many non-target cells are also reporter-positive.

---

## CD11c-Cre-GFP × Ai14 Dual-Reporter Logic

Some reporter lines may contain both a direct GFP reporter and an Ai14 tdTomato recombination reporter.

In a CD11c-Cre-GFP × Ai14 dual-reporter system:

| Signal   | Interpretation                                       |
| -------- | ---------------------------------------------------- |
| GFP      | Current or recent CD11c-associated reporter activity |
| tdTomato | Historical Cre-mediated Ai14 recombination           |

Therefore, this line should not be analyzed as a simple single-reporter line.

Instead, GFP and tdTomato should be analyzed:

1. Separately
2. In combination using GFP vs tdTomato quadrant gating

Example quadrants:

| FACS phenotype | Interpretation                                                        |
| -------------- | --------------------------------------------------------------------- |
| GFP+ tdTomato+ | Current/recent CD11c-associated activity and historical recombination |
| GFP− tdTomato+ | Historical recombination, but current GFP signal is low or absent     |
| GFP+ tdTomato− | Current/recent GFP signal without detectable Ai14 recombination       |
| GFP− tdTomato− | No detectable GFP or tdTomato reporter signal                         |

This analysis may help distinguish current reporter activity from historical lineage/recombination history.

---

## Compensation and Control Strategy

Recommended controls include:

| Control                          | Purpose                                          |
| -------------------------------- | ------------------------------------------------ |
| Unstained cells                  | Background and autofluorescence                  |
| Single-stained antibody controls | Compensation                                     |
| Live/dead single-stain control   | Viability dye compensation                       |
| GFP-positive cells               | GFP reporter gate and compensation check         |
| GFP-negative / WT cells          | GFP background                                   |
| tdTomato-positive cells          | tdTomato reporter gate and compensation check    |
| tdTomato-negative / WT cells     | tdTomato background                              |
| WT / no-reporter lung cells      | Autofluorescence and reporter-negative reference |

Important notes:

* Antibody capture beads can be used for antibody-conjugated fluorophores.
* Amine-reactive compensation beads should be used for fixable viability dyes when appropriate.
* Endogenous GFP and tdTomato are best controlled using true reporter-positive and reporter-negative biological samples.
* Lung macrophages can be highly autofluorescent, so unstained and no-reporter controls are important.

---

## Batch and Acquisition Considerations

For multi-batch experiments:

1. Use the same antibody panel and staining protocol.
2. Use a saved cytometer template as a starting point.
3. Verify voltages and compensation with daily controls.
4. Avoid changing acquisition settings within the same batch.
5. Keep batch design balanced across reporter lines whenever possible.
6. Prefer reporter-positive percentages and population composition as primary readouts rather than cross-batch MFI comparisons.

Example balanced batch logic:

```text
Each batch contains one mouse from each reporter line.
```

This helps reduce confounding between reporter-line effects and batch effects.

---

## Interpretation Principles

### Avoid overclaiming

If the panel lacks a key marker for a population, use conservative terminology.

Examples:

| Stronger claim           | Safer wording                            |
| ------------------------ | ---------------------------------------- |
| Monocytes                | CD11b+ Ly6G− SiglecF− myeloid-like cells |
| Interstitial macrophages | Macrophage-like / IM-like cells          |
| Dendritic cells          | DC-like cells                            |

### Separate technical signal from biological interpretation

Reporter-positive cells should not automatically be interpreted as the intended target population.

The goal of the panel is to determine the actual reporter distribution in the lung, not to assume it.

---

## Summary

This panel is designed to answer two central questions:

1. **Where does the reporter signal appear across lung cell populations?**
2. **How specific and efficient is the reporter labeling for the intended target population?**

The key logic is:

```text
First define cell identity with surface markers.
Then map GFP or tdTomato reporter signal onto the defined cell populations.
Finally calculate reporter efficiency and reporter-positive cell composition.
```

This approach supports systematic reporter-line validation in whole-lung single-cell suspensions.
