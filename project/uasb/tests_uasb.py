import unittest
#from uasb import UASB
from uasb import factory_UASB



#####
args_uasb={
"B":12.2,
"L":15,
"T":18,
"TDH":10,
"Qméd":4400,
"Qmáx":7920,
"DQOaf":0.6,
"DBOaf":0.35,
"NMód":2,
"H":5,
"COVMáx":15,
"CHVMáx":5,
"AInfTub":3,
"NTubAdot":70,
"YObs":0.21,
"Y":0.18,
"P":1,
"R":0.08206,
"PCH4":75,
"Vg":1,
"NCol":5,
"LAS":0.40,
"e":0.04,
"gamma":1020,
"c":0.04
}
#####

#####
args_tests={
"L0":2640,
"V":1833,
"VMód":917,
"AMód":183.33,
"AMódCorr":183,
"ATotCorr":366,
"VMódCorr":915,
"VTotCorr":1830,
"TDHCorr":10,
"COV":1.44,
"CHV":2.40,
"VAscMéd":0.5,
"VAscMáx":0.9,
"NTub":61,
"EDQO":70,
"EDBO":77,
"SDQO":0.1824,
"SDBO":0.0775,
"DQOCH4":1283.2,
"K":2.68,
"QCH4":478.7,
"QBio":638.3,
"NTotCol":10,
"CTotCol":122,
"ACol":26.6,
"Vg":1,
"LCol":0.218,
"NAS":4,
"NAD":8,
"NEqAS":20,
"CEqAS":244,
"ATotAb":97.6,
"VAscMédAbert":1.87,
"VAscMáxAbert":3.38,
"NCD":10,
"CTD":122,
"Lg":0.298,
"LCompDec":3,
"LÚ":2.7,
"ATotDec":329.6,
"VDMéd":0.55,
"VDMáx":1,
"PLodo":475.2,
"VLodo":11.64
}

#####

