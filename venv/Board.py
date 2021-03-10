from GameStatus import GameStatus
class Board:
    def __init__(self, last_position, snake, ladder):
        self.last_position = last_position
        self._all_position = set(range(1, last_position + 1))
        self._snake = snake
        self._ladder = ladder


    def Play(self, player, diceroll):
        if (player._position + diceroll) not in self._all_position:
            player.RemoveMoney(10)
        elif (player._position + diceroll) in self._snake:
            player.MoveTo(self._snake[player._position + diceroll])
            player.RemoveMoney(100)
        elif (player._position + diceroll) in self._ladder:
            player.MoveTo(self._ladder[player._position + diceroll])
            player.AddMoney(100)
        else:
            player.MoveTo(player._position + diceroll)

    def GameStatus(self,player):
        if player.IsMoneyAvailable()==False:
            return GameStatus.LOST
        if player._position==self.last_position:
            return GameStatus.WON
        else:
            return GameStatus.PLAYING





