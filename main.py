#!/usr/bin/env python3
import pygame as pg
import sys
from random import randint


SIZE  = W, H = 1000, 600
WHITE = (255, 255, 255)
win = pg.display.set_mode(SIZE)
pg.display.set_caption("Bubble sort")
clock = pg.time.Clock()
n = 20
bar_w = W//n
def draw(lines, win, color):
	for i in range(len(lines)):
		rect = pg.Rect((n + 1) * i, H - lines[i], n, lines[i])
		pg.draw.rect(win, color, rect)


arr = (randint(10, H) for _ in range(bar_w))
arr = list(arr)
counter = 0
color = (155, 0, 255)
sorting = True

	

while True:
	clock.tick(9)
	win.fill(WHITE)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		if  pg.mouse.get_pressed()[0] and not sorting:
			sorting = True
			arr = [randint(10, H) for _ in range(bar_w)]
			counter = 0
			
	if sorting:
		if counter  < len(arr):
			print("sorting!")
			for j in range(len(arr)- 1 - counter):
				if arr[j] > arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
		else:
			sorting = False
		counter += 1

	draw(arr, win, color)
	pg.display.flip()
