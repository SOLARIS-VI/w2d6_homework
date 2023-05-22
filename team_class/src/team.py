class Team:
    def __init__(self, names, players, coach):
        self.name = names
        self.players = players
        self.coach = coach

    def add_player(self, new_player):
        self.players.append(new_player)

    def find_player(self, input_player):
        for player in self.players:
            if (player == input_player):
                return True
            
        return False