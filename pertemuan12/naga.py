from Animal import *

class naga(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    
    def cetak_naga(self):    
        super().cetak ()
        print("jenis : ", self.jenis, "\nbunyi : ", self.bunyi)
        
naga = naga("naga", "daging", "citerem", "bertelur", "batik solo", "khakhakha")
naga.cetak_naga()

