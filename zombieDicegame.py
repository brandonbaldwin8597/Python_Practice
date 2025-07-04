# ZOMBIE DICE GAME
import zombiedice

# DEMO:
# zombiedice.demo()

# ZOMBIE DICE GAME:
class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
        
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'), 
        #            ('green', 'shotgun')]}
        
        # ZOMBIE STRATEGY CODE
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
        
        
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot')
)

# START TOURNAMENT COMMANDS
# zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)