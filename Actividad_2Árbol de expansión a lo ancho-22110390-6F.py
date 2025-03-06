import pandas as pd
grafo=pd.read_excel('IA_P2.xlsx',sheet_name='Hoja1',index_col=0)
grafo=grafo.fillna(0)
grafo
list(grafo.keys())
def ba(grafo):
    V=list(grafo.keys())
    v1='a'
    S=v1
    Vp=[v1]
    Ep=[]
    yd=V.copy()
    yd.remove(v1)
    flag=False
    s=[]
    while True:
        flag=False
        for x in S:
            for y in yd:
                if grafo[x][y]>0 and (y not in Vp):
                    Ep.append((x,y))
                    Vp.append(y)
                    s.append(y)
                    flag=True
            try:
                _=[yd.remove(y) for y in s]
            except:
                pass
        if not flag:
            T=(Ep,Vp)
            print(T)
            return T
        S=s.copy()
        s=[]
T=ba(grafo)
T
class BA:
    def __init__(self,grafo)->None:
        self.V=list(grafo.keys())
        self.v1='h'
        self.S=self.v1
        self.Vp=[self.v1]
        self.Ep=[]
        self.yd=self.V.copy()
        self.yd.remove(self.v1)
 
 
    def ba(self):
        flag=False
        s=[]
        while True:
            flag=False
            for x in self.S:
                for y in self.yd:
                    if (grafo[x][y]>0) and (y not in self.Vp):
                        self.Ep.append((x,y))
                        self.Vp.append(y)
                        s.append(y)
                        flag=True
                try:
                    _=[self.yd.remove(y) for y in self.s]
                except:
                    pass
            if not flag:
                T=(self.Ep,self.Vp)
                print(T)
                return T
            self.S=self.s.copy()
            s=[]
ba.BA(grafo)  
ba.ba()          