def test_UASB_dimensionar(args_uasb, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            UASB=factory_UASB(args_uasb)
            self.u=UASB()
            self.u.dimensionar()   
            
            d=dict(args_uasb, **args_tests)
            for key in d:
                setattr(self, key, d[key])     

        def tearDown(self):
            del self.u

        
        def test_B(self):
            self.assertTrue( abs(self.u.B - self.B) < 10**(-1), "A variavel B esta errada. O valor deveria ser B={}, mas é {}".format(self.B, self.u.B)) 
        
        def test_L(self):
            self.assertTrue( abs(self.u.L - self.L) < 10**(-1), "A variavel L esta errada. O valor deveria ser L={}, mas é {}".format(self.L, self.u.L)) 
         
        def test_T(self):
            self.assertTrue( abs(self.u.T - self.T) < 10**(-1), "A variavel T esta errada. O valor deveria ser T={}, mas é {}".format(self.T, self.u.T)) 
         
        def test_TDH(self):
            self.assertTrue( abs(self.u.TDH - self.TDH) < 10**(-1), "A variavel TDH esta errada. O valor deveria ser TDH={}, mas é {}".format(self.TDH, self.u.TDH)) 
         
        def test_Qméd(self):
            self.assertTrue( abs(self.u.Qméd - self.Qméd) < 10**(-1), "A variavel Qméd esta errada. O valor deveria ser Qméd={}, mas é {}".format(self.Qméd, self.u.Qméd)) 
         
        def test_Qmáx(self):
            self.assertTrue( abs(self.u.Qmáx - self.Qmáx) < 10**(-1), "A variavel Qmáx esta errada. O valor deveria ser Qmáx={}, mas é {}".format(self.Qmáx, self.u.Qmáx)) 
         
        def test_DQOaf(self):
            self.assertTrue( abs(self.u.DQOaf - self.DQOaf) < 10**(-1), "A variavel DQOaf esta errada. O valor deveria ser DQOaf={}, mas é {}".format(self.DQOaf, self.u.DQOaf)) 
         
        def test_DBOaf(self):
            self.assertTrue( abs(self.u.DBOaf - self.DBOaf) < 10**(-1), "A variavel DBOaf esta errada. O valor deveria ser DBOaf={}, mas é {}".format(self.DBOaf, self.u.DBOaf)) 
         
        def test_NMód(self):
            self.assertTrue( abs(self.u.NMód - self.NMód) < 10**(-1), "A variavel NMód esta errada. O valor deveria ser NMód={}, mas é {}".format(self.NMód, self.u.NMód)) 
         
        def test_H(self):
            self.assertTrue( abs(self.u.H - self.H) < 10**(-1), "A variavel H esta errada. O valor deveria ser H={}, mas é {}".format(self.H, self.u.H)) 
         
        def test_COVMáx(self):
            self.assertTrue( abs(self.u.COVMáx - self.COVMáx) < 10**(-1), "A variavel COVMáx esta errada. O valor deveria ser COVMáx={}, mas é {}".format(self.COVMáx, self.u.COVMáx)) 
         
        def test_CHVMáx(self):
            self.assertTrue( abs(self.u.CHVMáx - self.CHVMáx) < 10**(-1), "A variavel CHVMáx esta errada. O valor deveria ser CHVMáx={}, mas é {}".format(self.CHVMáx, self.u.CHVMáx)) 
         
        def test_AInfTub(self):
            self.assertTrue( abs(self.u.AInfTub - self.AInfTub) < 10**(-1), "A variavel AInfTub esta errada. O valor deveria ser AInfTub={}, mas é {}".format(self.AInfTub, self.u.AInfTub)) 
         
        def test_NTubAdot(self):
            self.assertTrue( abs(self.u.NTubAdot - self.NTubAdot) < 10**(-1), "A variavel NTubAdot esta errada. O valor deveria ser NTubAdot={}, mas é {}".format(self.NTubAdot, self.u.NTubAdot)) 
         
        def test_YObs(self):
            self.assertTrue( abs(self.u.YObs - self.YObs) < 10**(-1), "A variavel YObs esta errada. O valor deveria ser YObs={}, mas é {}".format(self.YObs, self.u.YObs)) 
         
        def test_Y(self):
            self.assertTrue( abs(self.u.Y - self.Y) < 10**(-1), "A variavel Y esta errada. O valor deveria ser Y={}, mas é {}".format(self.Y, self.u.Y)) 
         
        def test_P(self):
            self.assertTrue( abs(self.u.P - self.P) < 10**(-1), "A variavel P esta errada. O valor deveria ser P={}, mas é {}".format(self.P, self.u.P)) 
         
        def test_R(self):
            self.assertTrue( abs(self.u.R - self.R) < 10**(-1), "A variavel R esta errada. O valor deveria ser R={}, mas é {}".format(self.R, self.u.R)) 
         
        def test_PCH4(self):
            self.assertTrue( abs(self.u.PCH4 - self.PCH4) < 10**(-1), "A variavel PCH4 esta errada. O valor deveria ser PCH4={}, mas é {}".format(self.PCH4, self.u.PCH4)) 
         
        def test_Vg(self):
            self.assertTrue( abs(self.u.Vg - self.Vg) < 10**(-1), "A variavel Vg esta errada. O valor deveria ser Vg={}, mas é {}".format(self.Vg, self.u.Vg)) 
         
        def test_NCol(self):
            self.assertTrue( abs(self.u.NCol - self.NCol) < 10**(-1), "A variavel NCol esta errada. O valor deveria ser NCol={}, mas é {}".format(self.NCol, self.u.NCol)) 
         
        def test_LAS(self):
            self.assertTrue( abs(self.u.LAS - self.LAS) < 10**(-1), "A variavel LAS esta errada. O valor deveria ser LAS={}, mas é {}".format(self.LAS, self.u.LAS)) 
         
        def test_e(self):
            self.assertTrue( abs(self.u.e - self.e) < 10**(-1), "A variavel e esta errada. O valor deveria ser e={}, mas é {}".format(self.e, self.u.e)) 
         
        def test_gamma(self):
            self.assertTrue( abs(self.u.gamma - self.gamma) < 10**(-1), "A variavel gamma esta errada. O valor deveria ser gamma={}, mas é {}".format(self.gamma, self.u.gamma)) 
         
        def test_c(self):
            self.assertTrue( abs(self.u.c - self.c) < 10**(-1), "A variavel c esta errada. O valor deveria ser c={}, mas é {}".format(self.c, self.u.c)) 
         
        def test_L0(self):
            self.assertTrue( abs(self.u.L0 - self.L0) < 10**(-1), "A variavel L0 esta errada. O valor deveria ser L0={}, mas é {}".format(self.L0, self.u.L0)) 
         
        def test_V(self):
            self.assertTrue( abs(self.u.V - self.V) < 10**(0), "A variavel V esta errada. O valor deveria ser V={}, mas é {}".format(self.V, self.u.V)) 
         
        def test_VMód(self):
            self.assertTrue( abs(self.u.VMód - self.VMód) < 10**(1), "A variavel VMód esta errada. O valor deveria ser VMód={}, mas é {}".format(self.VMód, self.u.VMód)) 
         
        def test_AMód(self):
            self.assertTrue( abs(self.u.AMód - self.AMód) < 10**(-1), "A variavel AMód esta errada. O valor deveria ser AMód={}, mas é {}".format(self.AMód, self.u.AMód)) 
         
        def test_AMódCorr(self):
            self.assertTrue( abs(self.u.AMódCorr - self.AMódCorr) < 10**(-1), "A variavel AMódCorr esta errada. O valor deveria ser AMódCorr={}, mas é {}".format(self.AMódCorr, self.u.AMódCorr)) 
         
        def test_ATotCorr(self):
            self.assertTrue( abs(self.u.ATotCorr - self.ATotCorr) < 10**(-1), "A variavel ATotCorr esta errada. O valor deveria ser ATotCorr={}, mas é {}".format(self.ATotCorr, self.u.ATotCorr)) 
         
        def test_VMódCorr(self):
            self.assertTrue( abs(self.u.VMódCorr - self.VMódCorr) < 10**(-1), "A variavel VMódCorr esta errada. O valor deveria ser VMódCorr={}, mas é {}".format(self.VMódCorr, self.u.VMódCorr)) 
         
        def test_VTotCorr(self):
            self.assertTrue( abs(self.u.VTotCorr - self.VTotCorr) < 10**(-1), "A variavel VTotCorr esta errada. O valor deveria ser VTotCorr={}, mas é {}".format(self.VTotCorr, self.u.VTotCorr)) 
         
        def test_TDHCorr(self):
            self.assertTrue( abs(self.u.TDHCorr - self.TDHCorr) < 10**(-1), "A variavel TDHCorr esta errada. O valor deveria ser TDHCorr={}, mas é {}".format(self.TDHCorr, self.u.TDHCorr)) 
         
        def test_COV(self):
            self.assertTrue( abs(self.u.COV - self.COV) < 10**(-1), "A variavel COV esta errada. O valor deveria ser COV={}, mas é {}".format(self.COV, self.u.COV)) 
         
        def test_CHV(self):
            self.assertTrue( abs(self.u.CHV - self.CHV) < 10**(-1), "A variavel CHV esta errada. O valor deveria ser CHV={}, mas é {}".format(self.CHV, self.u.CHV)) 
         
        def test_VAscMéd(self):
            self.assertTrue( abs(self.u.VAscMéd - self.VAscMéd) < 10**(-1), "A variavel VAscMéd esta errada. O valor deveria ser VAscMéd={}, mas é {}".format(self.VAscMéd, self.u.VAscMéd)) 
         
        def test_VAscMáx(self):
            self.assertTrue( abs(self.u.VAscMáx - self.VAscMáx) < 10**(-1), "A variavel VAscMáx esta errada. O valor deveria ser VAscMáx={}, mas é {}".format(self.VAscMáx, self.u.VAscMáx)) 
         
        def test_NTub(self):
            self.assertTrue( abs(self.u.NTub - self.NTub) < 10**(-1), "A variavel NTub esta errada. O valor deveria ser NTub={}, mas é {}".format(self.NTub, self.u.NTub)) 
         
        def test_EDQO(self):
            self.assertTrue( abs(self.u.EDQO - self.EDQO) < 10**(-0.3), "A variavel EDQO esta errada. O valor deveria ser EDQO={}, mas é {}".format(self.EDQO, self.u.EDQO)) 
         
        def test_EDBO(self):
            self.assertTrue( abs(self.u.EDBO - self.EDBO) < 10**(0), "A variavel EDBO esta errada. O valor deveria ser EDBO={}, mas é {}".format(self.EDBO, self.u.EDBO)) 
         
        def test_SDQO(self):
            self.assertTrue( abs(self.u.SDQO - self.SDQO) < 10**(-1), "A variavel SDQO esta errada. O valor deveria ser SDQO={}, mas é {}".format(self.SDQO, self.u.SDQO)) 
         
        def test_SDBO(self):
            self.assertTrue( abs(self.u.SDBO - self.SDBO) < 10**(-1), "A variavel SDBO esta errada. O valor deveria ser SDBO={}, mas é {}".format(self.SDBO, self.u.SDBO)) 
         
        def test_DQOCH4(self):
            self.assertTrue( abs(self.u.DQOCH4 - self.DQOCH4) < 10**(1.5), "A variavel DQOCH4 esta errada. O valor deveria ser DQOCH4={}, mas é {}".format(self.DQOCH4, self.u.DQOCH4)) 
         
        def test_K(self):
            self.assertTrue( abs(self.u.K - self.K) < 10**(-1), "A variavel K esta errada. O valor deveria ser K={}, mas é {}".format(self.K, self.u.K)) 
         
        def test_QCH4(self):
            self.assertTrue( abs(self.u.QCH4 - self.QCH4) < 10**(-0.1), "A variavel QCH4 esta errada. O valor deveria ser QCH4={}, mas é {}".format(self.QCH4, self.u.QCH4)) 
         
        def test_QBio(self):
            self.assertTrue( abs(self.u.QBio - self.QBio) < 10**(0.8), "A variavel QBio esta errada. O valor deveria ser QBio={}, mas é {}".format(self.QBio, self.u.QBio)) 
         
        def test_NTotCol(self):
            self.assertTrue( abs(self.u.NTotCol - self.NTotCol) < 10**(0), "A variavel NTotCol esta errada. O valor deveria ser NTotCol={}, mas é {}".format(self.NTotCol, self.u.NTotCol)) 
         
        def test_CTotCol(self):
            self.assertTrue( abs(self.u.CTotCol - self.CTotCol) < 10**(-1), "A variavel CTotCol esta errada. O valor deveria ser CTotCol={}, mas é {}".format(self.CTotCol, self.u.CTotCol)) 
         
        def test_ACol(self):
            self.assertTrue( abs(self.u.ACol - self.ACol) < 10**(0), "A variavel ACol esta errada. O valor deveria ser ACol={}, mas é {}".format(self.ACol, self.u.ACol)) 
         
        def test_Vg(self):
            self.assertTrue( abs(self.u.Vg - self.Vg) < 10**(-1), "A variavel Vg esta errada. O valor deveria ser Vg={}, mas é {}".format(self.Vg, self.u.Vg)) 
         
        def test_LCol(self):
            self.assertTrue( abs(self.u.LCol - self.LCol) < 10**(0), "A variavel LCol esta errada. O valor deveria ser LCol={}, mas é {}".format(self.LCol, self.u.LCol)) 
         
        def test_NAS(self):
            self.assertTrue( abs(self.u.NAS - self.NAS) < 10**(-1), "A variavel NAS esta errada. O valor deveria ser NAS={}, mas é {}".format(self.NAS, self.u.NAS)) 
         
        def test_NAD(self):
            self.assertTrue( abs(self.u.NAD - self.NAD) < 10**(-1), "A variavel NAD esta errada. O valor deveria ser NAD={}, mas é {}".format(self.NAD, self.u.NAD)) 
         
        def test_NEqAS(self):
            self.assertTrue( abs(self.u.NEqAS - self.NEqAS) < 10**(-1), "A variavel NEqAS esta errada. O valor deveria ser NEqAS={}, mas é {}".format(self.NEqAS, self.u.NEqAS)) 
         
        def test_CEqAS(self):
            self.assertTrue( abs(self.u.CEqAS - self.CEqAS) < 10**(-1), "A variavel CEqAS esta errada. O valor deveria ser CEqAS={}, mas é {}".format(self.CEqAS, self.u.CEqAS)) 
         
        def test_ATotAb(self):
            self.assertTrue( abs(self.u.ATotAb - self.ATotAb) < 10**(-1), "A variavel ATotAb esta errada. O valor deveria ser ATotAb={}, mas é {}".format(self.ATotAb, self.u.ATotAb)) 
         
        def test_VAscMédAbert(self):
            self.assertTrue( abs(self.u.VAscMédAbert - self.VAscMédAbert) < 10**(-1), "A variavel VAscMédAbert esta errada. O valor deveria ser VAscMédAbert={}, mas é {}".format(self.VAscMédAbert, self.u.VAscMédAbert)) 
         
        def test_VAscMáxAbert(self):
            self.assertTrue( abs(self.u.VAscMáxAbert - self.VAscMáxAbert) < 10**(-1), "A variavel VAscMáxAbert esta errada. O valor deveria ser VAscMáxAbert={}, mas é {}".format(self.VAscMáxAbert, self.u.VAscMáxAbert)) 
         
        def test_NCD(self):
            self.assertTrue( abs(self.u.NCD - self.NCD) < 10**(-1), "A variavel NCD esta errada. O valor deveria ser NCD={}, mas é {}".format(self.NCD, self.u.NCD)) 
         
        def test_CTD(self):
            self.assertTrue( abs(self.u.CTD - self.CTD) < 10**(-1), "A variavel CTD esta errada. O valor deveria ser CTD={}, mas é {}".format(self.CTD, self.u.CTD)) 
         
        def test_Lg(self):
            self.assertTrue( abs(self.u.Lg - self.Lg) < 10**(-1), "A variavel Lg esta errada. O valor deveria ser Lg={}, mas é {}".format(self.Lg, self.u.Lg)) 
         
        def test_LCompDec(self):
            self.assertTrue( abs(self.u.LCompDec - self.LCompDec) < 10**(-1), "A variavel LCompDec esta errada. O valor deveria ser LCompDec={}, mas é {}".format(self.LCompDec, self.u.LCompDec)) 
         
        def test_LÚ(self):
            self.assertTrue( abs(self.u.LÚ - self.LÚ) < 10**(-1), "A variavel LÚ esta errada. O valor deveria ser LÚ={}, mas é {}".format(self.LÚ, self.u.LÚ)) 
         
        def test_ATotDec(self):
            self.assertTrue( abs(self.u.ATotDec - self.ATotDec) < 10**(-1), "A variavel ATotDec esta errada. O valor deveria ser ATotDec={}, mas é {}".format(self.ATotDec, self.u.ATotDec)) 
         
        def test_VDMéd(self):
            self.assertTrue( abs(self.u.VDMéd - self.VDMéd) < 10**(-1), "A variavel VDMéd esta errada. O valor deveria ser VDMéd={}, mas é {}".format(self.VDMéd, self.u.VDMéd)) 
         
        def test_VDMáx(self):
            self.assertTrue( abs(self.u.VDMáx - self.VDMáx) < 10**(-1), "A variavel VDMáx esta errada. O valor deveria ser VDMáx={}, mas é {}".format(self.VDMáx, self.u.VDMáx)) 
         
        def test_PLodo(self):
            self.assertTrue( abs(self.u.PLodo - self.PLodo) < 10**(-1), "A variavel PLodo esta errada. O valor deveria ser PLodo={}, mas é {}".format(self.PLodo, self.u.PLodo)) 
         
        def test_VLodo(self):
            self.assertTrue( abs(self.u.VLodo - self.VLodo) < 10**(-1), "A variavel VLodo esta errada. O valor deveria ser VLodo={}, mas é {}".format(self.VLodo, self.u.VLodo)) 
                 
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)



