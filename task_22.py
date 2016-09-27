#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
   fill_cell()
   if wall_is_beneath()==True and wall_is_above()==True:
    while wall_is_on_the_right()==False:
            fill_cell()
            move_right(n=1)
    while wall_is_on_the_left()==False:
            fill_cell()
            move_left(n=1)
   else:
       while wall_is_beneath()==False or wall_is_on_the_left()==False:
        while wall_is_on_the_right()==False:
            fill_cell()
            move_right(n=1)
        fill_cell()
        if wall_is_beneath()==True: break
        move_down(n=1)
        while wall_is_on_the_left()==False:
            fill_cell()
            move_left(n=1)
        fill_cell()
        if wall_is_beneath()==True: break
        move_down(n=1)
   while wall_is_on_the_right()==False:
            fill_cell()
            move_right(n=1)
   while wall_is_on_the_left()==False:
            fill_cell()
            move_left(n=1)




if __name__ == '__main__':
    run_tasks()
