from GameStatus import GameStatus
class GameRunner:
    def Run(self,player, board, console):
        while (board.GameStatus(player) == GameStatus(0)):
            console.DisplayPosition(player)
            rolled_number = console.GetDiceRoll()
            board.Play(player, rolled_number)

        status = board.GameStatus(player)
        if (status == GameStatus(1)):
            console.DisplayWinningTheGame()
            return
        elif (status == GameStatus(-1)):
            console.DisplayLosingTheGame()
            return
        else:
            raise Exception("This is not supposed to happen")