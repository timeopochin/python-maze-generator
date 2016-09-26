from tkinter import *


class New:
    def __init__(self, x, y, size, width):
        self.width = width
        self.size = size
        self.x = x*size + width + 1
        self.y = y*size + width + 1
        self.free = True
        self.walls = [True, True, True, True]
        self.colour = '#fff'


    def change_walls(self, toChange):
        if toChange == 'up':
            self.walls[0] = not self.walls[0]
        if toChange == 'left':
            self.walls[1] = not self.walls[1]
        if toChange == 'right':
            self.walls[2] = not self.walls[2]
        if toChange == 'down':
            self.walls[3] = not self.walls[3]


    def show(self, master):
        master.create_rectangle(self.x + self.width + 1, self.y + self.width + 1, self.x + self.size - self.width, self.y + self.size - self.width, fill=self.colour, outline='')
        if self.walls[0]:
            master.create_line(self.x, self.y, self.x + self.size, self.y, width=self.width, capstyle=PROJECTING)
        if self.walls[1]:
            master.create_line(self.x, self.y + self.size, self.x, self.y, width=self.width, capstyle=PROJECTING)
        if self.walls[2]:
            master.create_line(self.x + self.size, self.y, self.x + self.size, self.y + self.size, width=self.width, capstyle=PROJECTING)
        if self.walls[3]:
            master.create_line(self.x + self.size, self.y + self.size, self.x, self.y + self.size, width=self.width, capstyle=PROJECTING)
