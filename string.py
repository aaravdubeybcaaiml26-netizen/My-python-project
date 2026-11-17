st=input("emter a string")
#print(st)
#stl=" "
#length=len(st)
alphabet=0
number=0
special=0
#length=0
for i in st:
    if(i.isalpha()):
        alphabet=alphabet+1
    elif(i.isnumeric()):
            number=number+1
    else:
        special=special+1
    #length=length+1
    #st1=i+st1
    #print(i)
        print("alphabet=",alphabet)
        print("number=",number)
        print("special=",special)
