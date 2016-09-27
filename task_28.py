#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    i=0
    while i != 5:
        if cell_is_filled()==True:
            i+=1
        if i==5: break
        if wall_is_on_the_right()==True: break
        else: move_right(n=1)



if __name__ == '__main__':
    run_tasks()
