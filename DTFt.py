import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
w=np.linspace(-np.pi,np.pi,1000)
x=[1,1,1,1]
l=len(x)
n=0
j=cm.sqrt(-1)
X_w=0
for n in range(l):
    X_w+=(x[n]*np.exp(-j*w*n))
plt.plot(w,X_w)
plt.show()
X_mgtd=np.abs(X_w)
X_phase=np.angle(X_w)
plt.subplot(211)
plt.plot(w,X_mgtd)
plt.title('Magnitude Spectrum')
plt.subplot(212)
plt.plot(w,X_phase)
plt.title('Phase Spectrum')
plt.show()
