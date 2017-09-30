import numpy as np
import pylab
import re
import matplotlib.pyplot as plt

#Open file - get line count
flares = open("flares.txt")
fcount = 0
for line in flares:
	fcount = fcount + 1
flares.close()
#Data lists
flaredata = []
#Modified Zurich class
zca = [0] * fcount
zcb = [0] * fcount
zcc = [0] * fcount
zcd = [0] * fcount
zce = [0] * fcount
zcf = [0] * fcount
zch = [0] * fcount
flaredata.append(zca)
flaredata.append(zcb)
flaredata.append(zcc)
flaredata.append(zcd)
flaredata.append(zce)
flaredata.append(zcf)
flaredata.append(zch)
#Largest spot size
lssx = [0] * fcount
lssr = [0] * fcount
lsss = [0] * fcount
lssa = [0] * fcount
lssh = [0] * fcount
lssk = [0] * fcount
flaredata.append(lssx)
flaredata.append(lssr)
flaredata.append(lsss)
flaredata.append(lssa)
flaredata.append(lssh)
flaredata.append(lssk)
#Spot distribution
sdx = [0] * fcount
sdo = [0] * fcount
sdi = [0] * fcount
sdc = [0] * fcount
flaredata.append(sdx)
flaredata.append(sdo)
flaredata.append(sdi)
flaredata.append(sdc)
#Activity - 0=reduced, 1=unchanged
activity = [0] * fcount
flaredata.append(activity)
#Evolution
evod = [0] * fcount
evon = [0] * fcount
evog = [0] * fcount
flaredata.append(evod)
flaredata.append(evon)
flaredata.append(evog)
#Previous 24hr flare activity
pfacm1 = [0] * fcount
pfacm2 = [0] * fcount
pfacm3 = [0] * fcount
flaredata.append(pfacm1)
flaredata.append(pfacm2)
flaredata.append(pfacm3)
#Historically complex
histcomp = [0] * fcount
flaredata.append(histcomp)
#Did region become historically complex on this pass across the sun's disk? 0=no, 1=yes
bhcop = [0] * fcount
flaredata.append(bhcop)
#Area, 0=small, 1=large
flarearea = [0] * fcount
flaredata.append(flarearea)
#Area of largest spot, 0=(<=5) 1=(>5)
lspots = [0] * fcount
flaredata.append(lspots)

#Result set - flare count
flarecount = [0] * fcount
flaredata.append(flarecount)
#29 lists total, 28 without result set

#Populate data
flares = open("flares.txt")
findex = 0
for line in flares:
	thisflare = re.split("\s+", line)
	#Zurich class
	if thisflare[0] == "A":
		zca[findex] = 1
	elif thisflare[0] == "B":
		zcb[findex] = 1
	elif thisflare[0] == "C":
		zcc[findex] = 1
	elif thisflare[0] == "D":
		zcd[findex] = 1
	elif thisflare[0] == "E":
		zce[findex] = 1
	elif thisflare[0] == "F":
		zcf[findex] = 1
	elif thisflare[0] == "H":
		zch[findex] = 1
    #Spot size
	if thisflare[1] == "X":
		lssx[findex] = 1
	elif thisflare[1] == "R":
		lssr[findex] = 1
	elif thisflare[1] == "S":
		lsss[findex] = 1
	elif thisflare[1] == "A":
		lssa[findex] = 1
	elif thisflare[1] == "H":
		lssh[findex] = 1
	elif thisflare[1] == "K":
		lssk[findex] = 1
    #Spot distribution
	if thisflare[2] == "X":
		sdx[findex] = 1
	elif thisflare[2] == "O":
		sdo[findex] = 1
	elif thisflare[2] == "I":
		sdi[findex] = 1
	elif thisflare[2] == "C":
		sdc[findex] = 1
    #Activity
	if thisflare[3] == "2":
		activity[findex] = 1
    #Evolution
	if thisflare[4] == "1":
		evod[findex] = 1
	elif thisflare[4] == "2":
		evon[findex] = 1
	elif thisflare[4] == "3":
		evog[findex] = 1
    #Previous activity
	if thisflare[5] == "1":
		pfacm1[findex] = 1
	elif thisflare[5] == "2":
		pfacm2[findex] = 1
	elif thisflare[5] == "3":
		pfacm3[findex] = 1
	#Historically complex
	if thisflare[6] == "2":
		histcomp[findex] = 1
    #Became historically complex?
	if thisflare[7] == "2":
		bhcop[findex] = 1
    #Area
	if thisflare[8] == "2":
		flarearea[findex] = 1
    #Largest spot
	if thisflare[9] == "2":
		lspots[findex] = 1
	#Results
	if int(thisflare[10]) > 0:
		flarecount[findex] = flarecount[findex] + int(thisflare[9])
	if int(thisflare[11]) > 0:
		flarecount[findex] = flarecount[findex] + int(thisflare[10])
	if int(thisflare[12]) > 0:
		flarecount[findex] = flarecount[findex] + int(thisflare[11])
	#Iterate counter
	findex = findex + 1
