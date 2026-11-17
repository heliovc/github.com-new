# Writes the final file of each "vsc" scene (as produced by the edit engine) and runs it for real; output -> transcript.txt
import os, sys, subprocess, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE)) if os.path.basename(os.path.dirname(HERE)) == "demo" else HERE
sp = importlib.util.spec_from_file_location("ep", sys.argv[1]); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
W = os.path.join(HERE, "shortcuts"); os.makedirs(W, exist_ok=True)
files = {"cart2": ("cart.py", m.CART2), "cart3": ("cart.py", m.CART3), "list": ("list.py", m.vsc_final(m.V_LIST)), "report2": ("report.py", m.vsc_final(m.V_F2))}
out = []
for key, (fn, code) in files.items():
    open(os.path.join(W, f"{key}_{fn}"), "w").write(code); open(os.path.join(W, fn), "w").write(code)
    r = subprocess.run([sys.executable, fn], cwd=W, capture_output=True, text=True)
    out.append(f"### {key}\n$ python3 {fn}\n" + r.stdout + r.stderr)
open(os.path.join(HERE, "transcript.txt"), "w").write("".join(out)); print("".join(out))
