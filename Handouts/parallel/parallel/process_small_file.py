import sys

filename = sys.argv[1]
fp = open(filename,"r")
fpo = open("out_"+filename,"w")
for L in fp.readlines():
    num1,num2 = map(int,L.split(','))
    num3 = num1+num2
    print(L[:-1]+f",{num3}",file=fpo)

fpo.close()
fp.close()



