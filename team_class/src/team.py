class Team:
    def __init__(self, names, players, coach):
        self.name = names
        self.players = players
        self.coach = coach

    def add_player(self, new_player):
        self.players.append(new_player)
        