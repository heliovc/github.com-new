import sys, json, importlib.util
sys.path.insert(0, '.')
import render as R
spec=importlib.util.spec_from_file_location('e',sys.argv[1]); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
durs=json.load(open(sys.argv[2]+'/durs.json')); R.init(); t=0.0; n=0
while t < sum(durs):
    R.frame(m.SCENES,durs,t); t+=0.4; n+=1
print('scan ok', n)
