import matplotlib.pyplot as plt
import ROOT
import numpy as np
from matplotlib.font_manager import FontProperties 
fontP = FontProperties()
fontP.set_size('13')


xs = []
ys1 = []
ys2 = []

plt.figure(figsize = [6,8])
f = ROOT.TFile("Saffron-histos.root", "READ")
g1 = f.Get("SafRawPlots/WaveformSamples/Glib0/WaveformSamples3-0")
g2 = f.Get("SafNeutronId/neutronHorNum:1-Glib:4")
linew = 1.5

for i in range(1, 180):
	xs.append(16*g1.GetXaxis().GetBinCenter(i))
	ys1.append(g1.GetBinContent(i+10))
	ys2.append(g2.GetBinContent(i))

ax = plt.subplot(211)
ax.step(xs, ys1, color = 'k', lw = linew)
plt.grid()
plt.xlabel("Time (ns)")
plt.ylabel("Charge (ADC)")

ax2 = plt.subplot(212)
ax2.step(xs, ys2, color = 'k', lw = linew)

plt.grid()

plt.xlabel("Time (ns)")
plt.ylabel("Charge (ADC)")
# plt.show()
plt.savefig('sm1_waveform_kinds.pdf', format='pdf')
