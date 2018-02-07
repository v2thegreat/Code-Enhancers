def inline_addition(list_of_str_to_add_to,string_to_add):
	s=""
	for x in range(len(list_of_str_to_add_to)):
		if x==len(list_of_str_to_add_to)-1:
			s+=list_of_str_to_add_to[x]

		else:
			s+=list_of_str_to_add_to[x]+string_to_add

	return s

def ifEnhanceAnd(linesOfCode):
	for x in range(len(linesOfCode)):
		line=int(x)
		x=linesOfCode[x]
		if "if" in x:
			t=x[x.find("if")+len("if"):-1].split("and")
			for i in range(len(t)):
				t[i]="("+t[i].strip()+")"
			for i in range(len(t)):
				linesOfCode[line]=inline_addition(t," and ")
			linesOfCode[line]="if "+linesOfCode[line]+":"

	return linesOfCode

def ifEnhanceOr(linesOfCode):
	for x in range(len(linesOfCode)):
		line=int(x)
		x=linesOfCode[x]
		if "if" in x:
			t=x[x.find("if")+len("if"):-1].split("or")
			for i in range(len(t)):
				t[i]="("+t[i].strip()+")"
				linesOfCode[line]=inline_addition(t," or ")
			linesOfCode[line]="if "+linesOfCode[line]+":"

	return linesOfCode

def ifEnhance(linesOfCode):
	for x in range(len(linesOfCode)):
		if "if" in linesOfCode[x]:
			tabSpaces=int(linesOfCode[x].count('\t')/2)*'\t'
			linesOfCode[x]=tabSpaces+ifEnhanceOr(ifEnhanceAnd([linesOfCode[x]]))[-1]
	return linesOfCode

def enhanceFile(fileName):
	codeLines = open(fileName).read()
	codeLines = codeLines.split("\n")
	codeLines = [x + "\n" for x in ifEnhance(codeLines)]
	open(fileName,'w').writelines(codeLines)

def main():
	enhanceFile("Testing_If_Enhance.py")
	print(ifEnhanceOr(["if a or b:"]))

if __name__=='__main__':
	main()
