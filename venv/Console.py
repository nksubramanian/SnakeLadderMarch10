class Console:
    def GetDiceRoll(self,player):
        print(str(player._position) + " and  " + str(player._money_available))
        val = input("Enter the die value: ")
        return int(val)

    def DisplayWinningTheGame(self):
        print("Congrats you have reached cell 49. You've won!")

    def DisplayLosingTheGame(self):
        print("You've run out of money. You've lost!")



