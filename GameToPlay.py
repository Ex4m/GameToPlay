# %%

import random


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GamesStorage(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.games_list = []
        self.rank_list = {}
        self.lottery_list = []

    def display_wrapped(func):
        def wrapper(self, *args, **kwargs):
            print("**************************")
            result = func(self, *args, **kwargs)
            print("**************************")
            return result
        return wrapper

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

    @display_wrapped
    def show_lottery_list(self):
        for game in self.lottery_list:
            print(game)

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
            self.populate_lottery_list()
        self.show_lottery_list()
        selected_game = self.pick_from_lottery()
        print("\nRefreshed lottery list")
        self.show_lottery_list()
        return selected_game['name']

    def pick_from_lottery(self):
        picked_game = random.choice(self.lottery_list)
        for game in self.lottery_list:
            self.lottery_list.append(game)
        self.lottery_list = [x for x in self.lottery_list if x ==
                             picked_game] + [x for x in self.lottery_list if x != picked_game]
        return picked_game

    def populate_lottery_list(self):
        for game in self.rank_list:
            for i in range(1, self.rank_list[game]+1):
                self.lottery_list.append(game)

        return self.lottery_list


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

print("------------")
# g.what_we_should_play_tonight()
