def inline_addition(list_of_str_to_add_to,string_to_add):
	s=""
	for x in range(len(list_of_str_to_add_to)):
		if x==len(list_of_str_to_add_to)-1:
			s+=list_of_str_to_add_to[x]
		else:
			s+=list_of_str_to_add_to[x]+string_to_add
	return(s)

def if_enhance_and(l):
	for x in range(len(l)):
		line=int(x)
		x=l[x]
		if "if" in x:
			t=x[x.find("if")+len("if"):-1].split("and")
			for i in range(len(t)):
				t[i]="("+t[i].strip()+")"
			for i in range(len(t)):
				l[line]=inline_addition(t," and ")
			l[line ]="if"+l[line]+":"
	return l

def if_enhance_or(l):
	for x in range(len(l)):
		line=int(x)
		x=l[x]
		if "if" in x:
			t=x[x.find("if")+len("if"):-1].split("or")
			for i in range(len(t)):
				t[i]="("+t[i].strip()+")"
				l[line]=inline_addition(t," or ")
			l[line ]="if "+l[line]+":"
	return l

def if_enhance(l):
	for x in range(len(l)):
		if "if" in l[x]:
			l[x]=(int(l[x].count('\t')/2))*'\t'+if_enhance_or(if_enhance_and([l[x]]))[-1]
	return l

def main():
	Code_Input_Folder="Testing_If_Enhance.py"
	Code_Lines=open(Code_Input_Folder).read().split("\n")
	open(Code_Input_Folder,'w').writelines([x+"\n" for x in if_enhance(Code_Lines)])

if __name__=='__main__':
	main()
