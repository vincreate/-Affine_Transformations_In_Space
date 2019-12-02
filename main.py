from tkinter import *
from lib import Point, Canvas3D, Line, Figure, Flags
from math import cos, sin, acos, sqrt, fabs

		
root = Tk()
root.minsize(1280, 720)
root.maxsize(1280, 720)

canv = Canvas(root, width = 1100, height = 720, bg = "white")
canv3D = Canvas3D(canv, Point(1100/2, 720/2, 200000))

k = 5

flags = Flags()
flags.edit_flags("active", 0)

#__Functions__#	
def keypress(event):
	print(event.keycode)
	active = flags.get_flag_value("active")
	#__Движение объекта__
	if event.keycode == 87:#Создать клетчку(клавиша W)
		canv.delete("all")
		active.move(Point(0, -k, 0))
		active.draw()
	if event.keycode == 83:#Создать клетчку(клавиша S)
		canv.delete("all")
		active.move(Point(0, k, 0))
		active.draw()
	if event.keycode == 65:#Создать клетчку(клавиша A)
		canv.delete("all")
		active.move(Point(-k, 0, 0))
		active.draw()
	if event.keycode == 68:#Создать клетчку(клавиша D)
		canv.delete("all")
		active.move(Point(k, 0, 0))
		active.draw()
	if event.keycode == 81:#Создать клетчку(клавиша Z)
		canv.delete("all")
		active.move(Point(0, 0, k))
		active.draw()
	if event.keycode == 69:#Создать клетчку(клавиша E)
		canv.delete("all")
		active.move(Point(0, 0, -k))
		active.draw()
	#____________________

	#__Вращение объекта__
	if event.keycode == 38:#Создать клетчку(клавиша ↑)
		canv.delete("all")
		active.turn(Point(k, 0, 0))
		active.draw()
		
	if event.keycode == 40:#Создать клетчку(клавиша ↓)
		canv.delete("all")
		active.turn(Point(-k, 0, 0))
		active.draw()

	if event.keycode == 37:#Создать клетчку(клавиша ←)
		canv.delete("all")
		active.turn(Point(0, -k, 0))
		active.draw()

	if event.keycode == 39:#Создать клетчку(клавиша →)
		canv.delete("all")
		active.turn(Point(0, k, 0))
		active.draw()

	if event.keycode == 98:#Создать клетчку(клавиша 1 numpad)
		canv.delete("all")
		active.turn(Point(0, 0, k))
		active.draw()

	if event.keycode == 97:#Создать клетчку(клавиша 2 numpad)
		canv.delete("all")
		active.turn(Point(0, 0, -k))
		active.draw()

	if event.keycode == 49:#Создать клетчку(клавиша 1)
		canv.delete("all")
		flags.edit_flags("active", figure1)
		flags.get_flag_value("active").draw()

	if event.keycode == 50:#Создать клетчку(клавиша 2)
		canv.delete("all")
		flags.edit_flags("active", figure2)
		flags.get_flag_value("active").draw()
	#____________________

		
def start(event):
	print(1)
#___________#

#__Interface__#

btn_start = Button(root, text="Statr", width=30,height=2, bg="white",fg="black")
btn_start.bind("<Button-1>", start)
canv.bind("<Key>", keypress)

canv.focus_set()


#__Program__#
x0 = Point(100, 100, 100)
x1 = Point(100, -100, 100)
x2 = Point(-100, -100, 100)
x3 = Point(-100, 100, 100)
x4 = Point(100, 100, -100)
x5 = Point(100, -100, -100)
x6 = Point(-100, -100, -100)
x7 = Point(-100, 100, -100)


x8 = Point(50, 50, 100)
x9 = Point(50, -50, 100)
x10 = Point(-50, -50, 100)
x11 = Point(-50, 50, 100)
x12 = Point(50, 50, -100)
x13 = Point(50, -50, -100)
x14 = Point(-50, -50, -100)
x15 = Point(-50, 50, -100)
x16 = Point(100, 50, 50)
x17 = Point(100, -50, 50)
x18 = Point(100, -50, -50)
x19 = Point(100, 50, -50)
x20 = Point(-100, 50, 50)
x21 = Point(-100, -50, 50)
x22 = Point(-100, -50, -50)
x23 = Point(-100, 50, -50)
x24 = Point(50, 100, 50)
x25 = Point(-50, 100, 50)
x26 = Point(-50, 100, -50)
x27 = Point(50, 100, -50)
x28 = Point(50, -100, 50)
x29 = Point(-50, -100, 50)
x30 = Point(-50, -100, -50)
x31 = Point(50, -100, -50)

