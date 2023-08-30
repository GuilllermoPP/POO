from Article import Article

class Hardware (Article):
    __peripherals=False

    def __init__(self, code, name,peripherals):
        super().__init__(code, name)
        self.__peripherals=peripherals

    def isPeripherals(self):
        return self.__peripherals
    
    def setCode(self,peripherals):
        self.__peripherals=peripherals

    def __str__(self) -> str:
        return super().__str__()+ f'\nPeriferico :{self.isPeripherals()}'

    def salePrice(self):
        if self.getCode() == 'A' or self.getCode() == 'B':
            if self.isPeripherals is True :
                return self.price()*1.1
            else:
                return self.price()
        else:
            return 0,0
        
        
    
            