import sys
import random
random.seed(51800408);

#Create Latin Square
def CreateBlock(n):
	B=[]
	for i in range(n):
		B.append(random.sample(range(n),n))
	while(B[0][0]==B[1][0] or B[0][0]==B[2][0] or B[1][0]==B[2][0] or B[0][1]==B[2][1] or B[0][1]==B[1][1] or B[0][2]==B[2][2] or B[0][2]==B[1][2] or B[2][2]==B[1][2]):
		B[0]=random.sample(range(n),n)
		B[1]=random.sample(range(n),n)
		B[2]=random.sample(range(n),n)
	return B

base=3;
Block1=CreateBlock(base)
Block2=CreateBlock(base)
Block3=CreateBlock(base)
Block4=CreateBlock(base)
Block5=CreateBlock(base)
Block6=CreateBlock(base)
Block7=CreateBlock(base)
Block8=CreateBlock(base)
Block9=CreateBlock(base)
LatinSquare=[Block1,Block2,Block3,Block4,Block5,Block6,Block7,Block8,Block9]
pos = [i for i in range(9)]
random.shuffle(pos)
LatinSquareMix=[]
for i in range(9):
	LatinSquareMix.append(LatinSquare[pos[i]])

#Convert To Base 10
Position=random.randint(0,8)
TempTable=[]
SudokuSolutionTable=[]
for i in LatinSquare[Position]:
	for j in i:
		target=0;
		for n in LatinSquareMix[target]:
			for o in n:
				if(j==0):
					o=o+0*3+1
					TempTable.append(o)
				if(j==1):
					o=o+1*3+1
					TempTable.append(o)
				if(j==2):
					o=o+2*3+1
					TempTable.append(o)
			SudokuSolutionTable.append(TempTable)
			TempTable=[]
		target+=1

#Swap To Get Complete Sudoku Solution Table
SudokuSolutionTable[1],SudokuSolutionTable[9]  =SudokuSolutionTable[9],SudokuSolutionTable[1]
SudokuSolutionTable[4],SudokuSolutionTable[12] =SudokuSolutionTable[12],SudokuSolutionTable[4]
SudokuSolutionTable[7],SudokuSolutionTable[15] =SudokuSolutionTable[15],SudokuSolutionTable[7]
SudokuSolutionTable[2],SudokuSolutionTable[18] =SudokuSolutionTable[18],SudokuSolutionTable[2]
SudokuSolutionTable[5],SudokuSolutionTable[21] =SudokuSolutionTable[21],SudokuSolutionTable[5]
SudokuSolutionTable[8],SudokuSolutionTable[24] =SudokuSolutionTable[24],SudokuSolutionTable[8]
SudokuSolutionTable[11],SudokuSolutionTable[19]=SudokuSolutionTable[19],SudokuSolutionTable[11]
SudokuSolutionTable[14],SudokuSolutionTable[22]=SudokuSolutionTable[22],SudokuSolutionTable[14]
SudokuSolutionTable[17],SudokuSolutionTable[25]=SudokuSolutionTable[25],SudokuSolutionTable[17]

#Digging Hole
NumberOfHole=int(sys.argv[1]);
def DiggingHole():
	if(NumberOfHole==9):
		for i in range(0,9,4):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(9,18,4):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(18,27,4):
			SudokuSolutionTable[i][random.randint(0,2)]=0
	if(NumberOfHole==18):
		for i in range(0,9,4):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(9,18,4):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(18,27,4):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(3,9,2):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(12,18,2):
			SudokuSolutionTable[i][random.randint(0,2)]=0
		for i in range(21,27,2):
			SudokuSolutionTable[i][random.randint(0,2)]=0
	if(NumberOfHole==27):
		for i in range(0,27):
			SudokuSolutionTable[i][random.randint(0,2)]=0
	if(NumberOfHole==36):
		for i in range(0,9,4):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(9,18,4):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(18,27,4):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(3,9,2):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(12,18,2):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(21,27,2):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(0,9,4):
			SudokuSolutionTable[i][1]=0
		for i in range(9,18,4):
			SudokuSolutionTable[i][1]=0
		for i in range(18,27,4):
			SudokuSolutionTable[i][1]=0
		for i in range(3,9,2):
			SudokuSolutionTable[i][1]=0
		for i in range(12,18,2):
			SudokuSolutionTable[i][1]=0
		for i in range(21,27,2):
			SudokuSolutionTable[i][1]=0
	if(NumberOfHole==45):
		for i in range(0,27):
			SudokuSolutionTable[i][random.choice([0,2])]=0
		for i in range(0,9,4):
			SudokuSolutionTable[i][1]=0
		for i in range(9,18,4):
			SudokuSolutionTable[i][1]=0
		for i in range(18,27,4):
			SudokuSolutionTable[i][1]=0
		for i in range(3,9,2):
			SudokuSolutionTable[i][1]=0
		for i in range(12,18,2):
			SudokuSolutionTable[i][1]=0
		for i in range(21,27,2):
			SudokuSolutionTable[i][1]=0
	if(NumberOfHole==54):
		for i in range(0,27):
			SudokuSolutionTable[i][1]=0
		for i in range(0,9,4):
			SudokuSolutionTable[i][0]=0
		for i in range(9,18,4):
			SudokuSolutionTable[i][0]=0
		for i in range(18,27,4):
			SudokuSolutionTable[i][0]=0
		for i in range(3,9,2):
			SudokuSolutionTable[i][0]=0
		for i in range(12,18,2):
			SudokuSolutionTable[i][0]=0
		for i in range(21,27,2):
			SudokuSolutionTable[i][0]=0
		for i in range(3,9,2):
			SudokuSolutionTable[i][2]=0
		for i in range(12,18,2):
			SudokuSolutionTable[i][2]=0
		for i in range(21,27,2):
			SudokuSolutionTable[i][2]=0
		
def ShowLatinSquare(Table):
    for i in range(len(Table)):
        line = ""
        for j in range(len(Table[i])):
            line += str(Table[i][j])+" "
        print(line)
def ShowSudokuSolution(Table):
	line = ""
	for i in range(len(Table)):
		if(i==3 or i==6 or i==9 or i==12 or i==15 or i==18 or i==21 or i==24):
			line+='\n'
		line += str(Table[i])+" "
	return line
def FormatOutput():
	Result=[]
	for i in range(27):
		for j in range(0,3):
			Result.append(SudokuSolutionTable[i][j])
	return Result

#Show
print("Latin Square:")
ShowLatinSquare(LatinSquare)
print("Sudoku Solution: ")
print(ShowSudokuSolution(SudokuSolutionTable))
print("After Dig %d Holes: " %NumberOfHole)
DiggingHole()
print(ShowSudokuSolution(SudokuSolutionTable))

#Write to file
with open(sys.argv[2],"w") as f:
	for i in range(81):
		if(i==8 or i==17 or i==26 or i==35 or i==44 or i==53 or i==62 or i==71 or i==80):
			f.write(str(FormatOutput()[i])+"\n");
		else:
			f.write(str(FormatOutput()[i])+", ");
f.close();
print("\nFinish!!");





