"""
File: StepUp.py
Author:魏子菁
------------------------
Karel will pick up the beeper
at Street 1 Avenue 2 and
put it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()
#定義向右轉

def put_99():
    for i in range(99):
        put_beeper()
#定義放99次

def main():
    move()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    move()
    put_99()
    move()


if __name__ == '__main__':
    execute_karel_task(main)
