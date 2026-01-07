#experimentprotocol  
# genotyping protocol


---

## **Day1 — DNA Extraction (lysis / tissue lysis)**

1. get samples:(keep the labels of samples untill we got the results of this genotyping)
    
2. get **PBND buffer** and **enzyme (proteinase K)**
    
3. calculate: each sample needs **PBND buffer 150 uL** and **enzyme 3 uL**
    
    - usually we prepare more.
        
    - such as: if we have **43 samples**, we can prepare for **50**
        
        - which is => buffer: **150 uL × 50 = 7500 uL = 7.5 mL**
            
        - enzyme: **3 uL × 50 = 150 uL**
            
    
    then use the big pipette to add buffer  
    → we can use the **“10 mL” cube**
    
    use **200 uL pipetter** (switch to **150 uL**) to add enemy
    
    → add this two into a cube
    → then shake it to mix.  
    → then add **150 uL** of the mixture to each sample
    
    - (remember to **change the tips everytime**)
        
    - (also remember to use the tips with **filter**)
        
    - (all experiment with DNA/RNA need, so genotyping is always using this)
        
4. incubate overnight  
    **5\65°C - 150 rpm**  
    → proteinase K (**the best temperature for it**)
    

---

## **Day2** 

**备注：DreamTaq Green PCR buffer.**

- 里面含有蓝色染料（loading dye）和密度试剂（比如甘油）
    
- PS：不可用于做 real-time PCR (qPCR)，或者downstream的酶切/克隆反应
    → 因为里面的染料可能会干扰荧光信号或其他酶活性
    

1. **95°C, 15 min** High temperature incubation
    
    - to denature proteins
        
    - inactivate proteinase K 
        → finalizes the DNA extraction.
2. centrifugation (**13000 rpm 10 min**)
    
    - supernatant (contains DNA) → **100 uL**
        
    - add to new/fresh tube (lids → tight)
        
    - (and make sure all tubes were mark by the sample ID)
        
    - tube body：DB编号后四位
        
    - lids：名称简写和耳号
        
3. prepare PCR mixture  
    we need samples and controls.
    
    - for samples → 实际有多少
        
    - for controls → **water → always needed**
        
        - others → 阳性纯合子 杂合子
            
    
    if we have **7 samples**, **2 controls + 1 water**, in total we have **10 tubes**,  
    but we can prepare for **14~15 tubes** (prepare more will be better)
    
    - **2 uL** DNA / control / water (individual target)
        
    - **11.9 uL H2O** → 不定量，取决于下面的试剂的多少，用 H2O 补平
        
    - **2.0 uL 10× DreamTaq® Green Buffer**
        
    - **2.0 uL dNTPs (2 mM each)**
        
    - **2.0 uL primer** 
        
    - **0.1 uL DreamTaq Polymerase**
        
    - → **20.0 uL vol.** → in total (each tube)
        
    
    先加 **2 uL DNA** 或者对照 control 到 **PCR strip tubes**（条状管：一排放 8 个孔）
    再加 **18 uL mixture** to 每个 PCR strip tubes  
    → **每孔 20 uL**
    
4. set up PCR machine → overnight.
    

---

## **Day3** 

### 1. Gel casting

① **2% agarose powder** (**2 g for 100 mL**) → **大烧杯 (500 mL)**  
② **1× TBE buffer** (**100 mL**)  
③ mix them and heat until fully melted. (**microwave. 3 min**)
- dangerous → glove
④ add H2O to **100 mL total** (compensate evaporation).  
⑤ add **5 uL midori Green dye** (to bind the DNA) 
→ always careful about this  
⑥ Gently swirl to mix (avoid the bubble)  
⑦ Pour the solution into a gel casting tray / gel mold.  
⑧ insert a comb to create wells.  
⑨ let sit **20–30 min** to solidify.
(wash the beaker in the fume hood because midori)  
(pour the washed waste liquid into the wash liquid bin in the fume hood.)  
(then put the beaker in the right side shelf)


### 2. Sample loading & Electrophoresis

① Place the gel into the electrophoresis tank/chamber.  
② Add **1× TBE buffer** to submerge the gel  
③ load **5 uL MassRuler Low Range DNA ladder**
- 5 uL 或 6 uL 都可，**6 uL 只是多一点浓度**
- 每排25个孔，第一个孔 always 是 ladder  
④ Load PCR products into wells (**5–==10== uL**)  
⑤ Run at (**100–120 V**) for **45–60 min** (**120 volt, 50 min**)

**Ladder 的作用**

1. 比对 DNA 片段大小。  
    每一条 ladder 的条带代表一个特定大小的 DNA 片段  
    可通过对照 ladder 判断 PCR 产物的大小是否在预期。
    
2. 判断对错/成功与否。  
    没有 ladder，就不清楚条带到底是啥/对应啥。
    
3. 判断电泳效果是否均匀。  
    若 ladder 也跑得歪弥散扭曲，说明电泳不稳定，  
    如：速度过快。
    

---

## **3. Gel imaging & Band observation Procedure** 

设备：**Bio-Rad / Imager System**

① Insert USB flash drive or memory card for image storage.  
② Open the imaging chamber and carefully place the gel on the center tray  
③ Press the “live” button to activate real-time camera view  
④ Adjust the gel position to center the bands on the screen  
⑤ Close the chamber lid completely  
⑥ Turn on the UV light by pressing the UV button (turn off the white light)  
⑦ Observe the bands’ location, clarity, and size  
⑧ Click “save” or “capture” to save the image to USB or drive memory  
⑨ Switch to white light if needed for another view and repeat capture.

**Tips:**

- Place gel face-up with consistent orientation.
    
- Avoid overexposure or underexposure during image capture.
    
- Always back up images to a PC after capture.
    
- For Midori Green, blue light is safer than UV.
    
- If ladder bands are unclear, check electrophoresis conditions.
    

条带：100与200难以辨认，自下往上是100~1000，每次做的条带是多少看protocol
