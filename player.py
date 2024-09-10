class player:
    def __init__(self, name, money, favored_bet):
        self.name = str(name)
        self.money = money
        self.results = []
        self.favored_bet = favored_bet
        self.current_bet = 1
        self.starting_cash = money

    def winning(self):
        if self.money > self.starting_cash:
            return True

    def add_money(self, money):
        self.money += money

    def add_win(self, bet_type, point, reward):
        self.results.append({'winloss': 'win', 'bet_type': bet_type, 'point': point, 'rewared': reward})
#        print(self.results)
        #print('added win to results')

    def add_loss(self, bet_type, point, reward):
        self.results.append({'winloss': 'loss', 'bet_type': bet_type, 'point': point, 'rewared': reward})
        #print(self.results)
        #$print('added loss to results')

    def current_loss_streak(self):
        count = 0
        if len(self.results) > 0:
            for i in range(len(self.results)):
                inv_count = 0 - (count + 1)
                print(inv_count)
                if self.results[inv_count]['winloss'] == 'loss':
                    count += 1
                else:
                    break
        return count

    def last_lost(self):
        if self.results[-1]['winloss'] == 'loss':
            return True

    def show_money(self):
        if self.winning():
            print(f'{self.name} = {self.money} (winning)')
        else:
            print(f'{self.name} = {self.money}')

        return self.money

    def get_money(self):
        return self.money

    def get_name(self):
        return self.name

    def place_bets(self, bet, history):
        if self.last_lost:
            self.current_bet = (self.current_bet * 2) + 1
        else:
            self.current_bet = 1
        # print(f'current_loss_streak {self.current_loss_streak()}')
        if self.favored_bet not in bet or bet[self.favored_bet] == 0: 
            if self.money > self.current_bet:
                self.money -= self.current_bet
                bet[self.favored_bet] = self.current_bet
        return bet
