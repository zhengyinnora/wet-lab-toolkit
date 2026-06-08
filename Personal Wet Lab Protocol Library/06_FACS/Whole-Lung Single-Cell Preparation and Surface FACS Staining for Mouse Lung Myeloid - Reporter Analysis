# Mouse Whole-Lung Dissociation and Surface Flow Cytometry Staining Protocol

## Purpose

This protocol describes a general workflow for preparing mouse whole-lung single-cell suspensions followed by surface-marker flow cytometry staining. It is designed for lung immune-cell profiling and reporter-line analysis using endogenous fluorescent reporters such as GFP and tdTomato.

This protocol is intended for trained personnel working under approved institutional animal and biosafety regulations.

---

## Overview

Workflow:

```text
Mouse lung collection
→ enzymatic/mechanical lung dissociation
→ filtration
→ red blood cell lysis
→ Fc receptor blocking
→ viability staining
→ surface antibody staining
→ washing and resuspension
→ flow cytometry acquisition
→ gating and reporter analysis
```

---

## Reagents and materials

### Tissue dissociation and sample preparation

|Reagent / material|Example supplier|Purpose|
|---|---|---|
|Mouse Lung Dissociation Kit|Miltenyi Biotec|Enzymatic dissociation of mouse lung tissue|
|gentleMACS C Tubes|Miltenyi Biotec|Mechanical/enzymatic tissue dissociation|
|70 µm cell strainers|various|Removal of tissue debris and clumps|
|PBS|various|Washing and dilution|
|FACS buffer|PBS + serum, optionally EDTA|Cell washing and antibody dilution|
|RBC lysis buffer|eBioscience / equivalent|Red blood cell removal|
|Fc block, anti-mouse CD16/CD32|eBioscience / equivalent|Reduction of Fc receptor-mediated nonspecific antibody binding|

### Flow cytometry staining reagents

|Reagent / marker|Fluorophore / channel|Purpose|
|---|---|---|
|Fixable viability dye|e.g. FVS620 / PE-Dazzle-like channel|Dead-cell exclusion|
|CD45|fluorophore depends on panel|Leukocyte identification|
|CD11c|fluorophore depends on panel|AM / DC-associated marker|
|CD11b|fluorophore depends on panel|Myeloid marker|
|F4/80|fluorophore depends on panel|Macrophage-associated marker|
|Ly6G|fluorophore depends on panel|Neutrophil identification|
|CD64|fluorophore depends on panel|Macrophage identity|
|MerTK|fluorophore depends on panel|Mature/resident macrophage identity|
|MHCII|fluorophore depends on panel|Antigen-presenting/DC-like populations|
|GFP|endogenous reporter|Reporter signal; detected in a FITC-like channel|
|tdTomato|endogenous reporter|Reporter signal; detected in a PE-like channel|

Note: GFP and tdTomato are endogenous reporter signals and do not require anti-GFP or anti-tdTomato antibodies unless signal amplification is specifically intended.

---

## Example panel design

|Marker / signal|Example channel|Notes|
|---|---|---|
|Live/dead dye|FVS620 / PE-Dazzle-like|Requires single-stain compensation|
|CD45|BV421|CD45⁺ immune cells vs CD45⁻ fraction|
|CD11c|APC|AM / DC-related marker|
|CD11b|BV605|Myeloid cells|
|F4/80|BV650|Macrophage-associated marker|
|Ly6G|AF700|Neutrophils|
|CD64|BV711|Macrophage identity|
|MerTK|PE-Cy7|Resident/mature macrophage identity; compensation critical|
|MHCII|PerCP-based channel|DC-like / MHCII⁺ populations|
|GFP|FITC-like channel|Endogenous reporter|
|tdTomato|PE-like channel|Endogenous reporter|

Panel design notes:

- Avoid assigning other markers to FITC/AF488-like channels when GFP is used as a reporter.
    
- Avoid assigning other markers to PE-like channels when tdTomato is used as a reporter.
    
- PE-tandem dyes and viability dyes require careful compensation.
    
- Fluorophore choice should be adjusted according to the available cytometer configuration.
    

---

## Procedure

### 1. Lung collection

1. Euthanize the mouse according to the approved institutional animal protocol.
    
2. Collect the lung tissue.
    
3. Place the lung temporarily in cold PBS.
    
4. Transfer tissue into a gentleMACS C Tube or equivalent dissociation tube.
    

Optional: Perfusion may be performed if required by the experimental design. If perfusion is omitted, residual blood may increase the need for RBC lysis.

---

### 2. Lung dissociation

1. Prepare the enzyme mix according to the manufacturer’s instructions or a validated local optimization.
    
2. Add the appropriate volume of enzyme mix to each dissociation tube.
    
3. Run the appropriate lung dissociation program on a gentleMACS or equivalent tissue dissociator.
    
4. Keep the dissociation condition consistent across samples within the same experiment.
    

Note: Enzyme mix volume may need adjustment depending on whether whole lung or selected lung lobes are processed.

---

### 3. Filtration

