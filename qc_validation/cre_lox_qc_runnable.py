import sys

# --- 1. Define Mock Objects ---
# To make the logic executable, we create mock "Mouse" and "FACS Data" classes.

class MockMouseSample:
    def __init__(self, id, genotype, tail_fluorescence):
        self.id = id
        self.genotype = genotype
        self.tail_fluorescence = tail_fluorescence

    def check_fluorescence(self, tissue):
        # Simulating microscope inspection logic
        if tissue in ["tail", "ear"]:
            return self.tail_fluorescence
        return "UNKNOWN"

class MockFACSData:
    def __init__(self, tissue, histogram_peak):
        self.tissue = tissue
        self.histogram_peak = histogram_peak

# --- 2. Core QC Logic ---

class MouseModelQC:
    """
    Quality Control Logic for Siglecf-AI14 Cre-LoxP System.
    Automates the decision tree for validating recombination specificity.
    """
    def __init__(self, strain_name="Siglecf-AI14"):
        self.strain = strain_name
        print(f"🔹 Initializing QC protocol for {self.strain}...")

    def check_ai14_stock_integrity(self, mouse):
        """
        Validates Hypothesis 1: Spontaneous Recombination in the AI14 stock.
        """
        print(f"   [Step 1] Checking AI14 Stock Integrity for Mouse {mouse.id}...")
        
        if mouse.genotype == "Cre-:AI14+" and mouse.check_fluorescence("tail") == "RED":
            print("      ❌ CRITICAL FAILURE: AI14 Stock is compromised (Stop cassette lost).")
            return "DISCARD_COLONY"
        
        elif mouse.genotype == "Cre-:AI14+" and mouse.check_fluorescence("tail") == "BLACK":
            print("      ✅ PASS: AI14 Stock is clean (Stop cassette intact).")
            return "PROCEED"
        
        return "N/A (Wrong Genotype)"

    def check_germline_excision(self, mouse):
        """
        Validates Hypothesis 2: Germline Excision (Leakage during zygote stage).
        """
        print(f"   [Step 2] Checking Germline Excision for Mouse {mouse.id}...")
        
        if mouse.genotype == "Cre+:AI14+" and mouse.check_fluorescence("tail") == "RED":
            print("      ⚠️ WARNING: Germline Excision Detected! (Whole body recombination).")
            print("         -> Recommendation: Switch breeding strategy (Female Cre x Male Reporter).")
            return "BREEDING_ERROR"
        
        elif mouse.genotype == "Cre+:AI14+" and mouse.check_fluorescence("tail") == "BLACK":
            print("      ✅ PASS: Cre is specific. No germline leakage detected.")
            return "SUCCESS"

# --- 3. Execution Script ---

if __name__ == "__main__":
    # Initialize the QC System
    qc_system = MouseModelQC()
    print("-" * 60)

    # === Scenario A: The "Nightmare" Case (Ubiquitous Red) ===
    # Simulates a mouse with germline excision
    print("\n🧪 Running Diagnosis on: 'Suspicious Mouse A'...")
    bad_mouse = MockMouseSample(id="M001", genotype="Cre+:AI14+", tail_fluorescence="RED")
    qc_system.check_germline_excision(bad_mouse)

    # === Scenario B: The Expected Control (Clean Stock) ===
    # Simulates a Cre-negative littermate
    print("\n🧪 Running Diagnosis on: 'Control Mouse B'...")
    control_mouse = MockMouseSample(id="M002", genotype="Cre-:AI14+", tail_fluorescence="BLACK")
    qc_system.check_ai14_stock_integrity(control_mouse)
    
    # === Scenario C: The Perfect Result ===
    # Simulates a specific, working Cre model
    print("\n🧪 Running Diagnosis on: 'Perfect Mouse C'...")
    good_mouse = MockMouseSample(id="M003", genotype="Cre+:AI14+", tail_fluorescence="BLACK")
    qc_system.check_germline_excision(good_mouse)

    print("\n" + "-" * 60)
    print("🎉 Done! Protocol execution complete. Validation finished.")
