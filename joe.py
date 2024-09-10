from player import player

class joe(player):
    def place_bets(self, bet, history):
        if self.money > 0:
            if self.favored_bet in bet: 
                self.money -= 1
                bet[self.favored_bet] += 1
            else:
                self.money -= 1
                bet[self.favored_bet] = 1
        return bet
