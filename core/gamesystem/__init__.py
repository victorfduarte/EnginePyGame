from zmq import GSSAPI_NT_HOSTBASED
import gamesystem.game_system as gs

game: gs.GameSystem = None


def init():
    global game
    game = gs.GameSystem()