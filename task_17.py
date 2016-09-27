#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while cell_is_filled()==False:
        move_up(n=1)
    move_right(n=1)
    if cell_is_filled()==False:
        move_left(n=2)


if __name__ == '__main__':
    run_tasks()
