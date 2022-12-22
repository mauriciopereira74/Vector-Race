from numbers import Integral
from numbers import Real
from collections import namedtuple

class Point(namedtuple('Point', ['x', 'y'])):
	def __new__(cls, x, y):
		if not isinstance(x, Real) or not isinstance(y, Real):
			raise TypeError("Point coordinates must be real numbers.")
		return super(Point, cls).__new__(cls, x, y)

	def __eq__(self, other):
		if isinstance(other, Point):
			for (s, o) in zip(self, other):
				if s != o:
					return False
				else:
					return True
		else:
			return NotImplemented

	def __ne__(self, other):
		if isinstance(other, Point):
			for (s, o) in zip(self, other):
				if s != o:
					return True
				else:
					return False
			else:
				return NotImplemented

	def __add__(self, other):
		if isinstance(other, Vector):
			return Point._make(map(sum, zip(self, other)))
		else:
			return NotImplemented

	def __sub__(self, other):
		if isinstance(other, Vector):
			return self + -other
		elif isinstance(other, Point):
			return Vector._make([(s - o) for (s, o) in zip(self, other)])
		else:
			return NotImplemented

	def isIntegral(self):
		for c in self:
			if not c == int(c):
				return False
			else:
				return True

class LineSegment(object):
    def __init__(self, p0, a):
        if isinstance(p0, Point):
            self.p0 = p0
        else:
            raise TypeError("start point must be a Point.")
        if isinstance(a, Point):
            self.p1 = a
        elif isinstance(a, Vector):
            self.p1 = p0 + a
        else:
            raise TypeError("a must be a Point or a Vector.")

    def __repr__(self):
        return "LineSegment(%s, %s)" % (self.p0, self.p1)

    def __eq__(self, other):
        """self == other."""
        if isinstance(other, LineSegment):
            return self.p0 == other.p0 and self.p1 == other.p1
        else:
            return NotImplemented

    def __ne__(self, other):
        """self != other."""
        if isinstance(other, LineSegment):
            return self.p0 != other.p0 or self.p1 != other.p1
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.p0) ^ hash(self.p1)

    def __and__(self, other):
        u = self.getVector()
        v = other.getVector()
        w = other.p1 - self.p0
        d = u.x * v.y - v.x * u.y
        r = w.x * v.y - v.x * w.y
        q = u.x * w.y - w.x * u.y
        if d != 0:
            t = r / d
            s = q / d
            if 0.0 <= t <= 1.0 and 0.0 <= s <= 1.0:
                return self.p0 + t * u
            else:
                return None
        else:
            if r != 0 or q != 0:
                return None
            elif u.norm1() != 0:
                w0 = other.p0 - self.p0
                w1 = other.p1 - self.p0
                t = w0.x / u.x if u.x != 0 else w0.y / u.y
                s = w1.x / u.x if u.x != 0 else w1.y / u.y
                if (t < 0.0 and s < 0.0) or (t > 1.0 and s > 1.0):
                    return None
                elif (t < 0.0 <= s) or (s < 0.0 <= t):
                    return self.p0
                elif t <= s:
                    return other.p0
                else:
                    return other.p1
            elif v.norm1() != 0:
                w0 = self.p0 - other.p0
                t = w0.x / v.x if v.x != 0 else w0.y / v.y
                if 0.0 <= t <= 1.0:
                    return self.p0
                else:
                    return None
            elif w.norm1() != 0:
                return None
            else:
                return self.p0

    def getVector(self):
        return self.p1 - self.p0

    def isIntegral(self):
        return self.p0.isIntegral() and self.p1.isIntegral()

class Track(object):
	def __init__(self, width, height, start, finish, barriers=None, checks=None, path1=None, path2=None, alg1=None, alg2=None, custo1=None, custo2=None, collisions=None):
		if barriers == None:
			barriers = []

		if checks == None:
			checks = []

		if path1 == None:
			path1 = []

		if path2 == None:
			path2 = []

		if alg1 != None:
			self.alg1 = alg1

		if alg2 != None:
			self.alg2 = alg2

		if custo1 != None:
			self.custo1 = custo1

		if custo2 != None:
			self.custo2 = custo2
		
		if collisions != None:
			self.collisions = collisions
		else:
			self.collisions = []

		self.width = width
		self.height = height
		self.start = start
		self.finish = finish
		p0 = Point(x = 0, y = 0)
		p1 = Point(x = width+1, y = 0)
		p2 = Point(x = width+1, y = height+1)
		p3 = Point(x = 0, y = height+1)

		# add borders of the track as barriers
		self.barriers = [LineSegment(p0, p1), LineSegment(p1, p2), 
						 LineSegment(p2, p3), LineSegment(p3, p0)]
		self.addBarriers(barriers)
		self.checks = checks

		self.solution1 = []
		for x in range(len(path1) - 1):
			diff = height - eval(path1[x])[0] + 1
			diff2 = height - eval(path1[x+1])[0] + 1
			p0 = Point(eval(path1[x])[1], diff)
			p1 = Point(eval(path1[x+1])[1], diff2)
			self.solution1.append(LineSegment(p0, p1))

		self.solution2 = []
		for x in range(len(path2) - 1):
			diff = height - eval(path2[x])[0] + 1
			diff2 = height - eval(path2[x+1])[0] + 1
			p0 = Point(eval(path2[x])[1], diff)
			p1 = Point(eval(path2[x+1])[1], diff2)
			self.solution2.append(LineSegment(p0, p1))
	
	def addBarriers(self, barriers):
		self.barriers.extend(barriers)

	def bbox(self):
		xmin = None
		xmax = None
		ymin = None
		ymax = None
		for l in self.barriers:
			for p in (l.p0, l.p1):
				if xmin is None or p.x < xmin:
					xmin = p.x
				if xmax is None or p.x > xmax:
					xmax = p.x
				if ymin is None or p.y < ymin:
					ymin = p.y
				if ymax is None or p.y > ymax:
					ymax = p.y
		return (xmin, ymin, xmax, ymax)
