# COMP01 part 01: re-render of ep01_rome for the compilation (short rest instead of the 12-min tail; part 3 keeps the long tail)
import importlib.util as _u, os as _os
_s = _u.spec_from_file_location("_src", _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "ep01_rome.py"))
_m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
globals().update({k: v for k, v in vars(_m).items() if k.isupper()})
TAIL_MIN = 0.5
