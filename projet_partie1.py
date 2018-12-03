import re



#get the data from the page
#to extract "les substances actives" we must open the files from A to Z and apply the regulary expression
#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
#after getting the words we add .N+subst before to write them in the file

#file1 is the recipient file named "subst.dic" 
file1 = open("subst.txt","a",encoding='utf-16-le')#recommended coding
file1.write('\ufeff')#bom

#exract the words by opening the files
#fileA will contain words which begins with a 
fileA = open("vidal/vidal-Sommaires-Substances-A.txt","r")
#extract words
for i in fileA.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+ \w*|-?\w*-?\w*-?\w*| \w*-?\(?\w*\)?| \w* \w* \( \w*\))</a>
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileA.close()


fileB = open("vidal/vidal-Sommaires-Substances-B.txt","r")
for i in fileB.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
	#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
	#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileB.close()

fileC = open("vidal/vidal-Sommaires-Substances-C.txt","r")
for i in fileC.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileC.close()


fileD = open("vidal/vidal-Sommaires-Substances-D.txt","r")
for i in fileD.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileD.close()

fileE = open("vidal/vidal-Sommaires-Substances-E.txt","r")
for i in fileE.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileE.close()

fileF = open("vidal/vidal-Sommaires-Substances-F.txt","r")
for i in fileF.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileF.close()


fileG = open("vidal/vidal-Sommaires-Substances-G.txt","r")
for i in fileG.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileG.close()

fileH = open("vidal/vidal-Sommaires-Substances-H.txt","r")
for i in fileH.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileH.close()

fileI = open("vidal/vidal-Sommaires-Substances-I.txt","r")
for i in fileI.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileI.close()

fileJ = open("vidal/vidal-Sommaires-Substances-J.txt","r")
for i in fileJ.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileJ.close()

fileK = open("vidal/vidal-Sommaires-Substances-K.txt","r")
for i in fileK.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileK.close()

fileL = open("vidal/vidal-Sommaires-Substances-L.txt","r")
for i in fileL.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileL.close()

fileM = open("vidal/vidal-Sommaires-Substances-M.txt","r")
for i in fileM.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileM.close()

fileN = open("vidal/vidal-Sommaires-Substances-N.txt","r")
for i in fileN.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileN.close()

fileO = open("vidal/vidal-Sommaires-Substances-O.txt","r")
for i in fileO.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileO.close()

fileP = open("vidal/vidal-Sommaires-Substances-P.txt","r")
for i in fileP.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileP.close()

fileQ = open("vidal/vidal-Sommaires-Substances-Q.txt","r")
for i in fileQ.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileQ.close()

fileR = open("vidal/vidal-Sommaires-Substances-R.txt","r")
for i in fileR.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileR.close()

fileS = open("vidal/vidal-Sommaires-Substances-S.txt","r")
for i in fileS.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileS.close()	

fileT = open("vidal/vidal-Sommaires-Substances-T.txt","r")
for i in fileT.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileT.close()

fileU = open("vidal/vidal-Sommaires-Substances-U.txt","r")
for i in fileU.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileU.close()

fileV = open("vidal/vidal-Sommaires-Substances-V.txt","r")
for i in fileV.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileV.close()

fileW = open("vidal/vidal-Sommaires-Substances-W.txt","r")
for i in fileW.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileW.close()

fileX = open("vidal/vidal-Sommaires-Substances-X.txt","r")
for i in fileX.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileX.close()

fileY = open("vidal/vidal-Sommaires-Substances-Y.txt","r")
for i in fileY.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileY.close()

fileZ = open("vidal/vidal-Sommaires-Substances-Z.txt","r")
for i in fileZ.readlines():
	x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
	file1.write(x.group(2)+',.N+subst'+'\n') if x else ''
fileZ.close()

file1.close()