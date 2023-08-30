# 1. Una tienda de informática vende dos tipos de artículos (software y hardware) ambos
#caracterizados por su código (de tipo char) y su descripción. Además, en los productos
#debe indicar si es un periférico o no. Para saber el precio de un artículo utilice una
#interface que indique que para un artículo cuyo código es A el precio es 100.0 euros, si
#el código es B el precio es 50.3; para un artículo con código C el precio es 150.50
#euros. En el caso de ser un producto hardware, los artículos sólo serán A ó B y si es un
#periférico el precio se incrementará en un 10%. Los productos sofware serán
#exclusivamente B ó C incrementándose el precio del artículo en un 5% si el sofware es
#de tipo ProgramaJuegos. Nota: la interface debe tener un método abstracto.
#a) Implemente las clases y la interfaz.
#b) Realice un programa principal donde cree un objeto software y otro hardware y
#muestre el precio y demás características del objeto.



class Article():
    code=0
    name=""

    def __init__(self,code,name):
        self.code=code
        self.name=name
    
    
    
    def getCode(self):
        return self.code
    
    def getName(self):
        return self.name

    def setCode(self,code):
        self.code=code
    
    def setName(self,name):
        self.name=name

    def __str__(self) :
        return  f'\nCodigo: {self.getCode()}\nNombre: {self.getName()}'
  
    def price(self):
        if self.code == "A":
            return 100.0
        elif self.code == "B":
            return 50.3
        elif self.code == "C":
            return 150.5
        else:
            return 0.0
            


     

