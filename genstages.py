# make -C stage1 FW=1100 clean && make -C stage1 FW=1100
import os
fw = [900, 903, 904, 950, 960, 1000, 1001, 1050, 1070, 1071, 1100]
print("This requires WSL on Windows")
print("Beginning stage 1")
for f in fw:
    print(f"FW: {f}")
    os.system(f"make -C stage1 FW={f} clean && make -C stage1 FW={f}")
print("Beginning stage 2")
for f in fw:
    print(f"FW: {f}")
    os.system(f"make -C stage2 FW={f} clean && make -C stage2 FW={f}")
print("Finished!")