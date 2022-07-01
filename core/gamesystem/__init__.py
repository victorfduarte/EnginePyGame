
import gamesystem.object_manager as om

game: 'om.ObjectManager' = None


def init():
    global game
    game = om.ObjectManager()