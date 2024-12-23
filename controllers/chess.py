
class Game:
    def __init__(self, player1):
        self.colors = ["white", "black"]
        self.players = [player1]

        self.full = False
        self.current_player = 0

    def is_a_player(self, p):
        for player in self.players:
            if player == p:
                return True
            print(f"player {p} found")
        return False

    def verify_move(self, move):
        pass

    def play(self, id, move):
        return False
        

def create_or_get_game(player):
    waiting_game = None
    for game_id in games:
        if player in games[game_id].players:
            return game_id
        if not games[game_id].full and waiting_game == None:
            waiting_game = game_id
        
    
    if waiting_game is not None:
        games[waiting_game].players.append(player)
        games[waiting_game].full = True
        return waiting_game

    newGame = Game(player)
    id = len(games)
    games[id] = newGame
    return id


games = {}

started_games = {}