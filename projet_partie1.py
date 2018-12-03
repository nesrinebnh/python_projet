import re,sys



#get the data from the page
#to extract "les substances actives" we must open the files from A to Z and apply the regulary expression
#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
#after getting the words we add .N+subst before to write them in the file

#file1 is the recipient file named "subst.dic" 
lenghtA,lenghtB,lenghtC,lenghtD,lenghtE,lenghtF,lenghtG,lenghtH,lenghtI,lenghtJ,lenghtK,lenghtL,lenghtM,lenghtN,lenghtO=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
lenghtP,lenghtQ,lenghtR,lenghtS,lenghtT,lenghtU,lenghtV,lenghtW,lenghtX,lenghtY,lenghtZ=0,0,0,0,0,0,0,0,0,0,0

file1 = open("subst.txt","a",encoding='utf-16-le')#recommended coding
file1.write('\ufeff')#bom

if sys.argv[1] == "B-H":
	fileB = open("vidal/vidal-Sommaires-Substances-B.txt","r")
	for i in fileB.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtB +=1
		else:
			''
		
	fileB.close()

	fileC = open("vidal/vidal-Sommaires-Substances-C.txt","r")
	for i in fileC.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		 
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtC+=1
		else:
			''
		
	fileC.close()


	fileD = open("vidal/vidal-Sommaires-Substances-D.txt","r")
	for i in fileD.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtD +=1
		else:
			''

	fileD.close()

	fileE = open("vidal/vidal-Sommaires-Substances-E.txt","r")
	for i in fileE.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtE +=1
		else:
			''

	fileE.close()

	fileF = open("vidal/vidal-Sommaires-Substances-F.txt","r")
	for i in fileF.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtF +=1
		else:
			''

	fileF.close()


	fileG = open("vidal/vidal-Sommaires-Substances-G.txt","r")
	for i in fileG.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtG +=1
		else:
			''

	fileG.close()

	fileH = open("vidal/vidal-Sommaires-Substances-H.txt","r")
	for i in fileH.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtH +=1
		else:
			''

	fileH.close()
elif sys.argv[1] == "E-S":
	fileE = open("vidal/vidal-Sommaires-Substances-E.txt","r")
	for i in fileE.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtE +=1
		else:
			''

	fileE.close()

	fileF = open("vidal/vidal-Sommaires-Substances-F.txt","r")
	for i in fileF.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtF +=1
		else:
			''

	fileF.close()


	fileG = open("vidal/vidal-Sommaires-Substances-G.txt","r")
	for i in fileG.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtG +=1
		else:
			''

	fileG.close()

	fileH = open("vidal/vidal-Sommaires-Substances-H.txt","r")
	for i in fileH.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtH +=1
		else:
			''

	fileH.close()

	fileI = open("vidal/vidal-Sommaires-Substances-I.txt","r")
	for i in fileI.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtI +=1
		else:
			''
	fileI.close()

	fileJ = open("vidal/vidal-Sommaires-Substances-J.txt","r")
	for i in fileJ.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtJ +=1
		else:
			''
	fileJ.close()

	fileK = open("vidal/vidal-Sommaires-Substances-K.txt","r")
	for i in fileK.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtK +=1
		else:
			''
	fileK.close()

	fileL = open("vidal/vidal-Sommaires-Substances-L.txt","r")
	for i in fileL.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtL +=1
		else:
			''
	fileL.close()

	fileM = open("vidal/vidal-Sommaires-Substances-M.txt","r")
	for i in fileM.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtM +=1
		else:
			''
	fileM.close()

	fileN = open("vidal/vidal-Sommaires-Substances-N.txt","r")
	for i in fileN.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtN +=1
		else:
			''
	fileN.close()

	fileO = open("vidal/vidal-Sommaires-Substances-O.txt","r")
	for i in fileO.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtO +=1
		else:
			''
	fileO.close()

	fileP = open("vidal/vidal-Sommaires-Substances-P.txt","r")
	for i in fileP.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtP +=1
		else:
			''
	fileP.close()

	fileQ = open("vidal/vidal-Sommaires-Substances-Q.txt","r")
	for i in fileQ.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtQ +=1
		else:
			''
	fileQ.close()

	fileR = open("vidal/vidal-Sommaires-Substances-R.txt","r")
	for i in fileR.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtR +=1
		else:
			''
	fileR.close()

	fileS = open("vidal/vidal-Sommaires-Substances-S.txt","r")
	for i in fileS.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtS +=1
		else:
			''
	fileS.close()	

