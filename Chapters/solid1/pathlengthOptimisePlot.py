import ROOT
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update({'font.size': 13})
plt.rcParams['text.latex.unicode']=True

f = ROOT.TFile("pathlengthOptimisePlots.root")
g1 = f.Get("pathlengthResidual")
g2 = f.Get("pathlengthResidual_weighted")
g3 = f.Get("thinned")
fig = plt.figure(figsize = [11,8])

xs = []
ys1 = []
ys2 = []
ys3 = []

for i in range(1, g1.GetXaxis().GetNbins() + 1):
	xs.append(50*g1.GetXaxis().GetBinCenter(i))
	ys1.append(g1.GetBinContent(i))
	ys2.append(g2.GetBinContent(i))
	ys3.append(g3.GetBinContent(i))

lineWidth = 1.7
plt.subplot(121)
plt.step(xs, ys1, where='mid', lw = lineWidth, label = 'Raw', c='0.45')
plt.step(xs, ys2, where='mid', lw = lineWidth, label = 'Weights', c = 'k', alpha = 0.95)
plt.grid()
plt.xlim(-50*0.4, 50*0.4)
plt.ylim(0.0, 1.25*max(ys2))
plt.legend(loc = 'upper left', prop={'size':13})
#plt.step(xs, ys3, where='mid', lw = lineWidth, label = 'Weights and cuts', alpha = 0.9)
plt.ylabel("N")
plt.xlabel("Pathlength Residual (mm)")

plt.subplot(122)
plt.step(xs, ys2, where='mid', lw = lineWidth, label = 'Weights', c = 'k', alpha = 0.95)
plt.step(xs, ys3, where='mid', lw = lineWidth, label = 'Weights and cuts', c='0.45')
g3.Fit("gaus")

xsFit = np.linspace(5*xs[0], 5*xs[-1], 1000)
ysFit = []
for x in xsFit: ysFit.append(g3.GetFunction("gaus").Eval(x/50.))

plt.plot(xsFit, ysFit, ls = '--', c = 'k', lw = lineWidth, label = 'Gauss Fit')
# plt.semilogy()
plt.grid()
plt.xlim(-50*0.4, 50*0.4)
plt.ylim(0.0, 1.25*max(ys2))
plt.legend(loc = 'upper left', prop={'size':13})
plt.ylabel("N")
plt.xlabel("Pathlength Residual (mm)")
s = "$\sigma_{fit} = " + str(round(50*g3.GetFunction("gaus").GetParameter(2), 2)) + "\pm" + str(round(50*g3.GetFunction("gaus").GetParError(2), 2)) + " mm$"
plt.text(-10*1.85, 2050, s, fontsize = 16)

plt.subplots_adjust(left=0.08, right=0.97, top=0.95, bottom=0.08, wspace = 0.25, hspace = 0.06)
plt.savefig('pathlengthComparisons.pdf', format='pdf')
