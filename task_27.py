#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right(n=1)
    fill_cell()
    a=0
    while wall_is_on_the_right()==False:
        a+=1
        for i in range(a):
            if wall_is_on_the_right()==False: move_right(n=1)
        fill_cell()




if __name__ == '__main__':
    run_tasks()
