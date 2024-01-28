# %%
import random


class GamesStorage:
    def __init__(self) -> None:
        self.games_list = []

    def add_game(self, gameName):
        self.games_list.append(gameName)

    def remove_name(self, gameName):
        self.games_list.remove(gameName)

    def show_list(self):
        for i in self.games_list:
            print(i)

    def generate_rank_list(self):
        self.rank_list = {}
        for i in self.games_list:
            if i == 2:
                self.rank_list[self.games_list[i]] = 1
            else:
                value = random.randint(1, len(self.games_list))
                while value in self.rank_list.values():
                    value = random.randint(1, len(self.games_list))
                self.rank_list[self.games_list[i]] = value
        return self.rank_list

    def what_we_should_play_tonight(self):
        pass


g = GamesStorage()
g.add_game("Karak")
g.add_game("Karak 2")
g.add_game("Carcassone")
g.add_game("Avel")
g.add_game("Plyšová hlídka")
g.add_game("This war of mine")


# %%
