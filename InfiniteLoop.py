"""
File: InfiniteLoop.py
Author:魏子菁
------------------------
This file shows the idea of infinite loop,
reminding students one of the 3 bugs in using
while loop
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will be turning left non-stop
    """
    while front_is_clear():
        turn_left()


if __name__ == '__main__':
    execute_karel_task(main)