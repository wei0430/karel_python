"""
File: DoubleBeepers.py
Author:魏子菁

Karel will double the beepers
-------------------------------

"""

from karel.stanfordkarel import *

def double_beepers():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()

def move_back():
    move()
    #Karel is on beeper.
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()

def go_home():
    turn_around()
    move()
    move()
    turn_around()

def turn_around():
     for i in range(2):
        turn_left()


def main():
    move()
    double_beepers()
    move_back()
    go_home()


if __name__ == '__main__':
    execute_karel_task(main)