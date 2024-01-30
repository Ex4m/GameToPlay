# %%

import random


class GamesStorage:
    def __init__(self) -> None:
        self.games_list = []
        self.rank_list = {}
        self.lottery_list = []

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
        self.remaining_numbers = list(range(1, len(self.games_list) + 1))
        for game in self.games_list:
            game.set_rank(self.get_uniq_random_num())
            self.rank_list[game.name] = game.rank

    def get_uniq_random_num(self):
        if not self.remaining_numbers:
            print("Všechna čísla byla použita.")
            return None
        random_number = random.choice(self.remaining_numbers)
        self.remaining_numbers.remove(random_number)
        return random_number

    def what_we_should_play_tonight(self):
        if not self.lottery_list:
            self.refresh_lottery_list()

        selected_game = random.choice(self.lottery_list)
        selected_game_name = selected_game['name']
        selected_game_value = selected_game['value']

        # Snížení hodnoty a posunutí na konec seznamu
        selected_game_value -= 1
        self.lottery_list.remove(selected_game)
        self.lottery_list.append(
            {'name': selected_game_name, 'value': selected_game_value})

        return selected_game_name

    def refresh_lottery_list(self):
        self.lottery_list = [{'name': game.name, 'value': game.rank}
                             for game in self.games_list]


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
