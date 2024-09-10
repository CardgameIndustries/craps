#!/usr/bin/env python
#squawk(1,'sqawk')
import os
from dotenv import load_dotenv


def get_verbosity():
    try:
        if os.getenv("VERBOSITY"):
            verbosity = int(os.getenv("VERBOSITY"))
        elif load_dotenv():
            if os.getenv("VERBOSITY"):
                verbosity = int(os.getenv("VERBOSITY"))
            else:
                verbosity = 0
        else:
            verbosity = 0
    except:
        verbosity = 0
    return verbosity

def squawk(thresh, squawk):
    verbosity = get_verbosity()
    if verbosity > thresh:
        print(squawk)