elif sys.argv[1] == "A-W":
	#exract the words by opening the files
	#fileA will contain words which begins with a 
	fileA = open("vidal/vidal-Sommaires-Substances-A.txt","r")
	#extract words
	for i in fileA.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+ \w*|-?\w*-?\w*-?\w*| \w*-?\(?\w*\)?| \w* \w* \( \w*\))</a>
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtA +=1
		else:
			''
	fileA.close()


	fileB = open("vidal/vidal-Sommaires-Substances-B.txt","r")
	for i in fileB.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
		#(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtB +=1
		else:
			''
		
	fileB.close()

	fileC = open("vidal/vidal-Sommaires-Substances-C.txt","r")
	for i in fileC.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		 
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtC+=1
		else:
			''
		
	fileC.close()


	fileD = open("vidal/vidal-Sommaires-Substances-D.txt","r")
	for i in fileD.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtD +=1
		else:
			''

	fileD.close()

	fileE = open("vidal/vidal-Sommaires-Substances-E.txt","r")
	for i in fileE.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtE +=1
		else:
			''

	fileE.close()

	fileF = open("vidal/vidal-Sommaires-Substances-F.txt","r")
	for i in fileF.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtF +=1
		else:
			''

	fileF.close()


	fileG = open("vidal/vidal-Sommaires-Substances-G.txt","r")
	for i in fileG.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtG +=1
		else:
			''

	fileG.close()

	fileH = open("vidal/vidal-Sommaires-Substances-H.txt","r")
	for i in fileH.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtH +=1
		else:
			''

	fileH.close()

	fileI = open("vidal/vidal-Sommaires-Substances-I.txt","r")
	for i in fileI.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtI +=1
		else:
			''
	fileI.close()

	fileJ = open("vidal/vidal-Sommaires-Substances-J.txt","r")
	for i in fileJ.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtJ +=1
		else:
			''
	fileJ.close()

	fileK = open("vidal/vidal-Sommaires-Substances-K.txt","r")
	for i in fileK.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtK +=1
		else:
			''
	fileK.close()

	fileL = open("vidal/vidal-Sommaires-Substances-L.txt","r")
	for i in fileL.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtL +=1
		else:
			''
	fileL.close()

	fileM = open("vidal/vidal-Sommaires-Substances-M.txt","r")
	for i in fileM.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtM +=1
		else:
			''
	fileM.close()

	fileN = open("vidal/vidal-Sommaires-Substances-N.txt","r")
	for i in fileN.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtN +=1
		else:
			''
	fileN.close()

	fileO = open("vidal/vidal-Sommaires-Substances-O.txt","r")
	for i in fileO.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtO +=1
		else:
			''
	fileO.close()

	fileP = open("vidal/vidal-Sommaires-Substances-P.txt","r")
	for i in fileP.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtP +=1
		else:
			''
	fileP.close()

	fileQ = open("vidal/vidal-Sommaires-Substances-Q.txt","r")
	for i in fileQ.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtQ +=1
		else:
			''
	fileQ.close()

	fileR = open("vidal/vidal-Sommaires-Substances-R.txt","r")
	for i in fileR.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtR +=1
		else:
			''
	fileR.close()

	fileS = open("vidal/vidal-Sommaires-Substances-S.txt","r")
	for i in fileS.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtS +=1
		else:
			''
	fileS.close()	

	fileT = open("vidal/vidal-Sommaires-Substances-T.txt","r")
	for i in fileT.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtT +=1
		else:
			''
	fileT.close()

	fileU = open("vidal/vidal-Sommaires-Substances-U.txt","r")
	for i in fileU.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtU +=1
		else:
			''
	fileU.close()

	fileV = open("vidal/vidal-Sommaires-Substances-V.txt","r")
	for i in fileV.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtV +=1
		else:
			''
	fileV.close()

	fileW = open("vidal/vidal-Sommaires-Substances-W.txt","r")
	for i in fileW.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtW +=1
		else:
			''
	fileW.close()

	fileX = open("vidal/vidal-Sommaires-Substances-X.txt","r")
	for i in fileX.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtX +=1
		else:
			''
	fileX.close()

	fileY = open("vidal/vidal-Sommaires-Substances-Y.txt","r")
	for i in fileY.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtY +=1
		else:
			''
	fileY.close()

	fileZ = open("vidal/vidal-Sommaires-Substances-Z.txt","r")
	for i in fileZ.readlines():
		x=re.search("(.*<a href=\"\w+/?\w+-\d+.*\">)(\w+( \()?([-| |\(| \')]?\w*)*\)?)</a>",i,re.I)
		if x:
			file1.write(x.group(2)+',.N+subst'+'\n')
			lenghtZ +=1
		else:
			''
	fileZ.close()

