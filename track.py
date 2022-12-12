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
	def __init__(self, width, height, start, finish, barriers=None, checks=None, solution=None):
		if barriers == None:
			barriers = []

		if checks == None:
			checks = []

		if solution == None:
			solution = []

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

		self.caminho = [ (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (2,7), (2,6), (2,5), (2,4), (3,5), (3,6), (3,7), (2,8), (2,9), (3,8), (4,7), (4,8), (4,9), (4,10), (4,11), (4,12), (5,11), (5,10), (5,9), (5,8), (6,9), (6,10), (6,11), (5,12), (6,12)]

		self.solution = []
		for x in range(len(self.caminho) - 1):
			diff = height - self.caminho[x][0] + 1
			diff2 = height - self.caminho[x+1][0] + 1
			p0 = Point(self.caminho[x][1], diff)
			p1 = Point(self.caminho[x+1][1], diff2)
			self.solution.append(LineSegment(p0, p1))

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

	def checkCollision(self, move):
		for barrier in self.barriers:
			p = move & barrier
			if p:
				raise CollisionError(move, barrier, p)
