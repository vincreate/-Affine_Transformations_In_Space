from math import cos, sin, acos, atan, sqrt, fabs
from numpy import arctan2

class Flags(object):
	"""docstring for Flags"""
	def __init__(self):
		super(Flags, self).__init__()
		self.arr = {}


	def edit_flags(self, key, value):
		self.arr[key] = value
	def get_flag_value(self, key):
		return self.arr[key]

class Point(object):
	"""docstring for Point"""
	def __init__(self, X, Y, Z):
		super(Point, self).__init__()
		
		self.X = X
		self.Y = Y
		self.Z = Z
		
		

	def set(self, X, Y):
		self.X = X
		self.Y = Y
		self.Z = Z

	def get(self):
		return [self.X, self.Y, self.Z]

def p_add_p(p1, p2):
	x1, y1, z1 = p1.get()
	x2, y2, z2 = p2.get()
	return Point(x1+x2, y1+y2, z1+z2)
		
class Line(object):
	"""docstring for Line"""
	def __init__(self, p1, p2):
		super(Line, self).__init__()
		self.p1 = p1
		self.p2 = p2

	def get(self):
		return [self.p1, self.p2]

class Canvas3D(object):
	"""docstring for Canvas3D"""
	def __init__(self, canvas, C):
		super(Canvas3D, self).__init__()
		self.canvas = canvas
		self.C = C

	def draw_line(self, p1, p2):

		a, b, c = self.C.get()
		p1_x, p1_y, p1_z = p1.get()
		p2_x, p2_y, p2_z = p2.get()

		A_x = p1_x * (c/(c - p1_z)) + a
		A_y = p1_y * (c/(c - p1_z)) + b

		B_x = p2_x * (c/(c - p2_z)) + a
		B_y = p2_y * (c/(c - p2_z)) + b
		self.canvas.create_line(A_x, A_y, B_x, B_y)


def distance(p1, p2):
	x1, y1, z1 = p1.get()
	x2, y2, z2 = p2.get()
	return sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1) + (z2-z1) * (z2-z1))

def turnX_(p, al):
	t = 3.14159265359/180
	x, y, z = p.get()
	x1 = x
	y1 = y*cos(al*t) - z*sin(al*t)
	z1 = y*sin(al*t) + z*cos(al*t)
	return Point(x1, y1, z1)


def turnY_(p, al):
	t = 3.14159265359/180
	x, y, z = p.get()
	x1 = x*cos(al*t) + z*sin(al*t)
	y1 = y
	z1 = x*sin(al*t) + z*cos(al*t)
	return Point(x1, y1, z1)


def turnZ_(p, al):
	t = 3.14159265359/180
	x, y, z = p.get()
	x1 = x*cos(al*t)-y*sin(al*t)
	y1 = x*sin(al*t)+y*cos(al*t)
	z1 = z
	return Point(x1, y1, z1)

def turnXYZ(p, p_al):

	alX, alY, alZ = p_al.get()
	return turnZ_(turnY_(turnX_(p, alX), alY), alZ)



class Figure(object):
	"""docstring for Figure2"""
	def __init__(self, arg, canv3D):
		super(Figure, self).__init__()
		self.arg = arg
		self.XYZ = Point(0, 0, 0)

		self.rotate = Point(0, 0, 0)
		

		self.canv3D = canv3D

	def move(self, p):
		self.XYZ = p_add_p(self.XYZ, p)

	def turn(self, p):
		self.rotate = p_add_p(self.rotate, p)
		
	def draw(self):
		for x in self.arg:
			p1, p2 = x.get()

			self.canv3D.draw_line(turnXYZ(p_add_p(p1, self.XYZ), self.rotate) , turnXYZ(p_add_p(p2, self.XYZ), self.rotate))
		