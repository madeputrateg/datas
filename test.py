import itertools as iter


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
            s=baca[i].split(" -> ")
            k=s[1].split(" | ")
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

def permutatedlist(rmstr,listnye):
        temp=listnye.copy()
        indextam=[] 
        rout=[]
        for i in range(len(temp)):
            if listnye[i]==rmstr:
                rout.append(i)
        for i in rout:
            temp[i]=""
        for i in range(0,len(rout)):
            tam=list(iter.combinations(rout,i))
            indextam.extend(tam)
        hasil=[]
        for i in indextam:
            hsl=[]
            for z in i:
                temp[z]=rmstr
            for k in temp:
                if k!='':
                    hsl.append(k)
            if not (hsl in hasil):
                hasil.append(hsl)
            for z in i:
                temp[z]=""
        return hasil

def issubstring(trans,rmstr,grammer):
    for i in grammer:
        for z in range(len(trans[i])):
            if rmstr in trans[i][z]:
                ka=permutatedlist(rmstr,trans[i][z])
                if ([] in ka) and (i != rmstr):
                    for l in range( len(ka)):
                        if ka[l]==[]:
                            ka[l]=["ε"]
                    trans[i].extend(ka)
                    continue
                trans[i].extend(ka)

    print(trans)

trans={
    "ha" : [["ha","halo","haha"],["halo","halo","haha"]],
    "se" : [["haha","halo","ha","he"],["ha","ha","ha"]],
    "op" : [["halo","ha"],["se","op"]]
}

def replacecer(grammer,trans,longlist):
    counter=0
    for i in range(len(longlist)-2,0,-1):
        newvar="N"+str(counter)
        trans[newvar]=[]
        trans[newvar].append([longlist[i],longlist[i+1]])
        grammer.append(newvar)
        longlist.pop()
        longlist.pop()
        longlist.append(newvar)
        counter+=1
    return longlist

def rmlistnontm(grammer,trans,listnya):
    counter=0
    newcheck={}
    # value dari dictonary disempen buat dicek apakah udah ada atau belom
    for i in range(len(listnya)):
        if len(listnya)>=2 and not (listnya[i] in grammer):
            if listnya[i] in newcheck.keys():
                listnya[i]=newcheck[listnya[i]]
            newvar="N"+str(counter)
            newcheck[listnya[i]]=newvar
            trans[newvar]=[]
            trans[newvar].append([listnya[i]])
            listnya[i]=newvar
            grammer.append(newvar)
            counter+=1
    return trans


def rmsgter():#remove single terminal
    grammer=["ha","se","op","ho","he"]
    trans={
    "ha" : [["ha","halo","haha"],["halo","halo","haha"]],
    "se" : [["haha","halo","ha","he"],["ha","ha","ha"]],
    "op" : [["halo","ha"],["se","op"],["he"],["ho"]],
    "ho" :[["he"],["haha"]],
    "he"  : [["halo"]]
    }
    checkindex=[]
    for i in grammer:
        for k in range(len(trans[i])):
            if len(trans[i][k])==1 and trans[i][k][0] in grammer:
                checkindex.append([i,k]) 
    while len(checkindex)>0:
        for i in range(len(checkindex)-1,-1,-1):
            if (len(trans[checkindex[i][0]][checkindex[i][1]])>1) or (not (trans[checkindex[i][0]][checkindex[i][1]][0] in grammer)):
                del checkindex[i]
                continue
            isi=trans[trans[checkindex[i][0]][checkindex[i][1]][0]]
            for s in isi:
                if not s in trans[checkindex[i][0]]:
                    trans[checkindex[i][0]].append(s)
            del trans[checkindex[i][0]][checkindex[i][1]]
            del checkindex[i]
    print(trans)


rmsgter()
