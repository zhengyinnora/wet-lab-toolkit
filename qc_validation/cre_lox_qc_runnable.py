import sys

# --- 1. 定义模拟对象 (Mock Objects) ---
# 为了让代码能跑，我们需要造一些假的“老鼠”和“流式数据”

class MockMouseSample:
    def __init__(self, id, genotype, tail_fluorescence):
        self.id = id
        self.genotype = genotype
        self.tail_fluorescence = tail_fluorescence

    def check_fluorescence(self, tissue):
        # 模拟显微镜检查
        if tissue in ["tail", "ear"]:
            return self.tail_fluorescence
        return "UNKNOWN"

class MockFACSData:
    def __init__(self, tissue, histogram_peak):
        self.tissue = tissue
        self.histogram_peak = histogram_peak

# --- 2. 核心逻辑 (QC Logic) ---

class MouseModelQC:
    """
    Quality Control Logic for Siglecf-AI14 Cre-LoxP System.
    """
    def __init__(self, strain_name="Siglecf-AI14"):
        self.strain = strain_name
        print(f"🔹 Initializing QC protocol for {self.strain}...")

    def check_ai14_stock_integrity(self, mouse):
        print(f"   [Step 1] Checking AI14 Stock Integrity for Mouse {mouse.id}...")
        
        if mouse.genotype == "Cre-:AI14+" and mouse.check_fluorescence("tail") == "RED":
            print("      ❌ CRITICAL FAILURE: AI14 Stock is compromised (Stop cassette lost).")
            return "DISCARD_COLONY"
        
        elif mouse.genotype == "Cre-:AI14+" and mouse.check_fluorescence("tail") == "BLACK":
            print("      ✅ PASS: AI14 Stock is clean.")
            return "PROCEED"
        
        return "N/A (Wrong Genotype)"

    def check_germline_excision(self, mouse):
        print(f"   [Step 2] Checking Germline Excision for Mouse {mouse.id}...")
        
        if mouse.genotype == "Cre+:AI14+" and mouse.check_fluorescence("tail") == "RED":
            print("      ⚠️ WARNING: Germline Excision Detected! (Whole body recombination).")
            return "BREEDING_ERROR"
        
        elif mouse.genotype == "Cre+:AI14+" and mouse.check_fluorescence("tail") == "BLACK":
            print("      ✅ PASS: Cre is specific. No germline leakage.")
            return "SUCCESS"

# --- 3. 执行脚本 (Execution) ---

if __name__ == "__main__":
    # 实例化 QC 系统
    qc_system = MouseModelQC()
    print("-" * 60)

    # === 场景 A: 噩梦 (全红) ===
    print("\n🧪 Running Diagnosis on: 'Suspicious Mouse A'...")
    bad_mouse = MockMouseSample(id="M001", genotype="Cre+:AI14+", tail_fluorescence="RED")
    qc_system.check_germline_excision(bad_mouse)

    # === 场景 B: 期望 (阴性对照) ===
    print("\n🧪 Running Diagnosis on: 'Control Mouse B'...")
    control_mouse = MockMouseSample(id="M002", genotype="Cre-:AI14+", tail_fluorescence="BLACK")
    qc_system.check_ai14_stock_integrity(control_mouse)
    
    # === 场景 C: 完美结果 ===
    print("\n🧪 Running Diagnosis on: 'Perfect Mouse C'...")
    good_mouse = MockMouseSample(id="M003", genotype="Cre+:AI14+", tail_fluorescence="BLACK")
    qc_system.check_germline_excision(good_mouse)

    print("\n" + "-" * 60)
    print("🎉 Done! Protocol execution complete. GitHub Green Square Earned!")
