"""
File: Steeplechase.py
Author:魏子菁
---------------------------------
Karel crosses hurdles in a 12x12 world
with a for loop

"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def jump():
    up()
    cross()
    down()

def up():
        turn_left()
        #Karel is facing north.
        while not right_is_clear():
            move()

def cross():
    turn_right()
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()


def main():

    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


if __name__ == '__main__':
    execute_karel_task(main)