1. Place a 70 µm strainer on a collection tube.
    
2. Pass the dissociated lung suspension through the strainer.
    
3. Wash the dissociation tube and strainer with buffer.
    
4. Collect the filtered cell suspension.
    

---

### 4. Centrifugation

Centrifuge the cell suspension using a gentle condition suitable for immune cells, for example:

```text
300–400 ×g
5–10 min
4°C
```

Discard the supernatant carefully without disturbing the pellet.

---

### 5. Red blood cell lysis

1. Resuspend the pellet in 1× RBC lysis buffer.
    
2. Incubate for the optimized time.
    
3. Stop the reaction by adding excess PBS or FACS buffer.
    
4. Centrifuge and discard the supernatant.
    

Note: RBC lysis time should be optimized for tissue amount. Over-lysis may reduce cell viability.

---

### 6. Fc receptor blocking

1. Resuspend cells in Fc block diluted in PBS or FACS buffer according to the validated protocol.
    
2. Incubate on ice or at 4°C.
    
3. Proceed to viability and/or surface staining.
    

Purpose: Fc blocking reduces nonspecific antibody binding, especially in myeloid-rich lung samples.

---

### 7. Viability staining

1. Prepare fixable viability dye according to the manufacturer’s instructions.
    
2. Dilute the dye in PBS or another protein-free buffer if required.
    
3. Incubate cells protected from light.
    
4. Wash cells before antibody staining if needed.
    

Note: Protein-containing buffers may interfere with some fixable viability dyes.

---

### 8. Surface antibody staining

1. Prepare antibody master mix in FACS buffer.
    
2. Add antibody cocktail to each sample.
    
3. Incubate protected from light at 4°C or on ice.
    
4. Wash cells with FACS buffer.
    
5. Resuspend cells in FACS buffer for acquisition.
    
6. Filter cells before running on the cytometer to reduce clumping.
    

---

## Compensation and controls

Recommended controls:

|Control|Purpose|
|---|---|
|Unstained cells|Autofluorescence and background|
|Single-stain antibody controls|Compensation|
|Viability dye single-stain control|Live/dead compensation|
|GFP-positive and GFP-negative cells|GFP reporter gate and compensation check|
|tdTomato-positive and tdTomato-negative cells|tdTomato reporter gate and compensation check|
|WT / no-reporter control|Reporter background and lung autofluorescence|

Notes:

- Antibody capture beads are suitable for many antibody-conjugated fluorophores.
    
- Amine-reactive compensation beads should be used for fixable viability dyes when appropriate.
    
- Endogenous GFP and tdTomato are best controlled using true reporter-positive and reporter-negative biological samples.
    

---

## Acquisition notes

1. Use a saved cytometer template when running repeated batches.
    
2. Verify the settings with daily controls.
    
3. Keep voltages/gains consistent within each experiment.
    
4. Record cytometer name, template name, compensation setup, and event number.
    
5. Avoid comparing MFI across batches unless the instrument setup is standardized appropriately.
    

---

## Suggested gating strategy

General gating order:

```text
All events
→ FSC/SSC to remove debris
→ singlets
→ live cells
→ CD45⁺ vs CD45⁻
→ lung immune populations
→ reporter signal overlay
```

Example population definitions:

|Population|Example gating logic|
|---|---|
|Alveolar macrophages|CD45⁺ SiglecF⁺ CD11c⁺ CD11b low/− F4/80⁺ CD64⁺|
|Eosinophils|CD45⁺ SiglecF⁺ CD11b⁺ CD11c low/−, SSC high|
|Neutrophils|CD45⁺ Ly6G⁺ CD11b⁺|
|Macrophage-like / IM-like cells|CD45⁺ CD11b⁺ F4/80⁺ CD64⁺ SiglecF⁻|
|DC-like cells|CD45⁺ CD11c⁺ MHCII⁺ CD64 low/−|
|CD45⁻ fraction|Non-immune / structural-enriched cells|

Reporter analysis:

1. **Reporter efficiency**: percentage of reporter-positive cells within each defined cell population.
    
2. **Reporter specificity / composition**: cellular composition of reporter-positive cells.
    

---

## Troubleshooting

|Issue|Possible reason|Suggested action|
|---|---|---|
|Low cell yield|Incomplete dissociation|Check tissue amount, enzyme volume, dissociation program|
|High debris|Harsh dissociation or tissue over-processing|Avoid forcing tissue through the filter|
|High red blood cell contamination|No perfusion or insufficient RBC lysis|Optimize RBC lysis time|
|High background staining|Fc receptor-mediated binding or dead cells|Use Fc block and viability dye|
|Reporter gate unclear|Autofluorescence or insufficient controls|Include WT/no-reporter and reporter-positive controls|
|Poor GFP/tdTomato separation|Channel conflict or compensation issue|Avoid FITC/PE-conjugated antibodies and use appropriate controls|

---

## Notes

This protocol is a general guide and should be adapted to local animal protocols, cytometer configuration, tissue amount, and validated antibody titrations.
