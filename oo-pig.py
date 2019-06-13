import random

class RollOne(Exception):
    pass


class Player:
    """
    Represents a player. 
    """

    def __init__(self, die, score):
        """
        
        """
        self.player1 = "Human"
        self.player2 = "Computer"
        
        

class Die:
    """
    Determines order of play for player. 
    """

    def __init__(self, value):
        
        self.value = value
        
    def roll_die(self):

        return random.randint(1,6)
         


class GameManager():
    def __init__(self, die, player1, player2):
        self.die = die
        self.score = roll_die


    def main(self):
        
        game_manager.play_game()


#main()        




    