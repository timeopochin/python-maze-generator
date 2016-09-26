from a_maze_ing import *
from tkinter import *
import time

startTime = time.time()
maze = Maze.New(50, 50, 20, 1)
print('Time taken to generate:\t{0} seconds'.format(time.time() - startTime))
maze.show()

maze.master.mainloop()
