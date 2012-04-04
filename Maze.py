# Written by Cate Miller and Sam Keller on April 15th, 2011
#
# Maze.py
#
# This program imports the Cell and Grid classes from the Grid.py file to make a grid of a 
# dimension specified by the user. Then, using the makePath function defined below, this program
# chooses randomly from its four neighbors and moves there. If the neighbor has already been visited,
# the function goes back a level and tries another neighbor. If the neighbor hasn't been visited,
# the wall between it and the previous cell is broken down. Each cell has a south and an east wall 
# associated with it so when we take down walls, we either taken down the current cell's east or 
# south wall or the previous cell's south or east wall. It eventually reaches every part of the 
# grid so that every space is connected to the rest of the maze. By putting in a starting point
# on the top left and an ending point on the bottom right, we have a complete maze!

from Grid import *
import random

def makePath(grid,prev,row,col):
	""" First checks to see if the current cell has been visited. If it has, it gets out. If it 
	hasn't, it takes down the wall between the current cell and the previous cell, helping to make
	the maze. Then, it checks the current neighbors and recurses!"""
	#print row,col,prev
	current = grid[row][col]
	if current.getVisited():
		return
	if row == prev[0] and (col-prev[1])<0:
		# We just moved up so we want to delete current's south wall
		current.deleteEast()
	elif row == prev[0] and (col-prev[1])>0:
		# We just moved down so we want to delete previous's south wall	
		grid[prev[0]][prev[1]].deleteEast()
	elif col == prev[1] and (row-prev[0])<0:
		# We just moved left so we want to delete current's east wall
		current.deleteSouth()
	elif col == prev[1] and (row-prev[0])>0:
		# We just moved right so we want to delete previous's east wall
		grid[prev[0]][prev[1]].deleteSouth()
	neighbors = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
	random.shuffle(neighbors)
	index = 0
	current.setVisited(True)
	for nrow,ncol in neighbors:
		# Check through the neighbors and recurse!
		prev = [row,col]
		makePath(grid,prev,nrow,ncol)
	
def main():
	"""The main part of the program. The user specifies how large the maze should be (it's a
	square maze)."""
	response = int(raw_input('What dimension do you want your grid to have? Enter 2-44: '))
	M = Grid(response)
	makePath(M,[None,None],random.randint(0,response),random.randint(0, response))	
	print M

main()