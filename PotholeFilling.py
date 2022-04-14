"""
File: PotholeFilling.py
Author: 魏子菁
--------------------------
karel will fill 3 potholes.
 (learn the concept of decomposition)
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()
#定義向右轉

def go_in():
    move()
    turn_right()
    move()
#定義進洞

def put_99():
    for i in range(99):
        put_beeper()
#定義放99次

def go_out():
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()

def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()

    if __name__ == '__main__':
        execute_karel_task(main)
