from Animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    
    def cetak_burung(self):    
        super().cetak ()
        print("jenis : ", self.jenis, "\nbunyi : ", self.bunyi)
        
gereja = burung("gereja", "mie ayam", "citerem", "bertelur", "batik solo", "klutukklutuk")
gereja.cetak_burung()


         