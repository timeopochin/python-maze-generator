from a_maze_ing import Cell
from tkinter import *
import random

class New:
    def __init__(self, width, height, cellSize, wallWidth):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.wallWidth = wallWidth
        self.cells = [Cell.New(x, y, cellSize, wallWidth) for y in range(height) for x in range(width)]
        path = []
        current = (0, 0, self.cells[0])
        while any([cell.free for cell in self.cells]):
            adj = [(current[0] + x, current[1] + y, self.cells[current[0] + x + width*(current[1] + y)]) for y in (-1, 0, 1) for x in (-1, 0, 1) if 0 <= current[0] + x < width and 0 <= current[1] + y < height and self.cells[current[0] + x + width*(current[1] + y)].free and abs(x) != abs(y)]
            current[2].free = False
            try:
                temp = random.choice(adj)
                diff = (temp[0] - current[0], temp[1] - current[1])
                if diff == (0, -1):
                    current[2].change_walls('up')
                    temp[2].change_walls('down')
                elif diff == (0, 1):
                    current[2].change_walls('down')
                    temp[2].change_walls('up')
                elif diff == (-1, 0):
                    current[2].change_walls('left')
                    temp[2].change_walls('right')
                elif diff == (1, 0):
                    current[2].change_walls('right')
                    temp[2].change_walls('left')
                current = temp
                path.append(current)
            except:
                del path[-1]
                current = path[-1]


    def show(self):
        try:
            self.canvas.delete(ALL)
        except:
            self.master = Tk()
            self.canvas = Canvas(self.master, width=self.width*self.cellSize + self.wallWidth, height=self.height*self.cellSize + self.wallWidth, bg='#fff')
            self.canvas.pack()
        for cell in self.cells:
            cell.show(self.canvas)
