class UASB_Methods():
    __slots__=()

    def fL0(self, S0, Q):
        """Carga afluente média de DQO"""
        return S0*Q
    
    def fV(self, Qméd, TDH):
        """Volume do reator
        L_{0}=S_{0}Q 
        L_{0}=DQO_{af}Q_{máx}
        """
        return (Qméd/24)*TDH
    
    def fVMód(self, V, NMód ):
        """Volume de cada módulo"""
        return V/NMód

    def fAMód(self, VMód, H):
        """Área de cada módulo"""
        return  VMód/H

    def fAMódCorr(self, B, L):
        """Área de cada módulo corrigida"""
        return  B*L

    def fATotCorr(self, AMódCorr, NMód):
        """Área total corrigida"""
        return  AMódCorr*NMód

    def fVMódCorr(self, AMódCorr, H):
        """Volume de cada módulo corrigido"""
        return AMódCorr*H

    def fVTotCorr(self, NMód, VMódCorr):
        """Volume total corrigido"""
        return NMód*VMódCorr
    
    def fTDHCorr(self, NMód, VMódCorr, Qméd):
        """ TDH corigido """
        return NMód*VMódCorr/(Qméd/24) 

    # TO DO. Verificar se esta na faixa de valores da norma.
    def fCOV(self, COVMáx, S0, Qméd, V):
        """ Carga orgânica volumétrica """
        cov=(S0*Qméd)/V
        if cov > COVMáx:
            print("Erro no método COV.")
            pass
        else:
            return cov

    def fCHV(self, Q, V):
        """ Carga hidráulica volumétrica """
        return Q/V

    # TO DO. Colocar o teste se esta na faixa de valores da norma
    def fVAscMéd(self, Qméd, ATotCorr):
        return (Qméd/24)/ATotCorr
    
    # TO DO. Colocar o teste se esta na faixa de valores da norma
    def fVAscMáx(self, Qmáx, ATotCorr):
        return (Qmáx/24)/ATotCorr

    def fNTub(self, AMódCorr, AInfTub):
        """Número de tubos de distribuição por módulo"""
        return AMódCorr/AInfTub

    def fEDQO(self, TDH):
        return 100*(1 - 0.68*TDH**(-0.35))

    def fEDBO(self, TDH):
        return 100*(1 - 0.70*TDH**(-0.50))

    # TO DO. Definir qual nome se usa.
    def fSDQO(self, S0, EDQO):
        return S0*(1 - EDQO/100)

    # TO DO. Definir qual nome se usa.
    def fSDBO(self, S0, EDBO):
        return S0*(1 - EDBO/100)

    def fDQOCH4(self, Qméd, S0, S, YObs):
        return Qméd*(S0 - S - YObs*S0)

    def fK(self, t, P, R):
        num=P*64
        den=R*(273 + t)
        return num/den

    def fQCH4(self, DQOCH4, K):
        return DQOCH4/K

    def fQBio(self, QCH4, PCH4):
        return QCH4/(PCH4/100)

    def fNTotCol(self, NCol, NMód):
        return NCol*NMód

    def fLCol(self, QBio, Vg, CTotCol):
        return (QBio/24)/(Vg*CTotCol)

    def fCTotCol(self, B, NMód, NCol):
        return B*NMód*NCol

    def fACol(self, CTotCol, LCol):
        return CTotCol*LCol

    def fVg(self, QBio, ACol):
        return (QBio/24)/ACol

    def fNAS(self, NMód):
        return 2*NMód

    def fNAD(self, NCol, NMód):        
        return (NCol - 1)*NMód

    def fNEqAS(self, NAS, NAD):
        return NAS + 2*NAD

    def fCEqAS(self, NEqAS, B):
        return NEqAS*B

    def fATotAb(self, CEqAS, LAS):
        return CEqAS*LAS

    def fVAscMédAbert(self, Qméd, ATotAb):
        return (Qméd/24)/ATotAb

    def fVAscMáxAbert(self, Qmáx, ATotAb):        
        return (Qmáx/24)/ATotAb

    def fNCD(self, NCol, NMód):
        return NCol*NMód

    def fCTD(self, NCD, B):
        return NCD*B

    def fLg(self, LCol, e):
        return LCol + 2*e

    def fLCompDec(self, L, NCol):
        return L/NCol

    def fLÚ(self, LCompDec, Lg):
        return LCompDec - Lg

    def fATotDec(self, CTD, LÚ):
        return CTD*LÚ

    def fVDMéd(self, Qméd, ATotDec):
        return (Qméd/24)/ATotDec

    def fVDMáx(self, Qmáx, ATotDec):
        return (Qmáx/24)/ATotDec

    def fPLodo(self, Y, L0):
        return Y*L0
    
    def fVLodo(self, PLodo, gamma, c):        
        return PLodo/(gamma*c)


