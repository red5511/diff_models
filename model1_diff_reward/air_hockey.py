import curses
from ball import Ball
from palette import Palette

X, Y = 60, 30


def boarder_check(win, ball):
	#print(ball.x, ball.y, ball.dx, ball.dy)

	if ball.reset:
		print("reset??")
		ball.reset = False
		ball.y = 10
		ball.dy *= -1
		ball.dx = int(ball.dx / abs(ball.dx))
		for i in range(1, X-1):
			win.addch(Y-1, i, " ")
			win.addch(1, i, " ")


	if (ball.x != ball.dimX-2 and ball.x != 1):
		x_draw =  ball.x - ball.dx
	else:
		x_draw =  ball.x + ball.dx

	win.addch(ball.y - ball.dy, x_draw, " ")

	if ball.y == 1 or ball.y == ball.dimY-1:
		ball.reset = True




curses.initscr()
win = curses.newwin(Y, X, 0, 0) #y, x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

for i in range(1, X-1):
	win.addch(Y-1, i, " ")
	win.addch(0, i, " ")


palette1 = Palette(28, Y-2, 5) 
palette2 = Palette(28, 2, 5)
ball = Ball(X, Y, palette1, palette2, win)

ESC = 27
key = None

points1 = 0
points2 = 0


while key != ESC:
	print('start')
	win.timeout(666)
	win.addstr(0, 3, " Punkty #1 = " + str(points1) + " ")
	win.addstr(0, 40, " Punkty #2 = " + str(points2) + " ")
	win.addch(ball.y, ball.x, "+")



	event = win.getch()
	key = event


	if palette1.shot:
		if palette1.shot == 2:
			for i in range(palette1.len):
				win.addch(palette1.y, palette1.x + i, " ")
			palette1.y += 2
			palette1.shot = 0
		else:
			for i in range(palette1.len):
				win.addch(palette1.y, palette1.x + i, " ")

			palette1.y -= 1
			palette1.shot += 1
	elif key == curses.KEY_LEFT:
		if palette1.x > 1:
			for i in range(palette1.len):
				win.addch(palette1.y, palette1.x + i, " ")
			palette1.x -= 1

	elif key == curses.KEY_RIGHT:
		if palette1.x < X-1 - palette1.len:
			for i in range(palette1.len):
				win.addch(palette1.y, palette1.x + i, " ")
			palette1.x += 1
	elif key == ord(" "):
		palette1.shot = 1
		for i in range(palette1.len):
			win.addch(palette1.y, palette1.x + i, " ")
		palette1.y -= 1

	if palette2.shot:
		if palette2.shot == 2:
			for i in range(palette2.len):
				win.addch(palette2.y, palette2.x + i, " ")
			palette2.y -= 2
			palette2.shot = 0
		else:
			for i in range(palette2.len):
				win.addch(palette2.y, palette2.x + i, " ")
			palette2.y += 1
			palette2.shot += 1
	elif key == ord('a'):
		if palette2.x > 1:
			for i in range(palette2.len):
				win.addch(palette2.y, palette2.x + i, " ")
			palette2.x -= 1
	elif key == ord('d'):
		if palette2.x < X-1 - palette2.len:
			for i in range(palette2.len):
				win.addch(palette2.y, palette2.x + i, " ")
			palette2.x += 1
	elif key == ord("q"):
		palette2.shot = 1
		for i in range(palette2.len):
			win.addch(palette2.y, palette2.x + i, " ")
		palette2.y += 1

	ball.next_move()

	boarder_check(win, ball)

	for i in range(palette1.len):
		win.addch(palette1.y, palette1.x + i, "#")
		win.addch(palette2.y, palette2.x + i, "#")

	print('ball', ball.x, ball.y)
	if ball.y == 1:
		points1 += 1
	elif ball.y == Y-2:
		points2 += 1
	#print('palettle', palette1.x, palette1.y)


curses.endwin()
print('xd')