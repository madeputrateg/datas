import util
class CFGmsk:
    def __init__(self,filepath):
        grammer,simbol,trans,final=util.read_CFG(filepath)
        self.simbol=simbol
        self.trans={}
        for i in grammer:
            for z in grammer:
                self.trans[str(i+z)]=[]
        for i in trans:
            self.trans[i]=trans[i]
        for i in simbol:
            if i not in trans:
                self.trans[i]=""
                continue
            self.trans[i]=trans[i]
        self.final=final
    def findval(self,matrix,x,y):
        msk=[]
        for i in range(x,y):
            gab=util.listconcant(matrix[i][x],matrix[y][i+1])
            msk.extend(gab)
        return msk
    def checkstring(self,string): 
        martixs=util.make_mar(len(string))
        for i in range(len(string)):
            martixs[i][len(martixs[i])-1]=self.trans[string[i]]
        for i in range(1,len(string)):
            for z in range(len(string)-i):
                temp=self.findval(martixs,z,i+z)
                test=set()
                new=[]
                for k in temp:
                    test.add(k)
                for k in test:
                    new.extend(self.trans[k])
                martixs[i+z][z]=list(set(new))
        for i in martixs[len(string)-1][0]:

            if i==self.final:
                print("diterima")
                return
            print("ditolak")
