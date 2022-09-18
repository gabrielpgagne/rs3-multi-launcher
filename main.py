import sys
import re
import os

# --- ENVIRONMENT AND USER CONFIG ---
USE_JAGEX_LAUNCHER = True # True or False
RS_CFG_PATH = "C:/ProgramData/Jagex/launcher"
JAGEX_LAUNCHER_PATH = "C:/Program Files (x86)/Jagex Launcher"

# -- SCRIPT START ---
lang = 0 
if(len(sys.argv) > 1):
    lang = sys.argv[1] # sys.argv[0] = name of script

with open(RS_CFG_PATH + "/preferences.cfg", 'r+', encoding = 'utf-8') as cfg:
    data = cfg.read()
    newCfg = re.sub("Language=[0-9]", f"Language={str(lang)}", data)
    cfg.seek(0,0)
    cfg.write(newCfg)

if(USE_JAGEX_LAUNCHER):
    os.startfile(JAGEX_LAUNCHER_PATH + "/JagexLauncher.exe")
else:
    os.startfile(RS_CFG_PATH + "/rs2client.exe")

print(f"Successfully started script with parameters:\n -Jagex launcher = {USE_JAGEX_LAUNCHER}\n -Language = {lang}")