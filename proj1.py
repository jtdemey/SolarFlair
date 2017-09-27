import numpy as np
import pylab
import re

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
testcount = 0
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
	testcount = testcount + 1
print(testcount)

#Test by printing lists
#fcindex = 0
#for i in flarecount:
#	print(i)
flares.close()
counts = [0] * 29
cindex = 0
for data in flaredata:
	for i in data:
		if i == 1:
			counts[cindex] = counts[cindex] + 1
	cindex = cindex + 1
print(counts)
cindex = 0
for i in counts:
	print(i / 1066)

