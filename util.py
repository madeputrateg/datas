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
    with open(namafile,'r') as file:
        baca= file.readlines()
        temp={}
        trans={}
        for i in range(len(baca)):
            baca[i]=baca[i][:len(baca[i])-1]
        state=baca[0].split()
        simbol=baca[1].split()
        for i in range(2,len(baca)-1):
            k=baca[i][2:].split(" | ")
            temp[baca[i][0]]=[]
            for z in k:
                temp[baca[i][0]].append(z)
                trans[z]=[]
        for i in temp:
            for z in temp[i]:
                trans[z].append(i)
        final=baca[len(baca)-1]
        file.close()
    return state,simbol,trans,final

    
