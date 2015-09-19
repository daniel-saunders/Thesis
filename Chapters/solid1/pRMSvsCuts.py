import ROOT
import matplotlib.pyplot as plt
fig = plt.figure(figsize = [11,5.5])
f = ROOT.TFile("safSimHistos.root")
plt.rc('xtick', labelsize=12) 
plt.rc('ytick', labelsize=12) 
plt.rcParams.update({'font.size': 12})
xs = []
ys0 = []
ys1 = []
ys2 = []
ys3 = []

ys0N = []
ys1N = []
ys2N = []
ys3N = []

ys0Ndiv = []
ys1Ndiv = []
ys2Ndiv = []
ys3Ndiv = []

g0 = f.Get("SafSimComparison/pathlengthResidualVsSizeCuts0")
g1 = f.Get("SafSimComparison/pathlengthResidualVsSizeCuts1")
g2 = f.Get("SafSimComparison/pathlengthResidualVsSizeCuts2")
g3 = f.Get("SafSimComparison/pathlengthResidualVsSizeCuts3")

nBins = g0.GetXaxis().GetNbins()
for i in range(3, 8):
	xs.append(g0.GetXaxis().GetBinCenter(i))
	ys0.append(500*g0.ProjectionY("temp", i, nBins).GetRMS())
	ys1.append(500*g1.ProjectionY("temp", i, nBins).GetRMS())
	ys2.append(500*g2.ProjectionY("temp", i, nBins).GetRMS())
	ys3.append(500*g3.ProjectionY("temp", i, nBins).GetRMS())

	ys0N.append(g0.ProjectionY("temp", i, nBins).GetEntries())
	ys1N.append(g1.ProjectionY("temp", i, nBins).GetEntries())
	ys2N.append(g2.ProjectionY("temp", i, nBins).GetEntries())
	ys3N.append(g3.ProjectionY("temp", i, nBins).GetEntries())

	ys0Ndiv.append(ys0N[-1]/ys0[-1])
	ys1Ndiv.append(ys1N[-1]/ys1[-1])
	ys2Ndiv.append(ys2N[-1]/ys2[-1])
	ys3Ndiv.append(ys3N[-1]/ys3[-1])



plt.subplot(131)
lineWidth = 1.5
plt.plot(xs, ys0, '-o', lw = lineWidth, label = "$\Delta r_{max} < 250mm$")
plt.plot(xs, ys1, '-v', lw = lineWidth, label = "$\Delta r_{max} < 300mm$")
plt.plot(xs, ys2, '-^', lw = lineWidth, label = "$\Delta r_{max} < 350mm$")
plt.plot(xs, ys3, '-s', lw = lineWidth, c = 'k', label = "$\Delta r_{max} < 400mm$")
plt.xlim([4.5, 13.5])
plt.ylim(5, 105)
plt.grid()
plt.ylabel("Pathlength residual RMS (mm)")
plt.xlabel("Cluster lower size cut")
plt.legend(loc = 'upper right')

plt.subplot(132)
lineWidth = 1.5
plt.plot(xs, ys0N, '-o', lw = lineWidth)
plt.plot(xs, ys1N, '-v', lw = lineWidth)
plt.plot(xs, ys2N, '-^', lw = lineWidth)
plt.plot(xs, ys3N, '-s', lw = lineWidth, c = 'k')
plt.xlim([4.5, 13.5])
plt.grid()
plt.ylabel("N")
plt.xlabel("Cluster lower size cut")


plt.subplot(133)
lineWidth = 1.5
plt.plot(xs, ys0Ndiv, '-o', lw = lineWidth)
plt.plot(xs, ys1Ndiv, '-v', lw = lineWidth)
plt.plot(xs, ys2Ndiv, '-^', lw = lineWidth)
plt.plot(xs, ys3Ndiv, '-s', lw = lineWidth, c = 'k')
plt.xlim([4.5, 13.5])
plt.grid()
plt.ylabel("N/Pathlength residual RMS (/mm)")
plt.xlabel("Cluster lower size cut")


plt.subplots_adjust(left=0.07, right=0.99, top=0.95, bottom=0.13, wspace = 0.31, hspace = 0.06)
# plt.show()	
plt.savefig('pathlengthCutScans.pdf', format='pdf')