x32 = Point(50, 50, 500)
x33 = Point(50, -50, 500)
x34 = Point(-50, -50, 500)
x35 = Point(-50, 50, 500)
x36 = Point(50, 50, -500)
x37 = Point(50, -50, -500)
x38 = Point(-50, -50, -500)
x39 = Point(-50, 50, -500)
x40 = Point(500, 50, 50)
x41 = Point(500, -50, 50)
x42 = Point(500, -50, -50)
x43 = Point(500, 50, -50)
x44 = Point(-500, 50, 50)
x45 = Point(-500, -50, 50)
x46 = Point(-500, -50, -50)
x47 = Point(-500, 50, -50)
x48 = Point(50, 500, 50)
x49 = Point(-50, 500, 50)
x50 = Point(-50, 500, -50)
x51 = Point(50, 500, -50)
x52 = Point(50, -500, 50)
x53 = Point(-50, -500, 50)
x54 = Point(-50, -500, -50)
x55 = Point(50, -500, -50)

arr1 = [Line(x0, x1),
		Line(x1, x2),
		Line(x2, x3),
		Line(x3, x0),
		Line(x4, x5),
		Line(x5, x6),
		Line(x6, x7),
		Line(x7, x4),
		Line(x0, x4),
		Line(x1, x5),
		Line(x2, x6),
		Line(x3, x7)]

arr2 = [Line(x0, x1),
		Line(x1, x2),
		Line(x2, x3),
		Line(x3, x0),
		Line(x4, x5),
		Line(x5, x6),
		Line(x6, x7),
		Line(x7, x4),
		Line(x0, x4),
		Line(x1, x5),
		Line(x2, x6),
		Line(x3, x7),

		
		Line(x8, x0),
		Line(x9, x1),
		Line(x10, x2),
		Line(x11, x3),
		Line(x12, x4),
		Line(x13, x5),
		Line(x14, x6),
		Line(x15, x7),
		Line(x16, x0),
		Line(x17, x1),
		Line(x18, x5),
		Line(x19, x4), 
		Line(x20, x3),
		Line(x21, x2),
		Line(x22, x6),
		Line(x23, x7),
		Line(x24, x0),
		Line(x25, x3),
		Line(x26, x7),
		Line(x27, x4),
		Line(x28, x1),
		Line(x29, x2),
		Line(x30, x6),
		Line(x31, x5),

		Line(x32, x33),
		Line(x33, x34),
		Line(x34, x35),
		Line(x35, x32),
		Line(x36, x37),
		Line(x37, x38),
		Line(x38, x39),
		Line(x39, x36),
		Line(x40, x41),
		Line(x41, x42),
		Line(x42, x43),
		Line(x43, x40), 
		Line(x44, x45),
		Line(x45, x46),
		Line(x46, x47),
		Line(x47, x44),
		Line(x48, x49),
		Line(x49, x50),
		Line(x50, x51),
		Line(x51, x48),
		Line(x52, x53),
		Line(x53, x54),
		Line(x54, x55),
		Line(x55, x52),

		Line(x8, x32),
		Line(x9, x33),
		Line(x10, x34),
		Line(x11, x35),
		Line(x12, x36),
		Line(x13, x37),
		Line(x14, x38),
		Line(x15, x39),
		Line(x16, x40),
		Line(x17, x41),
		Line(x18, x42),
		Line(x19, x43), 
		Line(x20, x44),
		Line(x21, x45),
		Line(x22, x46),
		Line(x23, x47),
		Line(x24, x48),
		Line(x25, x49),
		Line(x26, x50),
		Line(x27, x51),
		Line(x28, x52),
		Line(x29, x53),
		Line(x30, x54),
		Line(x31, x55)]

figure1 = Figure(arr1, canv3D)
figure2 = Figure(arr2, canv3D)
flags.edit_flags("active", figure1)
print('_________')
flags.get_flag_value("active").draw()




"""
x5 = Point()
x6 = Point()
x7 = Point()
x8 = Point()

canv3D.draw_line(x4, x1)"""



#canv3D.draw_line(Point(-100, -110, 0), Point(-100, 100, 100))
#canv3D.draw_line(Point(-100, 100, -100), Point(100, 100, 0))
#canv3D.draw_line(Point(100, 100, 0), Point(100, -100, 0))
#canv3D.draw_line(Point(100, -100, 0), Point(-100, -100, 0))



canv.pack(side = LEFT)
btn_start.pack(pady=5, padx=5)
root.mainloop()
#___________#