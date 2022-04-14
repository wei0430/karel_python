"""
File: BeeperRow.py
Author:魏子菁
-------------------------
 Karel will fill up
Street 1 with beepers
(should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


if __name__ == '__main__':
    execute_karel_task(main)