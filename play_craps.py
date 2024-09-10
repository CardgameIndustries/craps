#!/usr/bin/env python
import craps, os, sys, getopt, time
# defaults
iterate_num = 1_000
delay = False
delay_x = 0
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hs:g:v:"

# Long options
long_options = ["help", "sleep=", "games=", "verbosity="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    
    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--help"):
            print('usage: play_craps.py --games=[number of games] --sleep=0.5')
        elif currentArgument in ("-v", "--verbosity"):
            os.environ["VERBOSITY"] = str(currentValue)
        elif currentArgument in ("-s", "--sleep"):
            print (("Enabling sleep mode (% s)") % (currentValue))
            delay_x = float(currentValue)
            delay = True
        elif currentArgument in ("-g", "--games"):
            print (("Iterating for (% s) games") % (currentValue))
            iterate_num = int(currentValue)
            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))


game = craps.craps()

game.add_bob(1_000_000, 'PASS')
game.add_joe(1_000_000, 'NOPASS')
game.add_grumpy(1_000_000, 'NOPASS')
game.add_chipper(1_000_000, 'PASS')
game.show_total_cash()
if delay:
    game.set_sleep(delay_x)
# time.sleep(1)

for i in range(iterate_num):
    game.new_shooter()
    game.show_ratio()
    game.show_total_cash()
    if delay:
        time.sleep(delay_x)

game.show_results()
game.show_ratio()
