import ukq3rvtf
gombakL=[]

def tinoru():
    index = 0
    while index < len(gombakL):
        index += 1
def papsapka():
    index = 0
    while index < len(gombakL):
        if gombakL[index] == "":
            print("III/C:")
            print("\tAz első papsapkagomba neve: ",gombakL[index.gombaneve])
        index += 1
def gombak_szama():
    index=0
    while index < len(gombakL):
        index += 1
    print("III/A, B:")
    print("\t A gombák száma:"+str(index))

def harmadik():
        kiFajl = open("gombak.txt", "r", encoding="utf-8")
        kiFajl.readline()
        sorok = kiFajl.readlines()
        index = 0
        for i in range(len(sorok)):
            adat = ukq3rvtf.gombak(sorok[i])
            gombakL.append(sorok)
harmadik()
gombak_szama()
papsapka()
tinoru()