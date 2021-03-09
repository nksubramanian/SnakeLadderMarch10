from GameStatus import GameStatus
class Board:
    _all_position = set(range(1, 50))
    _snake = {14: 2, 23: 8, 43: 41, 47: 37}
    _ladder = {5: 10, 12: 26, 16: 29, 19: 33, 35: 36, 40: 45}
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
            return GameStatus(-1)
        if player._position==49:
            return GameStatus(1)
        else:
            return GameStatus(0)





