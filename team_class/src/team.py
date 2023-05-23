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
    
    # Randolph's Solution:

    # def has_player(self, player):
    #     # return self.players.count(player) > 0
    #     if (self.players.count(player)> 0):
    #         return True
    #     else: 
    #         return False

    
    # Extensions Attempt

    # def team_has_points(self, input_team_points):
    #     for points in self.points:
    #         if (points == input_team_points):
    #             return True

    #     return False