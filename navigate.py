from a_maze_ing import *
from tkinter import *
import time

startTime = time.time()
maze = Maze.New(100, 100, 10, 1)
print('Time taken to generate:\t{0} seconds'.format(time.time() - startTime))
current = (0, 0, maze.cells[0])
track = False
current[2].colour = '#f00'
maze.show()


def move(event):
    global current, track
    toTestX = (-1, 0, 1) if current[0] < maze.width - 1 else (-1, 0)
    toTestY = (-1, 0, 1) if current[1] < maze.height - 1 else (-1, 0)
    adj = [(current[0] + x, current[1] + y, maze.cells[current[0] + x + maze.width*(current[1] + y)]) for y in toTestY for x in toTestX if abs(x) != abs(y) and not maze.cells[current[0] + x + maze.width*(current[1] + y)].walls[[(0, 1), (1, 0), (-1, 0), (0, -1)].index((x, y))]]
    if event.keycode == 38:
        direction = (0, -1)
    elif event.keycode == 37:
        direction = (-1, 0)
    elif event.keycode == 39:
        direction = (1, 0)
    elif event.keycode == 40:
        direction = (0, 1)
    elif event.keycode == 32:
        direction = None
        track = not track
    for adjCell in adj:
        if direction == (adjCell[0] - current[0], adjCell[1] - current[1]):
            current[2].colour = '#fdf' if track else '#fff'
            current[2].show(maze.canvas)
            adjCell[2].colour = '#f00'
            adjCell[2].show(maze.canvas)
            current = adjCell

maze.master.bind('<Up>', move)
maze.master.bind('<Left>', move)
maze.master.bind('<Right>', move)
maze.master.bind('<Down>', move)
maze.master.bind('<space>', move)
maze.master.mainloop()