class UASB_Part1():
    __slots__=()

    def parte1(self):
        self.V =self.fV(self.Qméd, self.TDH)
        self.VMód =self.fVMód(self.V, self.NMód)     
        self.AMód =self.fAMód(self.VMód, self.H)


class UASB_Part2():
    __slots__=()

    def parte2(self):
        self.AMódCorr = self.fAMódCorr(self.B, self.L)
        self.ATotCorr = self.fATotCorr(self.AMódCorr, self.NMód)
        self.VMódCorr = self.fVMódCorr(self.AMódCorr, self.H)
        self.VTotCorr = self.fVTotCorr(self.NMód, self.VMódCorr)
        self.TDHCorr = self.fTDHCorr(self.NMód, self.VMódCorr, self.Qméd)
        self.COV = self.fCOV(self.COVMáx, self.DQOaf,  self.Qméd, self.VTotCorr)    
        self.CHV = self.fCHV(self.Qméd, self.VTotCorr)        
        self.VAscMéd = self.fVAscMéd(self.Qméd, self.ATotCorr)        
        self.VAscMáx = self.fVAscMáx(self.Qmáx, self.ATotCorr)        
        self.NTub = self.fNTub(self.AMódCorr, self.AInfTub) 


class UASB_Part3():
    __slots__=()

    def parte3(self):
        self.EDQO = self.fEDQO(self.TDHCorr)
        self.EDBO = self.fEDBO(self.TDHCorr)
        self.SDQO = self.fSDQO(self.DQOaf, self.EDQO)
        self.SDBO = self.fSDBO(self.DBOaf, self.EDBO)
        self.DQOCH4 = self.fDQOCH4(self.Qméd, self.DQOaf,  self.SDQO, self.YObs)
        self.K = self.fK(self.T, self.P,  self.R)
        self.QCH4 = self.fQCH4(self.DQOCH4, self.K)
        self.QBio = self.fQBio(self.QCH4, self.PCH4)
        self.NTotCol = self.fNTotCol(self.NCol, self.NMód)
        self.CTotCol = self.fCTotCol(self.B, self.NMód, self.NCol)
        self.LCol = self.fLCol(self.QBio, self.Vg, self.CTotCol)        
        self.ACol = self.fACol(self.CTotCol, self.LCol)
        self.NAS = self.fNAS(self.NMód)
        self.NAD = self.fNAD(self.NCol, self.NMód)
        self.NEqAS = self.fNEqAS(self.NAS, self.NAD)
        self.CEqAS = self.fCEqAS(self.NEqAS, self.B)
        self.ATotAb = self.fATotAb(self.CEqAS, self.LAS)
        self.VAscMédAbert = self.fVAscMédAbert(self.Qméd, self.ATotAb)
        self.VAscMáxAbert = self.fVAscMáxAbert(self.Qmáx, self.ATotAb)
        self.NCD = self.fNCD(self.NCol, self.NMód)
        self.CTD = self.fCTD(self.NCD, self.B)
        self.Lg = self.fLg(self.LCol, self.e)
        self.LCompDec = self.fLCompDec(self.L, self.NCol)
        self.LÚ = self.fLÚ(self.LCompDec, self.Lg)
        self.ATotDec = self.fATotDec(self.CTD, self.LÚ)
        self.VDMéd = self.fVDMéd(self.Qméd, self.ATotDec)
        self.VDMáx = self.fVDMáx(self.Qmáx, self.ATotDec)
        self.L0 = self.fL0(self.DQOaf, self.Qméd)
        self.PLodo = self.fPLodo(self.Y, self.L0)
        self.VLodo = self.fVLodo(self.PLodo, self.gamma, self.c)


