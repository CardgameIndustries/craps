from player import player

class grumpy(player):
    def place_bets(self, bet, history):
        if self.money > 0:
            self.money -= 1
            if self.favored_bet in bet: 
                bet[self.favored_bet] += 1
            else:
                bet[self.favored_bet] = 1
        return bet
