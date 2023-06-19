fp = open("big_file.csv","w")

for i in range(100000):
    print(f"{i},{2*i}",file=fp)

fp.close()

