#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while wall_is_on_the_right()==False:
        if wall_is_beneath()==False:move_down(n=1); fill_cell(); move_up(n=1)
        if wall_is_above()==False:move_up(n=1); fill_cell(); move_down(n=1)
        if wall_is_above()==True and wall_is_beneath()==True:fill_cell()
        move_right(n=1)
    if wall_is_beneath()==False:
            move_down(n=1)
            fill_cell()
            move_up(n=1)
    if wall_is_above()==False:
            move_up(n=1)
            fill_cell()
            move_down(n=1)



if __name__ == '__main__':
    run_tasks()
