def listconcant(list1,list2):
    concatlist=[]
    for i in list2:
        for z in list1:
            concatlist.append(str(z+i))
    return concatlist
def make_mar(pj):
    isi=[]
    for i in range(pj):
        isi.append([])
        for z in range(i+1):
            isi[i].append([])
    return isi
def read_CFG(namafile):
    with open(namafile,'r',encoding='utf-8') as file:
        baca= file.readlines()
        temp={}
        trans={}
        for i in range(len(baca)):
            baca[i]=baca[i][:len(baca[i])-1]
        state=baca[0].split()
        simbol=baca[1].split()
        for i in range(2,len(baca)-1):
            s=baca[i].split(" -> ")
            k=s[1].split(" | ")
            for l in range(len(s)):
                if s[l]=="Îµ":
                    s[l]="ε"
            temp[s[0]]=[]
            for z in k:
                temp[s[0]].append(z.split(" "))
        #     trans[z]=[]
        # for i in temp:
        #     for z in temp[i]:
        #         trans[z].append(i)
        final=baca[len(baca)-1]
        file.close()
    return state,simbol,temp,final

def checkisthere(string,substring):
    pj = len(substring)
    for i in range(len(string)-pj):
        if string[i:i+pj]==substring:
            return True
    return False

def writemachine(T,V,P,S,nmstr):
    with open(nmstr,'w',encoding='utf-8') as f:
        f.write(T)
        f.write("\n")
        f.write(V)
        f.write("\n")
        f.write(P)
        f.write("\n")
        f.write(S)
        f.write("\n")
        f.close()

def tranlateToTable(martix):
    pj=len(martix)
    tablemartix=[]
    for i in range(pj):
        tablemartix.append([])
        for z in range(i+1):
            tablemartix[i].append([])
    for i in range(pj-1,-1,-1):
        for z in range(i+1):
            tablemartix[i][z]=martix[z+pj-1-i][z]
    return tablemartix