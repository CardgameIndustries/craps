#!/usr/bin/env python
# craps the dice game
# example
# game = craps()
#
# for i in range(1000000):
#     game.new_shooter()
#     game.show_ratio()
#
# game.show_results()
# game.show_ratio()

import dice, time
from bob import bob
from joe import joe
from chipper import chipper
from grumpy import grumpy
from pprint import pprint
from squawk import squawk

class craps:
    def __init__(self):
        #initial_combos['1 + 1']='snake eyes'
        self.players = {}
        self.players_names = []
        self.bets = {}
        self.house_cash = 1_000_000
        self.total_cash_check = 1_000_000
        #self.house_cash = 0
        self.shooter = 0
        self.shooter_history = []
        self.results = {}
        self.shooter_results = {}
        self.winners = (7, 11)
        self.craps = (2, 3, 12)
        self.overall_wins = 0
        self.overall_losses = 0
        self.die1 = dice.die(6)
        self.die2 = dice.die(6)
        self.roll1 = 0
        self.roll2 = 0
        self.point = 0
        self.delay_x = 0
        self.delay = False

    def set_sleep(self, delay_x):
        self.delay_x = delay_x
        self.delay = True

    def add_joe(self, money, favored_bet):
        self.players['joe'] = joe('joe', money, favored_bet)
        self.players_names.append('joe')
        self.total_cash_check += money

    def add_chipper(self, money, favored_bet):
        self.players['chipper'] = chipper('chipper', money, favored_bet)
        self.players_names.append('chipper')
        self.total_cash_check += money

    def add_grumpy(self, money, favored_bet):
        self.players['grumpy'] = grumpy('grumpy', money, favored_bet)
        self.players_names.append('grumpy')
        self.total_cash_check += money

    def add_bob(self, money, favored_bet):
        self.players['bob'] = bob('bob', money, favored_bet)
        self.players_names.append('bob')
        self.total_cash_check += money

    def roll(self):
        self.roll1 = self.die1.roll()
        self.roll2 = self.die2.roll()
        self.shooter_history.append([self.roll1, self.roll2])
        if self.roll2 > self.roll1:
            this_roll = f'{self.roll1} + {self.roll2}'
        else:
            this_roll = f'{self.roll2} + {self.roll1}'
        squawk(11, this_roll)
        point = self.roll1 + self.roll2
        return point

    def record_result(self, point, winloss):
        #self.record_result_shooter(point, winloss)
        self.results.setdefault(point, {'wins': 0,'losses': 0, 'ratio' : 0})
        if winloss == 'win':
            squawk(10, 'win!')
            newWins = self.results[point]['wins'] + 1
            newLosses = self.results[point]['losses']
            self.overall_wins += 1
        elif winloss == 'loss':
            squawk(10, 'lose!')
            newLosses = self.results[point]['losses'] + 1
            newWins = self.results[point]['wins']
            self.overall_losses += 1
        if self.results[point]['losses'] != 0:
            newRatio = newWins / newLosses
        else:
            newRatio = 0
        self.results[point] = {'wins': newWins,'losses': newLosses, 'ratio' : newRatio}
        squawk(20, f'house_cash = {self.house_cash}')

    # not working yet
    # def record_result_shooter(self, point, winloss):
    #     #self.shooter_results[self.players_names[self.shooter]].setdefault({point, {'wins': 0,'losses': 0, 'ratio' : 0}})
    #     self.shooter_results.setdefault([self.shooter], {point, {'wins': 0,'losses': 0, 'ratio' : 0}})
    #     if winloss == 'win':
    #         squawk(10, 'win!')
    #         newWins = self.shooter_results[self.players_names[self.shooter]][point]['wins'] + 1
    #         newLosses = self.shooter_results[self.players_names[self.shooter]][point]['losses']
    #         self.overall_wins += 1
    #     elif winloss == 'loss':
    #         squawk(10, 'lose!')
    #         newLosses = self.shooter_results[self.players_names[self.shooter]][point]['losses'] + 1
    #         newWins = self.shooter_results[self.players_names[self.shooter]][point]['wins']
    #         self.overall_losses += 1
    #     if self.shooter_results[self.players_names[self.shooter]][point]['losses'] != 0:
    #         newRatio = newWins / newLosses
    #     else:
    #         newRatio = 0
    #     self.shooter_results[self.players_names[self.shooter]][point] = {'wins': newWins,'losses': newLosses, 'ratio' : newRatio, 'shooter_name' : self.players_names[self.shooter]}
    #     squawk(20, f'house_cash = {self.house_cash}')

    def show_results(self):
        pprint(self.results)
        #self.show_player_money()
        squawk(0, f'house_cash = {self.house_cash}')
        for player_name, player in self.players.items():
             player.show_money()
        self.show_total_cash()

    def show_total_cash(self):
        squawk(20, f'total_cash = {self.get_total_cash()}')

    def get_total_cash(self):
        total_cash = self.house_cash
        for player in self.bets:
            for bet in self.bets[player]:
                total_cash += int(self.bets[player][bet])
        for player_name, player in self.players.items():
             total_cash += player.get_money()
        return total_cash

    def pay_bets(self):
        pass

    def new_shooter(self):
        if self.shooter >= (len(self.players_names) - 1) or self.shooter < 0:
            self.shooter = 0
        else:
            self.shooter += 1
        squawk(5, f'shooter is now {self.players_names[self.shooter]}')
        self.shooter_history = []
        while self.new_roll():
            squawk(13,'win')

    def new_roll(self):
        self.place_bets()
        self.point = self.roll()
        #self.pay_come_bets()
        if self.point in self.winners:
            self.record_result(self.point, 'win')
            self.PASS=True
            self.pay_PASS_bets()
            self.clear_bets()
            return True
        elif self.point in self.craps:
            self.record_result(self.point, 'loss')
            self.PASS=False
            self.pay_bets()
            self.pay_NOPASS_bets()
            self.clear_bets()
            return False
        else:
            while True:
                self.place_bets()
                this_point = self.roll()
                #self.pay_come_bets()
                if this_point == self.point:
                    self.record_result(self.point, 'win')
                    self.pay_PASS_bets()
                    self.clear_bets()
                    return True
                    break
                elif this_point == 7:
                    self.record_result(self.point, 'loss')
                    self.pay_NOPASS_bets()
                    self.clear_bets()
                    return False
                    break

    def show_house_cash(self):
        squawk(21, f'house_cash = {self.house_cash}')
        return self.house_cash

    def show_ratio(self):
        if self.overall_losses != 0:
            self.overall_ratio = self.overall_wins / float(self.overall_losses)
            squawk(20, f' {self.overall_wins} / {self.overall_losses} = {self.overall_ratio}')
  
    def show_player_money(self): 
        for player_name, player in self.players.items():
             player.show_money()
  
    def clear_bets(self):
        squawk(100, 'clearing bets')
        for player in self.bets:
            for bet in self.bets[player]:
                #print(self.bets[player][bet])
                self.house_cash += int(self.bets[player][bet])
                self.players[player].add_loss(bet, self.point, int(self.bets[player][bet]))
        self.bets = {}

    def pay_NOPASS_bets(self):
        pass
        squawk(101, 'paying NOPASS bets')
    #pprint(self.bets)

    def pay_PASS_bets(self):
        squawk(102, 'paying PASS bets')
        for player_name, player in self.players.items():
            if 'PASS' in self.bets[player.get_name()]:
                reward = int(self.bets[player.get_name()]['PASS'])
                self.house_cash -= reward
                self.bets[player.get_name()]['PASS'] = 0
                player.add_money(reward * 2)
                player.add_win('PASS', self.point, reward)
                #player.show_money()
                self.show_house_cash()
                if self.delay:
                    time.sleep(self.delay_x * 5)
        #pprint(self.bets)

    def check_bank(self):
        if self.get_total_cash() != self.total_cash_check:
            self.show_house_cash()
            squawk(0, f'house_cash = {self.house_cash}')
            self.show_player_money()
            self.show_total_cash()

            print('bank error!')
            exit(1)

    def place_bets(self):
        squawk(103, 'placing bets')
        self.check_bank()
        for player_name, player in self.players.items():
            self.bets.setdefault(player.get_name(),{})
            self.bets[player.get_name()] = player.place_bets(self.bets[player.get_name()],self.shooter_history)
            #player.show_money()
        #pprint(self.bets)
        #self.show_house_cash()
        if self.delay:
            time.sleep(self.delay_x)
