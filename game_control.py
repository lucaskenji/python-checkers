class GameControl:
    def __init__(self, starter):
        self.turn = starter
        self.winner = None
    
    def get_turn(self):
        return self.turn
    
    def get_winner(self):
        return self.winner
    
    def change_turn(self):
        self.turn = "W" if self.turn == "B" else "B"
    
    def change_winner(self, winner):
        self.winner = winner