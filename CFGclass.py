import util
import itertools as iter

class CFGmsk:
    def __init__(self,filepath):
        grammer,simbol,trans,final=util.read_CFG(filepath)
        self.simbol=simbol
        self.grammer=grammer
        self.trans=trans
        self.final=final
        self.counter=0
        self.newcheck={}
        self.simplfy()
        self.convert()
    def convert(self):
        simbol=self.simbol
        grammer=self.grammer
        trans=self.trans.copy()
        final=self.final
        newtrans={}
        for i in simbol:
            newtrans[i]=[]
        for i in grammer:
            for z in grammer:
                newtrans[str(i+z)]=[]
        for i in trans:
            for z in range(len(trans[i])):
                trans[i][z]="".join(trans[i][z])
        for i in grammer:
            for z in trans[i]:
                newtrans[z].append(i)
        self.trans=newtrans

    def cetakTrans(self):
        for i in self.trans:
            print("{}:{}".format(i,self.trans[i]))
    def rmsgter(self):#remove single terminal
        grammer=self.grammer
        trans=self.trans
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

    def rmter(self):
        grammer=self.grammer
        trans=self.trans
        for i in range(len(grammer)):
            for z in range(len(trans[grammer[i]])):
                self.rmlisttm(grammer,trans,trans[grammer[i]][z])
    
    def rmlisttm(self,grammer,trans,listnya):
        for i in range(len(listnya)):
            if len(listnya)>=2 and not (listnya[i] in grammer):
                if listnya[i] in self.newcheck.keys():
                    listnya[i]=self.newcheck[listnya[i]]
                newvar="N"+str(self.counter)
                self.newcheck[listnya[i]]=newvar
                trans[newvar]=[]
                trans[newvar].append([listnya[i]])
                listnya[i]=newvar
                grammer.append(newvar)
                self.counter+=1

                    
    def rmoverlength(self):
        grammer=self.grammer
        trans=self.trans
        for i in range(len(grammer)):
            for z in range(len(trans[grammer[i]])):
                if len(trans[grammer[i]][z])>2:
                    self.replacecer(grammer,trans,trans[grammer[i]][z])
        self.grammer=grammer
        self.trans=trans
    def replacecer(self,grammer,trans,longlist):
        for i in range(len(longlist)-2,0,-1):#ngeloop kedepan dari belakang list agar semua variable yang lebih dari panjang list bisa diubah
            newvar="N"+str(self.counter)
            trans[newvar]=[]
            trans[newvar].append([longlist[i],longlist[i+1]])
            grammer.append(newvar)
            longlist.pop()
            longlist.pop()
            longlist.append(newvar)
            self.counter+=1

    def findval(self,matrix,x,y):
        msk=[]
        for i in range(x,y):
            gab=util.listconcant(matrix[i][x],matrix[y][i+1])
            msk.extend(gab)
        return msk
    def simplfy(self):
        grammer=self.grammer
        simbol=self.simbol
        trans=self.trans
        final=self.final
        self.cetakTrans()
        self.rmnull()
        self.cetakTrans()
        self.rmoverlength()
        self.cetakTrans()
        self.rmter()
        self.cetakTrans()
        self.rmsgter()
        self.cetakTrans()
        for i in trans[final]:
            if final in i:
                trans[final+"1"]=trans[final]
                break
        final=final+"1"
    def rmnull(self):
        grammer=self.grammer
        trans=self.trans
        flag=True
        while flag:
            flag=False
            for i in grammer:
                if ["ε"] in trans[i]:
                    self.issubstring(trans,i,grammer)
                    trans[i].remove(["ε"])
                    flag=True
        self.grammer=grammer
        self.trans=trans

    def permutatedlist(self,rmstr,listnye):
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

    def issubstring(self,trans,rmstr,grammer):
        for i in grammer:
            for z in range(len(trans[i])):
                if rmstr in trans[i][z]:
                    ka=self.permutatedlist(rmstr,trans[i][z])
                    if ([] in ka) and (i != rmstr):
                        for l in range( len(ka)):
                            if ka[l]==[]:
                                ka[l]=["ε"]
                        trans[i].extend(ka)
                        continue
                    trans[i].extend(ka)
        


    def checkstring(self,string):
        hslsplt=string.split(" ")
        martixs=util.make_mar(len(hslsplt))
        for i in range(len(hslsplt)):
            martixs[i][len(martixs[i])-1]=self.trans[hslsplt[i]]
        for i in range(1,len(hslsplt)):
            for z in range(len(hslsplt)-i):
                temp=self.findval(martixs,z,i+z)
                test=set()
                new=[]
                for k in temp:
                    test.add(k)
                for k in test:
                    new.extend(self.trans[k])
                martixs[i+z][z]=list(set(new))
        for i in martixs[len(hslsplt)-1][0]:

            if i==self.final:
                print("diterima")
                return
        print("ditolak")