flares.close()

#x_range = np.arange(8)
#y_range = (0,5,10,15,20,25,30,35)
#plt.bar(x_range, y_range, align="center", alpha=0.5)
#plt.show()

#Get count
def getCount(li):
	c = 0
	for i in li:
		if i == 1:
			c = c + 1
	return c
#Plot Zurich class
zyax = [getCount(zca), getCount(zcb), getCount(zcc), getCount(zcd), getCount(zce), getCount(zcf), getCount(zch)]
zxax = np.arange(7)
plt.bar(zxax, zyax, align="center", alpha=0.5)
plt.title("Zurich Class Frequencies")
plt.xticks(zxax, ("A", "B", "C", "D", "E", "F", "H"))
#plt.show()

#Plot Largest Spot Size
plt.cla()
lsyax = [getCount(lssx), getCount(lssr), getCount(lsss), getCount(lssa), getCount(lssh), getCount(lssk)]
lsxax = np.arange(7)
plt.bar(zxax, zyax, align="center", alpha=0.5)
plt.title("Largest Spot Size")
plt.xticks(zxax, ("X", "R", "S", "A", "H", "K"))
#plt.show()

#Plot Spot Distribution
plt.cla()
sdyax = [getCount(sdx), getCount(sdo), getCount(sdi), getCount(sdc)]
sdxax = np.arange(4)
plt.bar(sdxax, sdyax, align="center", alpha=0.5)
plt.title("Spot Distribution Class")
plt.xticks(sdxax, ("X", "O", "I", "C"))
#plt.show()

#Plot Activity
plt.cla()
actyax = [getCount(activity), (1066 - getCount(activity))]
actxax = np.arange(2)
plt.bar(actxax, actyax, align="center", alpha=0.5)
plt.title("Activity")
plt.xticks(actxax, ("Activity", "No Activity"))
#plt.show()

#Plot Evolution
plt.cla()
evoyax = [getCount(evod), getCount(evon), getCount(evog)]
evoxax = np.arange(3)
plt.bar(evoxax, evoyax, align="center", alpha=0.5)
plt.title("Evolution")
plt.xticks(evoxax, ("Decay", "No Growth", "Growth"))
#plt.show()

#Plot Previous 24-hr Flare Activity Code
plt.cla()
pfacyax = [getCount(pfacm1), getCount(pfacm2), getCount(pfacm3)]
pfacxax = np.arange(3)
plt.bar(pfacxax, pfacyax, align="center", alpha=0.5)
plt.title("Previous 24-hr Flare Activity Code")
plt.xticks(pfacxax, ("Nothing as big as an M1", "One M1", "More activity than one M1"))
#plt.show()

#Plot Historically Complex
plt.cla()
hcyax = [getCount(histcomp), (1066 - getCount(histcomp))]
hcxax = np.arange(2)
plt.bar(hcxax, hcyax, align="center", alpha=0.5)
plt.title("Historically Complex")
plt.xticks(hcxax, ("Yes", "No"))
#plt.show()

#Plot Became Historically Complex
plt.cla()
bhyax = [getCount(bhcop), (1066 - getCount(bhcop))]
bhxax = np.arange(2)
plt.bar(bhxax, bhyax, align="center", alpha=0.5)
plt.title("Did area become historically complex on this pass?")
plt.xticks(bhxax, ("Yes", "No"))
#plt.show()

#Plot Area
plt.cla()
aryax = [getCount(flarearea), (1066 - getCount(flarearea))]
arxax = np.arange(2)
plt.bar(arxax, aryax, align="center", alpha=0.5)
plt.title("Area")
plt.xticks(arxax, ("Small", "Large"))
#plt.show()

#Plot Largest Spot Area - deprecated as everything is <=5
#plt.cla()
#spyax = [getCount(lspots), (1066 - getCount(lspots))]
#spxax = np.arange(2)
#plt.bar(spxax, spyax, align="center", alpha=0.5)
#plt.title("Area of Largest Spot")
#plt.xticks(spxax, ("<=5", ">5"))
#plt.show()
#print(lspots)