ex_prof = test_UASB_dimensionar(args_uasb, args_tests)

suite1=[ex_prof]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)
















'''
#####
B=12.2
L=15
T=18
TDH=10
Qméd=4400
Qmáx=7920
DQOaf=0.6
DBOaf=0.35
NMód=2
H=5
COVMáx=15
CHVMáx=5
AInfTub=3
NTubAdot=70
YObs=0.21
Y=0.18
P=1
R=0.08206
PCH4=75
Vg=1
NCol=5
LAS=0.40
e=0.04
gamma=1020
c=0.04
#####

#####
L0=2640
V=1833
VMód=917
AMód=183.33
AMódCorr=183
ATotCorr=366
VMódCorr=915
VTotCorr=1830
TDHCorr=10
COV=1.44
CHV=2.40
VAscMéd=0.5
VAscMáx=0.9
NTub=61
EDQO=70
EDBO=77
SDQO=0.1824
SDBO=0.0775
DQOCH4=1283.2
K=2.68
QCH4=478.7
QBio=638.3
NTotCol=10
CTotCol=122
ACol=26.6
Vg=1
LCol=0.218
NAS=4
NAD=8
NEqAS=20
CEqAS=244
ATotAb=97.6
VAscMédAbert=1.87
VAscMáxAbert=3.38
NCD=10
CTD=122
Lg=0.298
LCompDec=3
LÚ=2.7
ATotDec=329.6
VDMéd=0.55
VDMáx=1
PLodo=475.2
VLodo=11.64
#####

def test_UASB_dimensionar(args_uasb, args_tests):
    class MyTestCase(unittest.TestCase):
        def setUp(self):
            self.u=UASB(*args_uasb)
            self.u.dimensionar()        

        def tearDown(self):
            del self.u

        def test_B(self):
            self.assertTrue( abs(self.u.B - B) < 10**(-1), "A variavel B esta errada. O valor deveria ser B={}, mas é {}".format(B, self.u.B)) 
        
        def test_L(self):
            self.assertTrue( abs(self.u.L - L) < 10**(-1), "A variavel L esta errada. O valor deveria ser L={}, mas é {}".format(L, self.u.L)) 
         
        def test_T(self):
            self.assertTrue( abs(self.u.T - T) < 10**(-1), "A variavel T esta errada. O valor deveria ser T={}, mas é {}".format(T, self.u.T)) 
         
        def test_TDH(self):
            self.assertTrue( abs(self.u.TDH - TDH) < 10**(-1), "A variavel TDH esta errada. O valor deveria ser TDH={}, mas é {}".format(TDH, self.u.TDH)) 
         
        def test_Qméd(self):
            self.assertTrue( abs(self.u.Qméd - Qméd) < 10**(-1), "A variavel Qméd esta errada. O valor deveria ser Qméd={}, mas é {}".format(Qméd, self.u.Qméd)) 
         
        def test_Qmáx(self):
            self.assertTrue( abs(self.u.Qmáx - Qmáx) < 10**(-1), "A variavel Qmáx esta errada. O valor deveria ser Qmáx={}, mas é {}".format(Qmáx, self.u.Qmáx)) 
         
        def test_DQOaf(self):
            self.assertTrue( abs(self.u.DQOaf - DQOaf) < 10**(-1), "A variavel DQOaf esta errada. O valor deveria ser DQOaf={}, mas é {}".format(DQOaf, self.u.DQOaf)) 
         
        def test_DBOaf(self):
            self.assertTrue( abs(self.u.DBOaf - DBOaf) < 10**(-1), "A variavel DBOaf esta errada. O valor deveria ser DBOaf={}, mas é {}".format(DBOaf, self.u.DBOaf)) 
         
        def test_NMód(self):
            self.assertTrue( abs(self.u.NMód - NMód) < 10**(-1), "A variavel NMód esta errada. O valor deveria ser NMód={}, mas é {}".format(NMód, self.u.NMód)) 
         
        def test_H(self):
            self.assertTrue( abs(self.u.H - H) < 10**(-1), "A variavel H esta errada. O valor deveria ser H={}, mas é {}".format(H, self.u.H)) 
         
        def test_COVMáx(self):
            self.assertTrue( abs(self.u.COVMáx - COVMáx) < 10**(-1), "A variavel COVMáx esta errada. O valor deveria ser COVMáx={}, mas é {}".format(COVMáx, self.u.COVMáx)) 
         
        def test_CHVMáx(self):
            self.assertTrue( abs(self.u.CHVMáx - CHVMáx) < 10**(-1), "A variavel CHVMáx esta errada. O valor deveria ser CHVMáx={}, mas é {}".format(CHVMáx, self.u.CHVMáx)) 
         
        def test_AInfTub(self):
            self.assertTrue( abs(self.u.AInfTub - AInfTub) < 10**(-1), "A variavel AInfTub esta errada. O valor deveria ser AInfTub={}, mas é {}".format(AInfTub, self.u.AInfTub)) 
         
        def test_NTubAdot(self):
            self.assertTrue( abs(self.u.NTubAdot - NTubAdot) < 10**(-1), "A variavel NTubAdot esta errada. O valor deveria ser NTubAdot={}, mas é {}".format(NTubAdot, self.u.NTubAdot)) 
         
        def test_YObs(self):
            self.assertTrue( abs(self.u.YObs - YObs) < 10**(-1), "A variavel YObs esta errada. O valor deveria ser YObs={}, mas é {}".format(YObs, self.u.YObs)) 
         
        def test_Y(self):
            self.assertTrue( abs(self.u.Y - Y) < 10**(-1), "A variavel Y esta errada. O valor deveria ser Y={}, mas é {}".format(Y, self.u.Y)) 
         
        def test_P(self):
            self.assertTrue( abs(self.u.P - P) < 10**(-1), "A variavel P esta errada. O valor deveria ser P={}, mas é {}".format(P, self.u.P)) 
         
        def test_R(self):
            self.assertTrue( abs(self.u.R - R) < 10**(-1), "A variavel R esta errada. O valor deveria ser R={}, mas é {}".format(R, self.u.R)) 
         
        def test_PCH4(self):
            self.assertTrue( abs(self.u.PCH4 - PCH4) < 10**(-1), "A variavel PCH4 esta errada. O valor deveria ser PCH4={}, mas é {}".format(PCH4, self.u.PCH4)) 
         
        def test_Vg(self):
            self.assertTrue( abs(self.u.Vg - Vg) < 10**(-1), "A variavel Vg esta errada. O valor deveria ser Vg={}, mas é {}".format(Vg, self.u.Vg)) 
         
        def test_NCol(self):
            self.assertTrue( abs(self.u.NCol - NCol) < 10**(-1), "A variavel NCol esta errada. O valor deveria ser NCol={}, mas é {}".format(NCol, self.u.NCol)) 
         
        def test_LAS(self):
            self.assertTrue( abs(self.u.LAS - LAS) < 10**(-1), "A variavel LAS esta errada. O valor deveria ser LAS={}, mas é {}".format(LAS, self.u.LAS)) 
         
        def test_e(self):
            self.assertTrue( abs(self.u.e - e) < 10**(-1), "A variavel e esta errada. O valor deveria ser e={}, mas é {}".format(e, self.u.e)) 
         
        def test_gamma(self):
            self.assertTrue( abs(self.u.gamma - gamma) < 10**(-1), "A variavel gamma esta errada. O valor deveria ser gamma={}, mas é {}".format(gamma, self.u.gamma)) 
         
        def test_c(self):
            self.assertTrue( abs(self.u.c - c) < 10**(-1), "A variavel c esta errada. O valor deveria ser c={}, mas é {}".format(c, self.u.c)) 
         
        def test_L0(self):
            self.assertTrue( abs(self.u.L0 - L0) < 10**(-1), "A variavel L0 esta errada. O valor deveria ser L0={}, mas é {}".format(L0, self.u.L0)) 
         
        def test_V(self):
            self.assertTrue( abs(self.u.V - V) < 10**(0), "A variavel V esta errada. O valor deveria ser V={}, mas é {}".format(V, self.u.V)) 
         
        def test_VMód(self):
            self.assertTrue( abs(self.u.VMód - VMód) < 10**(1), "A variavel VMód esta errada. O valor deveria ser VMód={}, mas é {}".format(VMód, self.u.VMód)) 
         
        def test_AMód(self):
            self.assertTrue( abs(self.u.AMód - AMód) < 10**(-1), "A variavel AMód esta errada. O valor deveria ser AMód={}, mas é {}".format(AMód, self.u.AMód)) 
         
        def test_AMódCorr(self):
            self.assertTrue( abs(self.u.AMódCorr - AMódCorr) < 10**(-1), "A variavel AMódCorr esta errada. O valor deveria ser AMódCorr={}, mas é {}".format(AMódCorr, self.u.AMódCorr)) 
         
        def test_ATotCorr(self):
            self.assertTrue( abs(self.u.ATotCorr - ATotCorr) < 10**(-1), "A variavel ATotCorr esta errada. O valor deveria ser ATotCorr={}, mas é {}".format(ATotCorr, self.u.ATotCorr)) 
         
        def test_VMódCorr(self):
            self.assertTrue( abs(self.u.VMódCorr - VMódCorr) < 10**(-1), "A variavel VMódCorr esta errada. O valor deveria ser VMódCorr={}, mas é {}".format(VMódCorr, self.u.VMódCorr)) 
         
        def test_VTotCorr(self):
            self.assertTrue( abs(self.u.VTotCorr - VTotCorr) < 10**(-1), "A variavel VTotCorr esta errada. O valor deveria ser VTotCorr={}, mas é {}".format(VTotCorr, self.u.VTotCorr)) 
         
        def test_TDHCorr(self):
            self.assertTrue( abs(self.u.TDHCorr - TDHCorr) < 10**(-1), "A variavel TDHCorr esta errada. O valor deveria ser TDHCorr={}, mas é {}".format(TDHCorr, self.u.TDHCorr)) 
         
        def test_COV(self):
            self.assertTrue( abs(self.u.COV - COV) < 10**(-1), "A variavel COV esta errada. O valor deveria ser COV={}, mas é {}".format(COV, self.u.COV)) 
         
        def test_CHV(self):
            self.assertTrue( abs(self.u.CHV - CHV) < 10**(-1), "A variavel CHV esta errada. O valor deveria ser CHV={}, mas é {}".format(CHV, self.u.CHV)) 
         
        def test_VAscMéd(self):
            self.assertTrue( abs(self.u.VAscMéd - VAscMéd) < 10**(-1), "A variavel VAscMéd esta errada. O valor deveria ser VAscMéd={}, mas é {}".format(VAscMéd, self.u.VAscMéd)) 
         
        def test_VAscMáx(self):
            self.assertTrue( abs(self.u.VAscMáx - VAscMáx) < 10**(-1), "A variavel VAscMáx esta errada. O valor deveria ser VAscMáx={}, mas é {}".format(VAscMáx, self.u.VAscMáx)) 
         
        def test_NTub(self):
            self.assertTrue( abs(self.u.NTub - NTub) < 10**(-1), "A variavel NTub esta errada. O valor deveria ser NTub={}, mas é {}".format(NTub, self.u.NTub)) 
         
        def test_EDQO(self):
            self.assertTrue( abs(self.u.EDQO - EDQO) < 10**(-0.3), "A variavel EDQO esta errada. O valor deveria ser EDQO={}, mas é {}".format(EDQO, self.u.EDQO)) 
         
        def test_EDBO(self):
            self.assertTrue( abs(self.u.EDBO - EDBO) < 10**(0), "A variavel EDBO esta errada. O valor deveria ser EDBO={}, mas é {}".format(EDBO, self.u.EDBO)) 
         
        def test_SDQO(self):
            self.assertTrue( abs(self.u.SDQO - SDQO) < 10**(-1), "A variavel SDQO esta errada. O valor deveria ser SDQO={}, mas é {}".format(SDQO, self.u.SDQO)) 
         
        def test_SDBO(self):
            self.assertTrue( abs(self.u.SDBO - SDBO) < 10**(-1), "A variavel SDBO esta errada. O valor deveria ser SDBO={}, mas é {}".format(SDBO, self.u.SDBO)) 
         
        def test_DQOCH4(self):
            self.assertTrue( abs(self.u.DQOCH4 - DQOCH4) < 10**(1.5), "A variavel DQOCH4 esta errada. O valor deveria ser DQOCH4={}, mas é {}".format(DQOCH4, self.u.DQOCH4)) 
         
        def test_K(self):
            self.assertTrue( abs(self.u.K - K) < 10**(-1), "A variavel K esta errada. O valor deveria ser K={}, mas é {}".format(K, self.u.K)) 
         
        def test_QCH4(self):
            self.assertTrue( abs(self.u.QCH4 - QCH4) < 10**(-0.1), "A variavel QCH4 esta errada. O valor deveria ser QCH4={}, mas é {}".format(QCH4, self.u.QCH4)) 
         
        def test_QBio(self):
            self.assertTrue( abs(self.u.QBio - QBio) < 10**(0.8), "A variavel QBio esta errada. O valor deveria ser QBio={}, mas é {}".format(QBio, self.u.QBio)) 
         
        def test_NTotCol(self):
            self.assertTrue( abs(self.u.NTotCol - NTotCol) < 10**(0), "A variavel NTotCol esta errada. O valor deveria ser NTotCol={}, mas é {}".format(NTotCol, self.u.NTotCol)) 
         
        def test_CTotCol(self):
            self.assertTrue( abs(self.u.CTotCol - CTotCol) < 10**(-1), "A variavel CTotCol esta errada. O valor deveria ser CTotCol={}, mas é {}".format(CTotCol, self.u.CTotCol)) 
         
        def test_ACol(self):
            self.assertTrue( abs(self.u.ACol - ACol) < 10**(0), "A variavel ACol esta errada. O valor deveria ser ACol={}, mas é {}".format(ACol, self.u.ACol)) 
         
        def test_Vg(self):
            self.assertTrue( abs(self.u.Vg - Vg) < 10**(-1), "A variavel Vg esta errada. O valor deveria ser Vg={}, mas é {}".format(Vg, self.u.Vg)) 
         
        def test_LCol(self):
            self.assertTrue( abs(self.u.LCol - LCol) < 10**(0), "A variavel LCol esta errada. O valor deveria ser LCol={}, mas é {}".format(LCol, self.u.LCol)) 
         
        def test_NAS(self):
            self.assertTrue( abs(self.u.NAS - NAS) < 10**(-1), "A variavel NAS esta errada. O valor deveria ser NAS={}, mas é {}".format(NAS, self.u.NAS)) 
         
        def test_NAD(self):
            self.assertTrue( abs(self.u.NAD - NAD) < 10**(-1), "A variavel NAD esta errada. O valor deveria ser NAD={}, mas é {}".format(NAD, self.u.NAD)) 
         
        def test_NEqAS(self):
            self.assertTrue( abs(self.u.NEqAS - NEqAS) < 10**(-1), "A variavel NEqAS esta errada. O valor deveria ser NEqAS={}, mas é {}".format(NEqAS, self.u.NEqAS)) 
         
        def test_CEqAS(self):
            self.assertTrue( abs(self.u.CEqAS - CEqAS) < 10**(-1), "A variavel CEqAS esta errada. O valor deveria ser CEqAS={}, mas é {}".format(CEqAS, self.u.CEqAS)) 
         
        def test_ATotAb(self):
            self.assertTrue( abs(self.u.ATotAb - ATotAb) < 10**(-1), "A variavel ATotAb esta errada. O valor deveria ser ATotAb={}, mas é {}".format(ATotAb, self.u.ATotAb)) 
         
        def test_VAscMédAbert(self):
            self.assertTrue( abs(self.u.VAscMédAbert - VAscMédAbert) < 10**(-1), "A variavel VAscMédAbert esta errada. O valor deveria ser VAscMédAbert={}, mas é {}".format(VAscMédAbert, self.u.VAscMédAbert)) 
         
        def test_VAscMáxAbert(self):
            self.assertTrue( abs(self.u.VAscMáxAbert - VAscMáxAbert) < 10**(-1), "A variavel VAscMáxAbert esta errada. O valor deveria ser VAscMáxAbert={}, mas é {}".format(VAscMáxAbert, self.u.VAscMáxAbert)) 
         
        def test_NCD(self):
            self.assertTrue( abs(self.u.NCD - NCD) < 10**(-1), "A variavel NCD esta errada. O valor deveria ser NCD={}, mas é {}".format(NCD, self.u.NCD)) 
         
        def test_CTD(self):
            self.assertTrue( abs(self.u.CTD - CTD) < 10**(-1), "A variavel CTD esta errada. O valor deveria ser CTD={}, mas é {}".format(CTD, self.u.CTD)) 
         
        def test_Lg(self):
            self.assertTrue( abs(self.u.Lg - Lg) < 10**(-1), "A variavel Lg esta errada. O valor deveria ser Lg={}, mas é {}".format(Lg, self.u.Lg)) 
         
        def test_LCompDec(self):
            self.assertTrue( abs(self.u.LCompDec - LCompDec) < 10**(-1), "A variavel LCompDec esta errada. O valor deveria ser LCompDec={}, mas é {}".format(LCompDec, self.u.LCompDec)) 
         
        def test_LÚ(self):
            self.assertTrue( abs(self.u.LÚ - LÚ) < 10**(-1), "A variavel LÚ esta errada. O valor deveria ser LÚ={}, mas é {}".format(LÚ, self.u.LÚ)) 
         
        def test_ATotDec(self):
            self.assertTrue( abs(self.u.ATotDec - ATotDec) < 10**(-1), "A variavel ATotDec esta errada. O valor deveria ser ATotDec={}, mas é {}".format(ATotDec, self.u.ATotDec)) 
         
        def test_VDMéd(self):
            self.assertTrue( abs(self.u.VDMéd - VDMéd) < 10**(-1), "A variavel VDMéd esta errada. O valor deveria ser VDMéd={}, mas é {}".format(VDMéd, self.u.VDMéd)) 
         
        def test_VDMáx(self):
            self.assertTrue( abs(self.u.VDMáx - VDMáx) < 10**(-1), "A variavel VDMáx esta errada. O valor deveria ser VDMáx={}, mas é {}".format(VDMáx, self.u.VDMáx)) 
         
        def test_PLodo(self):
            self.assertTrue( abs(self.u.PLodo - PLodo) < 10**(-1), "A variavel PLodo esta errada. O valor deveria ser PLodo={}, mas é {}".format(PLodo, self.u.PLodo)) 
         
        def test_VLodo(self):
            self.assertTrue( abs(self.u.VLodo - VLodo) < 10**(-1), "A variavel VLodo esta errada. O valor deveria ser VLodo={}, mas é {}".format(VLodo, self.u.VLodo)) 
         
    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)


args_uasb=[
B,
L,
T, 
TDH, 
Qméd,
Qmáx,
DQOaf,
DBOaf,
NMód,
H,
COVMáx,
CHVMáx,
AInfTub,
NTubAdot,
YObs,
Y,
P,
R,
PCH4,
Vg,
NCol,
LAS,
e,
gamma,
c
]

args_tests=[
L0,
V,
VMód,
AMód,
AMódCorr,
ATotCorr,
VMódCorr,
VTotCorr,
TDHCorr,
COV,
CHV,
VAscMéd,
VAscMáx,
NTub,
EDQO,
EDBO,
SDQO,
SDBO,
DQOCH4,
K,
QCH4,
QBio,
NTotCol,
CTotCol,
ACol,
Vg,
LCol,
NAS,
NAD,
NEqAS,
CEqAS,
ATotAb,
VAscMédAbert,
VAscMáxAbert,
NCD,
CTD,
Lg,
LCompDec,
LÚ,
ATotDec,
VDMéd,
VDMáx,
PLodo,
VLodo
]

ex_prof = test_UASB_dimensionar(args_uasb, args_tests)

suite1=[ex_prof]
alltests = unittest.TestSuite(suite1)
result = unittest.TextTestRunner(verbosity=2).run(alltests)
'''
   


