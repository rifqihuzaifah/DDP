from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, 
    design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun  = racun
    def cetak_ular(self):    
        super().cetak ()
        print("design \t\t\t\t : ", self.design, "\nracun \t\t\t : ", self.racun)
        
anaconda = ular("anaconda", "kambing", "amazon", "bertelur", "batik solo", "tidak berbisa")
anaconda.cetak_ular()
        