class Extras():
    __slots__=()

    def make_out(self):
        d=dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self,name))) 
        self.out=d

    def arredondamento(self):
        for key in self.out:
            if type(self.out[key]) == float:
                self.out[key]=round(self.out[key],4)

class UASB_Main():
    __slots__=()

    def dimensionar(self):    
        self.parte1()
        self.parte2()
        self.parte3()
        
        self.make_out()
        self.arredondamento()

# Teste de comit mexendo em dois arquivos ao mesmo tempo. 
# Esss dicionarios deveriam esta em outra parte.
uasb_dict_inputs={
    "B":None,
    "L":None,
    "T":None,
    "TDH":None,
    "Qméd":None,
    "Qmáx":None,
    "DQOaf":None,
    "DBOaf":None,
    "NMód":None,
    "H":None,
    "COVMáx":None,
    "CHVMáx":None,
    "AInfTub":None,
    "NTubAdot":None,
    "YObs":None,
    "Y":None,
    "P":None,             
    "R":None,
    "PCH4":None,
    "Vg":None,
    "NCol":None,
    "LAS":None,
    "e":None,
    "gamma":None,
    "c":None
} 


# As classes não são passadas como argumentos para não dificultar 
# para o usuario.
def factory_UASB(inp):  
    r={
        "L0":None,
        "V":None,
        "VMód":None,
        "AMód":None,
        "AMódCorr":None,
        "ATotCorr":None,
        "VMódCorr":None,
        "VTotCorr":None,
        "TDHCorr":None,
        "COV":None,
        "CHV":None,
        "VAscMéd":None,
        "VAscMáx":None,
        "NTub":None,
        "EDQO":None,
        "EDBO":None,
        "SDQO":None,
        "SDBO":None,
        "DQOCH4":None,
        "K":None,
        "QCH4":None,
        "QBio":None,
        "NTotCol":None,
        "CTotCol":None,
        "ACol":None,
        "LCol":None,
        "NAS":None,
        "NAD":None,
        "NEqAS":None,
        "CEqAS":None,
        "ATotAb":None,
        "VAscMédAbert":None,
        "VAscMáxAbert":None,
        "NCD":None,
        "CTD":None,
        "Lg":None,
        "LCompDec":None,
        "LÚ":None,
        "ATotDec":None,
        "VDMéd":None,
        "VDMáx":None,
        "PLodo":None,
        "VLodo":None,
        
        "out":None
    }
    '''
    def verifica_key(e, uasb_inputs):
        for key in e:
            if not key in e_gab:
                assert False, "Chave errada no dicionario de entradas"

    verifica_key(e, e_gab)
    '''
    d=dict(inp, **r)

    class UASB(UASB_Methods, UASB_Part1, UASB_Part2, UASB_Part3,
                Extras, UASB_Main):
        __slots__ = [key for key in d]
        def __init__(self):
            for key in d:
                setattr(self, key, d[key])

    return UASB

        