'''
def test_UASB_dimensionar(B, L, T, TDH, Qméd, Qmáx, DQOaf,
    DBOaf, NMód, H, COVMáx, CHVMáx, AInfTub, NTubAdot, YObs, Y, P, R, 
    PCH4, Vg, NCol, LAS, e, gamma, c,
        L0, V, VMód, AMód, AMódCorr, ATotCorr,
    VMódCorr, VTotCorr, TDHCorr, COV, CHV, VAscMéd, 
    VAscMáx, NTub, EDQO, EDBO, SDQO, SDBO, DQOCH4, K,
    QCH4, QBio, CTotCol, ACol):

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            self.u=UASB(B, L, T, TDH, Qméd, Qmáx, DQOaf, DBOaf, NMód,
             H, COVMáx, CHVMáx, AInfTub, NTubAdot, YObs, Y, P, R, PCH4,
              Vg, NCol, LAS, e, gamma, c)
            self.u.dimensionar()        

        def tearDown(self):
            del self.u

        def test_B(self):
            self.assertTrue( abs(u.B - B) < 10**(-1), "A variavel B esta errada. O valor deveria ser B={}, mas é {}".format(B, u.B)) 
         
        def test_L(self):
            self.assertTrue( abs(u.L - L) < 10**(-1), "A variavel L esta errada. O valor deveria ser L={}, mas é {}".format(L, u.L)) 
         
        def test_T(self):
            self.assertTrue( abs(u.T - T) < 10**(-1), "A variavel T esta errada. O valor deveria ser T={}, mas é {}".format(T, u.T)) 
         
        def test_TDH(self):
            self.assertTrue( abs(u.TDH - TDH) < 10**(-1), "A variavel TDH esta errada. O valor deveria ser TDH={}, mas é {}".format(TDH, u.TDH)) 
         
        def test_Qméd(self):
            self.assertTrue( abs(u.Qméd - Qméd) < 10**(-1), "A variavel Qméd esta errada. O valor deveria ser Qméd={}, mas é {}".format(Qméd, u.Qméd)) 
         
        def test_Qmáx(self):
            self.assertTrue( abs(u.Qmáx - Qmáx) < 10**(-1), "A variavel Qmáx esta errada. O valor deveria ser Qmáx={}, mas é {}".format(Qmáx, u.Qmáx)) 
         
        def test_DQOaf(self):
            self.assertTrue( abs(u.DQOaf - DQOaf) < 10**(-1), "A variavel DQOaf esta errada. O valor deveria ser DQOaf={}, mas é {}".format(DQOaf, u.DQOaf)) 
         
        def test_DBOaf(self):
            self.assertTrue( abs(u.DBOaf - DBOaf) < 10**(-1), "A variavel DBOaf esta errada. O valor deveria ser DBOaf={}, mas é {}".format(DBOaf, u.DBOaf)) 
         
        def test_NMód(self):
            self.assertTrue( abs(u.NMód - NMód) < 10**(-1), "A variavel NMód esta errada. O valor deveria ser NMód={}, mas é {}".format(NMód, u.NMód)) 
         
        def test_H(self):
            self.assertTrue( abs(u.H - H) < 10**(-1), "A variavel H esta errada. O valor deveria ser H={}, mas é {}".format(H, u.H)) 
         
        def test_COVMáx(self):
            self.assertTrue( abs(u.COVMáx - COVMáx) < 10**(-1), "A variavel COVMáx esta errada. O valor deveria ser COVMáx={}, mas é {}".format(COVMáx, u.COVMáx)) 
         
        def test_CHVMáx(self):
            self.assertTrue( abs(u.CHVMáx - CHVMáx) < 10**(-1), "A variavel CHVMáx esta errada. O valor deveria ser CHVMáx={}, mas é {}".format(CHVMáx, u.CHVMáx)) 
         
        def test_AInfTub(self):
            self.assertTrue( abs(u.AInfTub - AInfTub) < 10**(-1), "A variavel AInfTub esta errada. O valor deveria ser AInfTub={}, mas é {}".format(AInfTub, u.AInfTub)) 
         
        def test_NTubAdot(self):
            self.assertTrue( abs(u.NTubAdot - NTubAdot) < 10**(-1), "A variavel NTubAdot esta errada. O valor deveria ser NTubAdot={}, mas é {}".format(NTubAdot, u.NTubAdot)) 
         
        def test_YObs(self):
            self.assertTrue( abs(u.YObs - YObs) < 10**(-1), "A variavel YObs esta errada. O valor deveria ser YObs={}, mas é {}".format(YObs, u.YObs)) 
         
        def test_Y(self):
            self.assertTrue( abs(u.Y - Y) < 10**(-1), "A variavel Y esta errada. O valor deveria ser Y={}, mas é {}".format(Y, u.Y)) 
         
        def test_P(self):
            self.assertTrue( abs(u.P - P) < 10**(-1), "A variavel P esta errada. O valor deveria ser P={}, mas é {}".format(P, u.P)) 
         
        def test_R(self):
            self.assertTrue( abs(u.R - R) < 10**(-1), "A variavel R esta errada. O valor deveria ser R={}, mas é {}".format(R, u.R)) 
         
        def test_PCH4(self):
            self.assertTrue( abs(u.PCH4 - PCH4) < 10**(-1), "A variavel PCH4 esta errada. O valor deveria ser PCH4={}, mas é {}".format(PCH4, u.PCH4)) 
         
        def test_Vg(self):
            self.assertTrue( abs(u.Vg - Vg) < 10**(-1), "A variavel Vg esta errada. O valor deveria ser Vg={}, mas é {}".format(Vg, u.Vg)) 
         
        def test_NCol(self):
            self.assertTrue( abs(u.NCol - NCol) < 10**(-1), "A variavel NCol esta errada. O valor deveria ser NCol={}, mas é {}".format(NCol, u.NCol)) 
         
        def test_LAS(self):
            self.assertTrue( abs(u.LAS - LAS) < 10**(-1), "A variavel LAS esta errada. O valor deveria ser LAS={}, mas é {}".format(LAS, u.LAS)) 
         
        def test_e(self):
            self.assertTrue( abs(u.e - e) < 10**(-1), "A variavel e esta errada. O valor deveria ser e={}, mas é {}".format(e, u.e)) 
         
        def test_gamma(self):
            self.assertTrue( abs(u.gamma - gamma) < 10**(-1), "A variavel gamma esta errada. O valor deveria ser gamma={}, mas é {}".format(gamma, u.gamma)) 
         
        def test_c(self):
            self.assertTrue( abs(u.c - c) < 10**(-1), "A variavel c esta errada. O valor deveria ser c={}, mas é {}".format(c, u.c)) 
         
        def test_L0(self):
            self.assertTrue( abs(u.L0 - L0) < 10**(-1), "A variavel L0 esta errada. O valor deveria ser L0={}, mas é {}".format(L0, u.L0)) 
         
        def test_V(self):
            self.assertTrue( abs(u.V - V) < 10**(0), "A variavel V esta errada. O valor deveria ser V={}, mas é {}".format(V, u.V)) 
         
        def test_VMód(self):
            self.assertTrue( abs(u.VMód - VMód) < 10**(1), "A variavel VMód esta errada. O valor deveria ser VMód={}, mas é {}".format(VMód, u.VMód)) 
         
        def test_AMód(self):
            self.assertTrue( abs(u.AMód - AMód) < 10**(-1), "A variavel AMód esta errada. O valor deveria ser AMód={}, mas é {}".format(AMód, u.AMód)) 
         
        def test_AMódCorr(self):
            self.assertTrue( abs(u.AMódCorr - AMódCorr) < 10**(-1), "A variavel AMódCorr esta errada. O valor deveria ser AMódCorr={}, mas é {}".format(AMódCorr, u.AMódCorr)) 
         
        def test_ATotCorr(self):
            self.assertTrue( abs(u.ATotCorr - ATotCorr) < 10**(-1), "A variavel ATotCorr esta errada. O valor deveria ser ATotCorr={}, mas é {}".format(ATotCorr, u.ATotCorr)) 
         
        def test_VMódCorr(self):
            self.assertTrue( abs(u.VMódCorr - VMódCorr) < 10**(-1), "A variavel VMódCorr esta errada. O valor deveria ser VMódCorr={}, mas é {}".format(VMódCorr, u.VMódCorr)) 
         
        def test_VTotCorr(self):
            self.assertTrue( abs(u.VTotCorr - VTotCorr) < 10**(-1), "A variavel VTotCorr esta errada. O valor deveria ser VTotCorr={}, mas é {}".format(VTotCorr, u.VTotCorr)) 
         
        def test_TDHCorr(self):
            self.assertTrue( abs(u.TDHCorr - TDHCorr) < 10**(-1), "A variavel TDHCorr esta errada. O valor deveria ser TDHCorr={}, mas é {}".format(TDHCorr, u.TDHCorr)) 
         
        def test_COV(self):
            self.assertTrue( abs(u.COV - COV) < 10**(-1), "A variavel COV esta errada. O valor deveria ser COV={}, mas é {}".format(COV, u.COV)) 
         
        def test_CHV(self):
            self.assertTrue( abs(u.CHV - CHV) < 10**(-1), "A variavel CHV esta errada. O valor deveria ser CHV={}, mas é {}".format(CHV, u.CHV)) 
         
        def test_VAscMéd(self):
            self.assertTrue( abs(u.VAscMéd - VAscMéd) < 10**(-1), "A variavel VAscMéd esta errada. O valor deveria ser VAscMéd={}, mas é {}".format(VAscMéd, u.VAscMéd)) 
         
        def test_VAscMáx(self):
            self.assertTrue( abs(u.VAscMáx - VAscMáx) < 10**(-1), "A variavel VAscMáx esta errada. O valor deveria ser VAscMáx={}, mas é {}".format(VAscMáx, u.VAscMáx)) 
         
        def test_NTub(self):
            self.assertTrue( abs(u.NTub - NTub) < 10**(-1), "A variavel NTub esta errada. O valor deveria ser NTub={}, mas é {}".format(NTub, u.NTub)) 
         
        def test_EDQO(self):
            self.assertTrue( abs(u.EDQO - EDQO) < 10**(-0.3), "A variavel EDQO esta errada. O valor deveria ser EDQO={}, mas é {}".format(EDQO, u.EDQO)) 
         
        def test_EDBO(self):
            self.assertTrue( abs(u.EDBO - EDBO) < 10**(0), "A variavel EDBO esta errada. O valor deveria ser EDBO={}, mas é {}".format(EDBO, u.EDBO)) 
         
        def test_SDQO(self):
            self.assertTrue( abs(u.SDQO - SDQO) < 10**(-1), "A variavel SDQO esta errada. O valor deveria ser SDQO={}, mas é {}".format(SDQO, u.SDQO)) 
         
        def test_SDBO(self):
            self.assertTrue( abs(u.SDBO - SDBO) < 10**(-1), "A variavel SDBO esta errada. O valor deveria ser SDBO={}, mas é {}".format(SDBO, u.SDBO)) 
         
        def test_DQOCH4(self):
            self.assertTrue( abs(u.DQOCH4 - DQOCH4) < 10**(1.5), "A variavel DQOCH4 esta errada. O valor deveria ser DQOCH4={}, mas é {}".format(DQOCH4, u.DQOCH4)) 
         
        def test_K(self):
            self.assertTrue( abs(u.K - K) < 10**(-1), "A variavel K esta errada. O valor deveria ser K={}, mas é {}".format(K, u.K)) 
         
        def test_QCH4(self):
            self.assertTrue( abs(u.QCH4 - QCH4) < 10**(-0.1), "A variavel QCH4 esta errada. O valor deveria ser QCH4={}, mas é {}".format(QCH4, u.QCH4)) 
         
        def test_QBio(self):
            self.assertTrue( abs(u.QBio - QBio) < 10**(0.8), "A variavel QBio esta errada. O valor deveria ser QBio={}, mas é {}".format(QBio, u.QBio)) 
         
#        def test_NTotCol(self):
#            self.assertTrue( abs(u.NTotCol - NTotCol) < 10**(0), "A variavel NTotCol esta errada. O valor deveria ser NTotCol={}, mas é {}".format(NTotCol, u.NTotCol)) 
         
        def test_CTotCol(self):
            self.assertTrue( abs(u.CTotCol - CTotCol) < 10**(-1), "A variavel CTotCol esta errada. O valor deveria ser CTotCol={}, mas é {}".format(CTotCol, u.CTotCol)) 
         
        def test_ACol(self):
            self.assertTrue( abs(u.ACol - ACol) < 10**(0), "A variavel ACol esta errada. O valor deveria ser ACol={}, mas é {}".format(ACol, u.ACol)) 
         
        def test_Vg(self):
            self.assertTrue( abs(u.Vg - Vg) < 10**(-1), "A variavel Vg esta errada. O valor deveria ser Vg={}, mas é {}".format(Vg, u.Vg)) 
        """ 
        def test_LCol(self):
            self.assertTrue( abs(u.LCol - LCol) < 10**(0), "A variavel LCol esta errada. O valor deveria ser LCol={}, mas é {}".format(LCol, u.LCol)) 
         
        def test_NAS(self):
            self.assertTrue( abs(u.NAS - NAS) < 10**(-1), "A variavel NAS esta errada. O valor deveria ser NAS={}, mas é {}".format(NAS, u.NAS)) 
         
        def test_NAD(self):
            self.assertTrue( abs(u.NAD - NAD) < 10**(-1), "A variavel NAD esta errada. O valor deveria ser NAD={}, mas é {}".format(NAD, u.NAD)) 
         
        def test_NEqAS(self):
            self.assertTrue( abs(u.NEqAS - NEqAS) < 10**(-1), "A variavel NEqAS esta errada. O valor deveria ser NEqAS={}, mas é {}".format(NEqAS, u.NEqAS)) 
         
        def test_CEqAS(self):
            self.assertTrue( abs(u.CEqAS - CEqAS) < 10**(-1), "A variavel CEqAS esta errada. O valor deveria ser CEqAS={}, mas é {}".format(CEqAS, u.CEqAS)) 
         
        def test_ATotAb(self):
            self.assertTrue( abs(u.ATotAb - ATotAb) < 10**(-1), "A variavel ATotAb esta errada. O valor deveria ser ATotAb={}, mas é {}".format(ATotAb, u.ATotAb)) 
         
        def test_VAscMédAbert(self):
            self.assertTrue( abs(u.VAscMédAbert - VAscMédAbert) < 10**(-1), "A variavel VAscMédAbert esta errada. O valor deveria ser VAscMédAbert={}, mas é {}".format(VAscMédAbert, u.VAscMédAbert)) 
         
        def test_VAscMáxAbert(self):
            self.assertTrue( abs(u.VAscMáxAbert - VAscMáxAbert) < 10**(-1), "A variavel VAscMáxAbert esta errada. O valor deveria ser VAscMáxAbert={}, mas é {}".format(VAscMáxAbert, u.VAscMáxAbert)) 
         
        def test_NCD(self):
            self.assertTrue( abs(u.NCD - NCD) < 10**(-1), "A variavel NCD esta errada. O valor deveria ser NCD={}, mas é {}".format(NCD, u.NCD)) 
         
        def test_CTD(self):
            self.assertTrue( abs(u.CTD - CTD) < 10**(-1), "A variavel CTD esta errada. O valor deveria ser CTD={}, mas é {}".format(CTD, u.CTD)) 
         
        def test_Lg(self):
            self.assertTrue( abs(u.Lg - Lg) < 10**(-1), "A variavel Lg esta errada. O valor deveria ser Lg={}, mas é {}".format(Lg, u.Lg)) 
         
        def test_LCompDec(self):
            self.assertTrue( abs(u.LCompDec - LCompDec) < 10**(-1), "A variavel LCompDec esta errada. O valor deveria ser LCompDec={}, mas é {}".format(LCompDec, u.LCompDec)) 
         
        def test_LÚ(self):
            self.assertTrue( abs(u.LÚ - LÚ) < 10**(-1), "A variavel LÚ esta errada. O valor deveria ser LÚ={}, mas é {}".format(LÚ, u.LÚ)) 
         
        def test_ATotDec(self):
            self.assertTrue( abs(u.ATotDec - ATotDec) < 10**(-1), "A variavel ATotDec esta errada. O valor deveria ser ATotDec={}, mas é {}".format(ATotDec, u.ATotDec)) 
         
        def test_VDMéd(self):
            self.assertTrue( abs(u.VDMéd - VDMéd) < 10**(-1), "A variavel VDMéd esta errada. O valor deveria ser VDMéd={}, mas é {}".format(VDMéd, u.VDMéd)) 
         
        def test_VDMáx(self):
            self.assertTrue( abs(u.VDMáx - VDMáx) < 10**(-1), "A variavel VDMáx esta errada. O valor deveria ser VDMáx={}, mas é {}".format(VDMáx, u.VDMáx)) 
         
        def test_PLodo(self):
            self.assertTrue( abs(u.PLodo - PLodo) < 10**(-1), "A variavel PLodo esta errada. O valor deveria ser PLodo={}, mas é {}".format(PLodo, u.PLodo)) 
         
        def test_VLodo(self):
            self.assertTrue( abs(u.VLodo - VLodo) < 10**(-1), "A variavel VLodo esta errada. O valor deveria ser VLodo={}, mas é {}".format(VLodo, u.VLodo)) 
         """

    return unittest.TestLoader().loadTestsFromTestCase(MyTestCase)


'''