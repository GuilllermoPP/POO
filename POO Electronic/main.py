# 1. Una tienda de informática vende dos tipos de artículos (software y hardware) ambos
# caracterizados por su código (de tipo char) y su descripción. Además, en los productos
# debe indicar si es un periférico o no. Para saber el precio de un artículo utilice una
# interface que indique que para un artículo cuyo código es A el precio es 100.0 euros, si
# el código es B el precio es 50.3; para un artículo con código C el precio es 150.50
# euros. En el caso de ser un producto hardware, los artículos sólo serán A ó B y si es un
# periférico el precio se incrementará en un 10%. Los productos sofware serán
# exclusivamente B ó C incrementándose el precio del artículo en un 5% si el sofware es
# de tipo ProgramaJuegos. Nota: la interface debe tener un método abstracto.
# a) Implemente las clases y la interfaz.
# b) Realice un programa principal donde cree un objeto software y otro hardware y
# muestre el precio y demás características del objeto.
from Article import Article
from Software import Software
from Hardware import Hardware
def calculatePriceSale (article):
    return article.salePrice()

def main():
    sw1=Software("B","halo","ProgramaJuegos")
    sw2=Software('B',"Crash","ProgramaJuegos")
    sw3=Software('C',"Paquete Ofice 365","ProgramaOfinematica")
    hw1=Hardware('A',"monitor",True)
    hw2=Hardware('A',"Mause Luz RGB",True)
    hw3=Hardware('B',"ventilador",False)
    
    inventaryList=[sw1,sw2,sw3,hw1,hw2,hw3]

    print("Lista de articulos electronicos")
    for a in inventaryList:
        print(a,"\n Precio de vente",calculatePriceSale(a))

if __name__=='__main__':
    main()