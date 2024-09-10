# Craps

To play:

`./play_craps.py`

or more verbosely:

`./play_craps.py -v 1000`

or for a custom number games:

`./play_craps.py -g 1000`

or with delays so you can watch what is happening:

`./play_craps.py -v 1000 -s 0.5`

or more verbosely using an env var:

`VERBOSITY=1000 ./play_craps.py`

or set a verbosity using .env:

`echo VERBOSITY=1000 >> .env`

## players

the players inherit from player.py, right now there is bob, grumpy, chipper, and josh, they mainly just change place_bets()
