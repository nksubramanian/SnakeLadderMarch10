import enum
# Using enum class create enumerations
class GameStatus(enum.Enum):
   WON = 1
   LOST = -1
   PLAYING = 0