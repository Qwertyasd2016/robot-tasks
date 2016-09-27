#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down(n=1)
    for i in range(13):
        for a in range(i+1):
            move_right(n=1)
            fill_cell()
        while wall_is_on_the_left()==False:
            move_left(n=1)
        move_down(n=1)
    move_right(n=1)


if __name__ == '__main__':
    run_tasks()