'''
class UASB():
    __slots__ = (
            "B",
            "L",
            "T",
            "TDH",
            "Qméd",
            "Qmáx",
            "DQOaf",
            "DBOaf",
            "NMód",
            "H",
            "COVMáx",
            "CHVMáx",
            "AInfTub",
            "NTubAdot",
            "YObs",
            "Y",
            "P",             
            "R",
            "PCH4",
            "Vg",
            "NCol",
            "LAS",
            "e",
            "gamma",
            "c",
#######################
            "L0",
            "V",
            "VMód",
            "AMód",
            "AMódCorr",
            "ATotCorr",
            "VMódCorr",
            "VTotCorr",
            "TDHCorr",
            "COV",
            "CHV",
            "VAscMéd",
            "VAscMáx",
            "NTub",
            "EDQO",
            "EDBO",
            "SDQO",
            "SDBO",
            "DQOCH4",
            "K",
            "QCH4",
            "QBio",
            "NTotCol",
            "CTotCol",
            "ACol",
            "Vg",
            "LCol",
            "NAS",
            "NAD",
            "NEqAS",
            "CEqAS",
            "ATotAb",
            "VAscMédAbert",
            "VAscMáxAbert",
            "NCD",
            "CTD",
            "Lg",
            "LCompDec",
            "LÚ",
            "ATotDec",
            "VDMéd",
            "VDMáx",
            "PLodo",
            "VLodo",
            "out")
    
    def __init__(self, B, L, T, TDH, Qméd, Qmáx, DQOaf, 
        DBOaf, NMód, H, COVMáx, CHVMáx, AInfTub, NTubAdot, YObs, Y, P,
         R, PCH4, Vg, NCol, LAS, e, gamma, c):

        self.B          = B
        self.L          = L
        self.T          = T
        self.TDH        = TDH
        self.Qméd       = Qméd
        self.Qmáx       = Qmáx
        self.DQOaf      = DQOaf
        self.DBOaf      = DBOaf
        self.NMód       = NMód
        self.H          = H
        self.COVMáx     = COVMáx
        self.CHVMáx     = CHVMáx
        self.AInfTub    = AInfTub
        self.NTubAdot   = NTubAdot
        self.YObs       = YObs
        self.Y          = Y
        self.P          = P             
        self.R          = R
        self.PCH4       = PCH4
        self.Vg         = Vg
        self.NCol       = NCol
        self.LAS        = LAS  
        self.e          = e
        self.gamma      = gamma
        self.c          = c

                    
        self.L0=None
        self.V=None
        self.VMód=None
        self.AMód=None
        self.AMódCorr=None
        self.ATotCorr=None
        self.VMódCorr=None
        self.VTotCorr=None
        self.TDHCorr=None
        self.COV=None
        self.CHV=None
        self.VAscMéd=None
        self.VAscMáx=None
        self.NTub=None
        self.EDQO=None
        self.EDBO=None
        self.SDQO=None
        self.SDBO=None
        self.DQOCH4=None
        self.K=None
        self.QCH4=None
        self.QBio=None
        self.NTotCol=None
        self.CTotCol=None
        self.ACol=None
        self.NAS=None
        self.NAD=None
        self.NEqAS=None
        self.CEqAS=None
        self.ATotAb=None
        self.VAscMédAbert=None
        self.VAscMáxAbert=None
        self.NCD=None
        self.CTD=None
        self.Lg=None
        self.LCompDec=None
        self.LÚ=None
        self.ATotDec=None
        self.VDMéd=None
        self.VDMáx=None
        self.PLodo=None
        self.VLodo=None
        
        self.out=None
            

    def fL0(self, S0, Q):
        """Carga afluente média de DQO"""
        return S0*Q
    
    def fV(self, Qméd, TDH):
        """Volume do reator
        L_{0}=S_{0}Q 
        L_{0}=DQO_{af}Q_{máx}
        """
        return (Qméd/24)*TDH
    
    def fVMód(self, V, NMód ):
        """Volume de cada módulo"""
        return V/NMód

    def fAMód(self, VMód, H):
        """Área de cada módulo"""
        return  VMód/H

    def fAMódCorr(self, B, L):
        """Área de cada módulo corrigida"""
        return  B*L

    def fATotCorr(self, AMódCorr, NMód):
        """Área total corrigida"""
        return  AMódCorr*NMód

    def fVMódCorr(self, AMódCorr, H):
        """Volume de cada módulo corrigido"""
        return AMódCorr*H

    def fVTotCorr(self, NMód, VMódCorr):
        """Volume total corrigido"""
        return NMód*VMódCorr
    
    def fTDHCorr(self, NMód, VMódCorr, Qméd):
        """ TDH corigido """
        return NMód*VMódCorr/(Qméd/24) 

    # TO DO. Verificar se esta na faixa de valores da norma.
    def fCOV(self, COVMáx, S0, Qméd, V):
        """ Carga orgânica volumétrica """
        cov=(S0*Qméd)/V
        if cov > COVMáx:
            print("Erro no método COV.")
            pass
        else:
            return cov

    def fCHV(self, Q, V):
        """ Carga hidráulica volumétrica """
        return Q/V

    # TO DO. Colocar o teste se esta na faixa de valores da norma
    def fVAscMéd(self, Qméd, ATotCorr):
        return (Qméd/24)/ATotCorr
    
    # TO DO. Colocar o teste se esta na faixa de valores da norma
    def fVAscMáx(self, Qmáx, ATotCorr):
        return (Qmáx/24)/ATotCorr

    def fNTub(self, AMódCorr, AInfTub):
        """Número de tubos de distribuição por módulo"""
        return AMódCorr/AInfTub

    def fEDQO(self, TDH):
        return 100*(1 - 0.68*TDH**(-0.35))

    def fEDBO(self, TDH):
        return 100*(1 - 0.70*TDH**(-0.50))

    # TO DO. Definir qual nome se usa.
    def fSDQO(self, S0, EDQO):
        return S0*(1 - EDQO/100)

    # TO DO. Definir qual nome se usa.
    def fSDBO(self, S0, EDBO):
        return S0*(1 - EDBO/100)

    def fDQOCH4(self, Qméd, S0, S, YObs):
        return Qméd*(S0 - S - YObs*S0)

    def fK(self, t, P, R):
        num=P*64
        den=R*(273 + t)
        return num/den

    def fQCH4(self, DQOCH4, K):
        return DQOCH4/K

    def fQBio(self, QCH4, PCH4):
        return QCH4/(PCH4/100)

    def fNTotCol(self, NCol, NMód):
        return NCol*NMód

    def fLCol(self, QBio, Vg, CTotCol):
        return (QBio/24)/(Vg*CTotCol)

    def fCTotCol(self, B, NMód, NCol):
        return B*NMód*NCol

    def fACol(self, CTotCol, LCol):
        return CTotCol*LCol

    def fVg(self, QBio, ACol):
        return (QBio/24)/ACol

    def fNAS(self, NMód):
        return 2*NMód

    def fNAD(self, NCol, NMód):        
        return (NCol - 1)*NMód

    def fNEqAS(self, NAS, NAD):
        return NAS + 2*NAD

    def fCEqAS(self, NEqAS, B):
        return NEqAS*B

    def fATotAb(self, CEqAS, LAS):
        return CEqAS*LAS

    def fVAscMédAbert(self, Qméd, ATotAb):
        return (Qméd/24)/ATotAb

    def fVAscMáxAbert(self, Qmáx, ATotAb):        
        return (Qmáx/24)/ATotAb

    def fNCD(self, NCol, NMód):
        return NCol*NMód

    def fCTD(self, NCD, B):
        return NCD*B

    def fLg(self, LCol, e):
        return LCol + 2*e

    def fLCompDec(self, L, NCol):
        return L/NCol

    def fLÚ(self, LCompDec, Lg):
        return LCompDec - Lg

    def fATotDec(self, CTD, LÚ):
        return CTD*LÚ

    def fVDMéd(self, Qméd, ATotDec):
        return (Qméd/24)/ATotDec

    def fVDMáx(self, Qmáx, ATotDec):
        return (Qmáx/24)/ATotDec

    def fPLodo(self, Y, L0):
        return Y*L0
    
    def fVLodo(self, PLodo, gamma, c):        
        return PLodo/(gamma*c)


    def make_out(self):
        d=dict((name, getattr(self, name)) for name in dir(self) 
        if not name.startswith('__') and 
        not callable(getattr(self,name))) 
        self.out=d

    def arredondamento(self):
        for key in self.out:
            if type(self.out[key]) == float:
                self.out[key]=round(self.out[key],4)

    def parte1(self):
        self.V =self.fV(self.Qméd, self.TDH)
        self.VMód =self.fVMód(self.V, self.NMód)     
        self.AMód =self.fAMód(self.VMód, self.H)

    def parte2(self):
        self.AMódCorr = self.fAMódCorr(self.B, self.L)
        self.ATotCorr = self.fATotCorr(self.AMódCorr, self.NMód)
        self.VMódCorr = self.fVMódCorr(self.AMódCorr, self.H)
        self.VTotCorr = self.fVTotCorr(self.NMód, self.VMódCorr)
        self.TDHCorr = self.fTDHCorr(self.NMód, self.VMódCorr, self.Qméd)
        self.COV = self.fCOV(self.COVMáx, self.DQOaf,  self.Qméd, self.VTotCorr)    
        self.CHV = self.fCHV(self.Qméd, self.VTotCorr)        
        self.VAscMéd = self.fVAscMéd(self.Qméd, self.ATotCorr)        
        self.VAscMáx = self.fVAscMáx(self.Qmáx, self.ATotCorr)        
        self.NTub = self.fNTub(self.AMódCorr, self.AInfTub) 

    def parte3(self):
        self.EDQO = self.fEDQO(self.TDHCorr)
        self.EDBO = self.fEDBO(self.TDHCorr)
        self.SDQO = self.fSDQO(self.DQOaf, self.EDQO)
        self.SDBO = self.fSDBO(self.DBOaf, self.EDBO)
        self.DQOCH4 = self.fDQOCH4(self.Qméd, self.DQOaf,  self.SDQO, self.YObs)
        self.K = self.fK(self.T, self.P,  self.R)
        self.QCH4 = self.fQCH4(self.DQOCH4, self.K)
        self.QBio = self.fQBio(self.QCH4, self.PCH4)
        self.NTotCol = self.fNTotCol(self.NCol, self.NMód)
        self.CTotCol = self.fCTotCol(self.B, self.NMód, self.NCol)
        self.LCol = self.fLCol(self.QBio, self.Vg, self.CTotCol)        
        self.ACol = self.fACol(self.CTotCol, self.LCol)
        self.NAS = self.fNAS(self.NMód)
        self.NAD = self.fNAD(self.NCol, self.NMód)
        self.NEqAS = self.fNEqAS(self.NAS, self.NAD)
        self.CEqAS = self.fCEqAS(self.NEqAS, self.B)
        self.ATotAb = self.fATotAb(self.CEqAS, self.LAS)
        self.VAscMédAbert = self.fVAscMédAbert(self.Qméd, self.ATotAb)
        self.VAscMáxAbert = self.fVAscMáxAbert(self.Qmáx, self.ATotAb)
        self.NCD = self.fNCD(self.NCol, self.NMód)
        self.CTD = self.fCTD(self.NCD, self.B)
        self.Lg = self.fLg(self.LCol, self.e)
        self.LCompDec = self.fLCompDec(self.L, self.NCol)
        self.LÚ = self.fLÚ(self.LCompDec, self.Lg)
        self.ATotDec = self.fATotDec(self.CTD, self.LÚ)
        self.VDMéd = self.fVDMéd(self.Qméd, self.ATotDec)
        self.VDMáx = self.fVDMáx(self.Qmáx, self.ATotDec)
        self.L0 = self.fL0(self.DQOaf, self.Qméd)
        self.PLodo = self.fPLodo(self.Y, self.L0)
        self.VLodo = self.fVLodo(self.PLodo, self.gamma, self.c)

    def dimensionar(self):
        
        self.parte1()
        self.parte2()
        self.parte3()
        
        self.make_out()
        self.arredondamento()
'''
        