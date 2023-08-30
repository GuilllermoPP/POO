from Article import Article
class Software(Article):
    typeA=None
# el atributo tipo se nombra "typeA" debido a que "type" tiene algun uso reservado en Python
    def __init__(self, code, name,typeA):
        super().__init__(code, name)
        self.typeA=typeA
    
    def getTypeA(self):
        return self.typeA

    def setCode(self,typeA):
        self.typeA=typeA

    def __str__(self) -> str:
        return super().__str__() +f'\nTipo: {self.typeA}'
    
    def salePrice(self):
        if (self.getCode() == "B") or (self.getCode() == "C"):
           if self.getTypeA() == "ProgramaJuegos" :
              return self.price()*1.05
           else:
               return self.price()
        return 0.0

