#XadievDev
#37-lesson.Classlarni tekshirish

#-------------------------------------------------#

class Car:
    """(self,make,model,year,km=0,price=None)"""
    def __init__(self,make,model,year,km=0,price=None):
        """Carning xususiyatlari."""
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
    
    def set_price(self,price):
        self.price = price
        
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")
    
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}, " 
        info += f"{self.year}-yil, {self.__km}km yurgan."
        if self.price:
            info += f" Narhi: {self.price}"
        return info
       
    def get_km(self):
        return self.__km

avto1 = Car('bmw','x8',2021,100,30000)