else:
	print("ERROR, page not found\n");

file1.close()

lenght = lenghtA+lenghtB+lenghtC+lenghtD+lenghtE+lenghtF+lenghtG+lenghtH+lenghtI+lenghtJ+lenghtK+lenghtL+lenghtM+lenghtN+lenghtO+lenghtP+lenghtQ+lenghtR+lenghtS+lenghtT+lenghtU+lenghtV+lenghtW+lenghtX+lenghtY+lenghtZ
file2 = open("info.txt","a",encoding='utf-16-le')
file2.write("\ufeff")
file2.write("total = "+str(lenght)+"\n");
file2.write("les substance A actives =  "+str(lenghtA)+"\n")
file2.write("les substance B actives =  "+str(lenghtB)+"\n")
file2.write("les substance C actives =  "+str(lenghtC)+"\n")
file2.write("les substance D actives =  "+str(lenghtD)+"\n")
file2.write("les substance E actives =  "+str(lenghtE)+"\n")
file2.write("les substance F actives =  "+str(lenghtF)+"\n")
file2.write("les substance G actives =  "+str(lenghtG)+"\n")
file2.write("les substance H actives =  "+str(lenghtH)+"\n")
file2.write("les substance I actives =  "+str(lenghtI)+"\n")
file2.write("les substance J actives =  "+str(lenghtJ)+"\n")
file2.write("les substance K actives =  "+str(lenghtK)+"\n")
file2.write("les substance L actives =  "+str(lenghtL)+"\n")
file2.write("les substance M actives =  "+str(lenghtM)+"\n")
file2.write("les substance N actives =  "+str(lenghtN)+"\n")
file2.write("les substance O actives =  "+str(lenghtO)+"\n")
file2.write("les substance P actives =  "+str(lenghtP)+"\n")
file2.write("les substance Q actives =  "+str(lenghtQ)+"\n")
file2.write("les substance R actives =  "+str(lenghtR)+"\n")
file2.write("les substance S actives =  "+str(lenghtS)+"\n")
file2.write("les substance T actives =  "+str(lenghtT)+"\n")
file2.write("les substance U actives =  "+str(lenghtU)+"\n")
file2.write("les substance V actives =  "+str(lenghtV)+"\n")
file2.write("les substance W actives =  "+str(lenghtW)+"\n")
file2.write("les substance X actives =  "+str(lenghtX)+"\n")
file2.write("les substance Y actives =  "+str(lenghtY)+"\n")
file2.write("les substance Z actives =  "+str(lenghtZ)+"\n")

file2.close()
