# Genotyping Protocol – PCR-Based Strategy  
**Sample type:** Mouse ear / tail biopsies  
**Last updated:** 2026-01-07  
**Author:** Nora  

---

## 🧪 Day 1 — DNA Extraction (Tissue Lysis)

1. Collect samples.  
   > Keep original labels (tube ID, tissue info) until genotyping results are confirmed.

2. Prepare **PBND buffer** and **proteinase K enzyme**.

3. Calculate required volumes:  
   Each sample requires:
   - PBND buffer: **150 µL**
   - Proteinase K: **3 µL**

   **Example:** For 43 samples, prepare for 50:
   - PBND buffer: 150 µL × 50 = **7.5 mL**
   - Enzyme: 3 µL × 50 = **150 µL**

4. Mix buffer and enzyme:
   - Use 10 mL cube for preparation.
   - Pipette 150 µL of the buffer+enzyme mix into each sample tube.
   - Use **filtered tips** and **change tips between samples** (essential for DNA/RNA experiments).

5. Incubate overnight:  
   **65 °C, 150 rpm**  
   > Optimal for proteinase K activity.

---

## ⚗️ Day 2 — DNA Purification & PCR Setup

### 1. Enzyme Inactivation

- Incubate samples at **95 °C for 15 min** to:
  - Denature proteins
  - Inactivate proteinase K

### 2. Centrifugation

- Spin at **13,000 rpm for 10 min**
- Collect the supernatant (~**100 µL**) containing genomic DNA.
- Transfer to new labeled tubes:
  - **Tube body:** use last 4 digits of internal ID (e.g., DBXXXX)
  - **Lid:** include sample name + ear tag info

---

### 3. PCR Master Mix Preparation

> Use **DreamTaq Green 10× buffer**, which contains loading dye.  
> ⚠️ *Not compatible with qPCR or enzymatic cloning.*

#### Prepare for:
- Actual number of samples  
- Controls: positive (e.g. homozygous, heterozygous) + **water** as NTC

**Example:**  
If 7 samples + 2 controls + 1 water → **10 tubes**, prepare for 14–15.

**Per reaction (20 µL total volume):**
- 2.0 µL DNA sample / control / water  
- 2.0 µL 10× DreamTaq Green Buffer  
- 2.0 µL dNTPs (2 mM each)  
- 2.0 µL primer mix  
- 0.1 µL DreamTaq Polymerase  
- 11.9 µL H₂O (adjust to 20 µL total)

#### Setup:

- Add **2 µL DNA** into each PCR strip tube (8-well).
- Then add **18 µL PCR master mix** to each tube.
- Final volume: **20 µL per reaction**

### 4. PCR Program

- Run overnight in thermal cycler with appropriate genotyping program.

---

## 🧫 Day 3 — Gel Electrophoresis & Imaging

---

### 1. Gel Preparation

**Reagents:**
- 2% agarose gel = 2 g agarose + 100 mL 1× TBE
- 5 µL **Midori Green dye** (for DNA staining)

**Steps:**
1. Mix agarose + TBE in a 500 mL flask.
2. Microwave (~3 min) until fully melted.
3. Adjust final volume to 100 mL (compensate evaporation).
4. Add Midori Green, swirl gently (avoid bubbles).
5. Pour into casting tray and insert comb.
6. Let solidify for 20–30 min.

> ⚠️ Handle Midori Green in fume hood.  
> Waste liquid must go into designated container.

---

### 2. Gel Loading & Electrophoresis

1. Place gel in tank, cover with 1× TBE buffer.
2. Load **5–6 µL DNA ladder** (MassRuler Low Range).
   - First well of each row = ladder.
3. Load **5–10 µL PCR product** into each well.
4. Run at **100–120 V** for **45–60 min**.

**DNA Ladder Functions:**
- Size reference
- Success check (whether bands match expectations)
- Internal control for gel quality (e.g., distorted bands = uneven voltage)

---

### 3. Gel Imaging

**Equipment:** Bio-Rad Imaging System

Steps:
1. Insert USB drive or SD card for image storage.
2. Place gel centered in imaging chamber.
3. Click “Live” to view bands in real time.
4. Adjust position, close lid fully.
5. Switch to **UV or blue light** (Midori is safer with blue).
6. Observe bands, adjust exposure.
7. Click “Capture” or “Save” image.
8. Optionally switch to white light and capture again.

**Tips:**
- Keep consistent gel orientation (ladder on same side).
- Avoid over/underexposure.
- Backup images immediately to PC.
- Faint ladder? → check buffer volume, voltage, dye quality.

---

## 🧠 Notes

- If bands between 100–200 bp are hard to distinguish, refer to the ladder sheet.
- Actual PCR product size depends on your genotyping primer design – refer to gene-specific protocol.
- Always include water control to rule out contamination.
- For Midori Green: blue light imaging preferred to reduce DNA damage.

---

