class NameGame:

    def __init__(self, letter):
        self.letter = letter
        self.entries = [[], [], [], []]
        self.players = []

    def add_player(self, entry):
        x = entry.split()
        self.players.append(x)
        for i in range(4):
            self.entries[i].append(x[i])

    def get_scores(self):
        top_score = 0
        for player in self.players:
            score = 0
            for i in range(4):
                count = self.entries[i].count(player[i])
                if player[i].startswith(self.letter) and count == 1:
                    score += 10
                elif player[i].startswith(self.letter) and count > 1:
                    score += 5
                else:
                    pass

            print(*player, score)

            if score > top_score:
                top_score = score

        print("Top score:", top_score)


game1 = NameGame(input())

while True:
    player = input()
    if player == '':
        break
    game1.add_player(player)

game1.get_scores()
