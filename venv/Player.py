class Player:
    def __init__(self, position, money_available):
        self._position = position
        self._money_available = money_available

    def MoveTo(self,newposition):
        self._position=newposition

    def AddMoney(self,quantity):
        self._money_available=self._money_available+quantity

    def RemoveMoney(self,quantity):
        self._money_available = self._money_available -quantity

    def IsMoneyAvailable(self):
        if self._money_available>0:
            return True
        else:
            return False
