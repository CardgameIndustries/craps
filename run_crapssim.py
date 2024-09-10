#!/usr/bin/env python

import crapssim as craps 
from crapssim.strategy import * 

import numpy as np  
import pandas as pd
from plotnine import *

strategy = ironcross
# Adjust bankroll or rolls here
bankroll = 200
max_rolls = 20 

table = craps.Table()
you = craps.Player(bankroll=bankroll, bet_strategy=strategy)
table.add_player(you)
table.run(max_rolls=max_rolls)
