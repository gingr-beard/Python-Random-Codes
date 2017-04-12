'''
classes for cartisian geomety
class point():
	att:[x,y]
	meth:[__str__, __add__, translate, dso, dfp]

'''

class Point():
	"""A point in XY plane"""
	def __init__(self, x=0, y=0):
		#initialise to origin if no values are given
		self.x=x
		self.y=y
	
	def __str__(self):
		'''string representation of point'''
		return '({},{})'.format(self.x, self.y)
	
	def __add__(self, point):
		'''adding 2 points, returns sum as a new point'''
		res=Point(self.x,self.y)
		if isinstance(point, Point):
			return (res+point.x),(res.y+point.y)
		elif isinstance(point, tuple):
			return (res.x+point[0], res.y+point[1])
	
	def dfo(self):
		'''claculates distance to the origin'''
		return (abs(self.x**2 - self.y**2))**0.5
	
	def dfp(self, point):
		'''calculated the distance to another point'''
		try:
			a,b= point.x, point.y
		except:
			print("Argument must be a point object")
		
		dx, dy=abs(a-self.x), abs(b-self.y)
		return (abs(dx**2 - dy**2))**0.5
	
	def cords(self):
		"""returns a tuble of x-y co-ordinates of the point"""
		return (self.x, self.y)
	
	def translate(self, dx,dy):
		"""moves the point by dx, dy"""
		self.x+= dx
		self.y+=dy
		return 'new co-ords: {}'.format(self.__str__())


class Polygon():
	"""A class describing general traits of polygons in x-y plane
	contains within_range methods"""
	
	def within_range(self, point=Point(5,5), x_range=(0,10), y_range=(0,10)):
		'''returns True if a given point is within the polygon's x-y ranges'''
		x1,x2=x_range[0], x_range[1]
		y1,y2= y_range[0], y_range[1]
		
		try:
			return x1<point.x<x2 and y1<point.y<y2
		except:
			print("point must be a Point object, ranges must be tuples") 


class Circle(Polygon):
	"""A point in XY plane, defined by radius, center point(point object)"""
	pi=22.0/7
	def __init__(self, r=1, cx=0, cy=0):
		#initailise as a unit circle
		self.r=r
		self.cen=Point(x=cx, y=cy)
	
	def circ(self):
		#claculates the circumference of the circle
		return 2*self.pi*self.r
	
	def area(self):
		#calculates the area of the circle
		return self.pi*(self.r)**2
	
	def inside(self,point):
		#returns True if the gien point is inside the circle
		try:
			dfc=point.dfp(self.cen)
		except:
			print("argument must be a point object")
		
		return dfc <= self.r
	
	def x_part(self):
		#returns the part of X-Axis occupied by the circle
		return (self.cen.x-self.r, self.cen.x+self.r)
	
	def y_part(self):
		#returns the part of Y-Axis occupied by the circle
		return (self.cen.y-self.r, self.cen.y+self.r)
	
	def overlap(self, polygon):
		#returns true if the circle overlaps with the given polygon
		#the polygon must have the x_part, y_part methods
		try:			
			x1,x2=polygon.x_part()[0], polygon.xpart()[1]
			y1,y2=polygon.y_part()[0], polygon.y_part()[1]
		except:
			print("Polygon must have x_part, y_part methods")
		
		a1,a2=self.x_part()[0], self.x_part()[1]
		b1,b2=self.y_part()[0], self.y_part()[1]
		
		x_over= lambda: (x1<a1<x2) or (a1<x1<a2)
		y_over= lambda: (y1<b1<y2) or (b1<y1<b2)
		
		return (x_over() and y_over())
		
	

class Rect(Polygon):
	"""A rectangle in XY plane defined by length, hight, lower-left corner(point object)
	The corners are named A,B,C,D starting at the lower-left corner and going counter-clock wise
	"""
	def __init__(self,len=1,hight=1,cx=-0.5, cy=-0.5):
		self.len=len
		self.hight=hight
		self.a=Point(cx, cy)
		self.b=Point(cx+self.len, cy)
		self.c=Point(cx+self.len, cy+self.hight)
		self.d=Point(cx, cy+self.hight)
		self.cen=Point(cx+self.len/2, cy+self.hight/2)
	
	def area(self):
		#calculates the area of the rectangle
		return self.len*self.hight/2
	
	def circ(self):
		#claculates the circumference
		return (self.len+self.hight)*2
	
	def x_part(self):
		return (self.a.x, self.b.x)
	
	def y_part(self):
		return (self.a.y, self.d.y)
	
	def inside(self,point):
		#returns True if a Point is inside the rectangle
		x1,x2=self.x_part()[0],self.x_part()[1]
		y1,y2=self.y_part()[0], self.y_part()[1]
		try:
			x,y=point.x, point.y
		except:
			print("Argument must be a Point object")
		return x1<x<x2 and y1<y<y2
	
	
	def in_circle(self,circle):
		#returns True if any part of the rectangle is inside the given circle
		a=circle.cen
		return any(filter(a.inside,[self.a, self.b, self.c, self.d]))
	
	def overlap(self, polygon):
		#returns true if the circle overlaps with the given polygon
		#the polygon must have the x_part, y_part methods
		try:		
			x1,x2=polygon.x_part()[0], polygon.x_part()[1]
			y1,y2=polygon.y_part()[0], polygon.y_part()[1]
		except:
			print("Polygon must have x_part, y_part methods")
		
		a1,a2=self.x_part()[0], self.x_part()[1]
		b1,b2=self.y_part()[0], self.y_part()[1]
		
		x_over= lambda: (x1<a1<x2) or (a1<x1<a2)
		y_over= lambda: (y1<b1<y2) or (b1<y1<b2)
		
		return (x_over() and y_over())

"""
Test case
"""


p1=Point(0,0)
print(
p1,
p1+(1,1),
p1.translate(2,2)
)
print('-'*50)
circ=Circle(r=5, cx=0, cy=0)
box=Rect(5, 5, -2.5, -2.5)

print('Circle, area, circum, inside (3,4), x_part, y_part, in_range((3,4),x_part, y_part)\n',
circ.area(),
circ.circ(),
circ.inside(Point(3,4)),
circ.x_part(),
circ.y_part(),
circ.within_range(Point(3,4), circ.x_part(), circ.y_part()),
'\n\nRectangle, area, circum, nside (0,0), x_part, y_part, overlaps circle\n',
box.area(),
box.circ(),
box.inside(Point(0,0)),
box.x_part(),
box.y_part(),
box.overlap(circ),
'\n\nRectangle corners: top-right, top-left, bottom-right, bottom-left',
box.c.cords(), box.d.cords(), box.b.cords(), box.a.cords()

)
