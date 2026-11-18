# flat LambdaCDM, Planck 2018 (TT,TE,EE+lowE+lensing+BAO): H0 67.66, Om 0.3111, radiation ~9.1e-5
import numpy as np
H0 = 67.66; Om = 0.3111; Or = 9.1e-5; OL = 1 - Om - Or
C = 299792.458; MPC_GLY = 3.26156e-3
HUB_GYR = 977.8 / H0  # 1/H0 in Gyr
def E(a): return np.sqrt(Or / a**4 + Om / a**3 + OL)
_a = np.logspace(-9, 1.2, 200001)
_dt = 1 / (_a * E(_a))       # dt/da * H0
_dc = 1 / (_a**2 * E(_a))    # dchi/da * H0/c
def _cum(f):
    out = np.zeros_like(_a); out[1:] = np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(_a)); return out
T = _cum(_dt) * HUB_GYR       # age at a (Gyr)
X = _cum(_dc) * HUB_GYR       # conformal "distance" from a=0 (Gly) = c*integral dt/a
def age(z): return np.interp(1 / (1 + z), _a, T)
AGE = age(0.0)
X0 = np.interp(1.0, _a, X)
def chi(z): return X0 - np.interp(1 / (1 + z), _a, X)          # comoving distance now (Gly)
def d_then(z): return chi(z) / (1 + z)                           # proper distance at emission (Gly)
def lookback(z): return AGE - age(z)
XINF = X[-1] + HUB_GYR / np.sqrt(OL) / _a[-1]
EVENT = XINF - X0  # comoving event horizon now (approx)
if __name__ == "__main__":
    print("age", AGE, "particle horizon", X0, "event horizon", EVENT, "hubble radius", C / H0 * MPC_GLY)
    zs = np.linspace(0.01, 6, 6000); dt = d_then(zs); i = dt.argmax(); print("max emission dist", dt[i], "at z", zs[i], "lookback", lookback(zs[i]))
    for z in [0.1, 0.5, 1, 1.6, 3, 6, 10, 14.44, 20, 1089.8]:
        print(z, "lookback %.3f age %.4f Gyr  then %.3f now %.2f Gly" % (lookback(z), age(z), d_then(z), chi(z)))
    # angular size of 100,000 ly galaxy (arcsec)
    for z in [0.1, 0.5, 1, 1.6, 3, 10, 14.44]:
        print("ang", z, 1e-4 / d_then(z) * 206265, "arcsec; dimming (1+z)^4 =", (1 + z) ** 4)
