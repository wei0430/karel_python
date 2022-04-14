"""
File: MoveToTheEnd.py
Author: 魏子菁
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move to the end of the first Street in any world
    """
    while front_is_clear():
        move()
    # When front is not clear


if __name__ == '__main__':
    execute_karel_task(main)
