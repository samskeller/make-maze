# Written by Cate Miller and Sam Keller on April 15th, 2011
#
# Grid.py
#
# This file contains the two classes that are used in the Maze.py program to make a randomly
# generated maze. The Cell class makes a cell that has an south wall, an east wall, and a value
# for visited that is either equal to true or false. The Grid class makes a grid for the maze as
# a starting point with a bunch of dummy cells that are already marked as visited around the real 
# cells.

class Cell():
	""" Creates a cell in the maze with a south and east wall as well as a value of visited. To
	delete a wall, we simply set the south or east wall equal to 'x' so that it doesn't print
	in the Maze.py file"""
	def __init__(self,south,east,visited=False):
		self.south = south
		self.east = east
		self.visited = visited
	def getVisited(self):
		return self.visited
	def setVisited(self,visited):
		self.visited = visited
	def getEast(self):
		return self.east
	def getSouth(self):
		return self.south
	def deleteEast(self):
		self.east = 'x'
	def deleteSouth(self):
		self.south = 'x'
		

class Grid(list):
	"""Creates a grid for our maze to start from. A set of dummy cells are created around the 
	real cells to make things easier to use-- these cells have a southa east wall value of 'x' so
	that they don't print at the end and they also have their visited value equal to false"""
	def __init__ (self, size):
		list.__init__(self)
		self.size = size + 2
		self.row = None
		self.col = None
		for i in range(self.size):
			row = []
			if i == 0 or i == self.size-1:
				for j in range(self.size):
					row.append(Cell('x','x',True))
			else:
				for j in range(self.size):
					if j == 0 or j == self.size-1:
						row.append(Cell('x','x',True))
					else:
						row.append(Cell('s','e',False))
			self.append(row)
		
	# with dummy borders
	def __str__(self):
		""" convert maze into a nice text string so can print"""
	
	# the bottom-right corner is now at [-2][-2] because of the dummy-node border
		#self.grid[-2][-2].remove('s')
	
	# in this Maze class we keep a size variable with the grid's true size 
	# including the dummy borders, but we don't want to print those borders,
	# just the actual maze cells
		retstr = '   '+'___'*(self.size-3)+'\n'
		for i in range(1,self.size-1):
			s="|"
			self[self.size-2][self.size-2].deleteSouth()
			for j in range(1,self.size-1):
				if 's' in self[i][j].getSouth():
					s += '___'
				else:
					s += '   '
				if 'e' in self[i][j].getEast():
					s = s[:-1]+'|' 
			retstr += s + '\n'
		return retstr
	
if __name__=="__main__":
	response = int(raw_input('What dimension do you want your grid to have? Enter 2-44: '))
	M = Grid(response)
	print M