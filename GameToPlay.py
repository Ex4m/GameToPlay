# %%

import random


class GamesStorage:
    def __init__(self) -> None:
        self.games_list = []
        self.rank_list = {}

    def add_game(self, *gameNames):
        for gameName in gameNames:
            game = Game(gameName)
            self.games_list.append(game)

    def remove_name(self, *gameNames):
        self.games_list = [
            game for game in self.games_list if game.name not in gameNames]

    def show_list(self):
        for game in self.games_list:
            print(game.name)

    def show_rank_list(self):
        for game_name, rank in self.rank_list.items():
            print(f"{game_name} - {rank}")

    def generate_rank_list(self):
        for i, game in enumerate(self.games_list, start=1):
            game.set_rank(i)
            self.rank_list[game.name] = game.rank
        self.remaining_numbers = list(range(1, len(self.games_list) + 1))

    def get_uniq_random_num(self):
        if not self.remaining_numbers:
            print("Všechna čísla byla použita.")
            return None
        random_number = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(random_number)
        return random_number

    def what_we_should_play_tonight(self):
        pass


class Game:
    def __init__(self, name):
        self.name = name
        self.rank = None

    def set_rank(self, rank):
        self.rank = rank


# Test
g = GamesStorage()
g.add_game("Karak")
g.add_game("Karak 2")
g.add_game("Carcassone")
g.add_game("Avel")
g.add_game("Plyšová hlídka")
g.add_game("This war of mine")
g.generate_rank_list()

# Zobrazí seznam her a jejich rank
print("Seznam her:")
g.show_list()
print("\nRank list:")
g.show_rank_list()
