"""
File: BeeperRowAdv.py
Author: 魏子菁
------------------------------
Karel will fill upStreet 1
with some beepers already existed
(should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()

    if not on_beeper():
        put_beeper()
#判斷最後一格動作

#if(not)後必須宣告動作，else可略


if __name__ == '__main__':
    execute_karel_task(main)