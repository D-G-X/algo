import colorama
import time
from colorama import Fore,Back,Style

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class bfsMaze:
	def __init__(self, maze, start, destination):
		self.maze = maze 
		self.start = start
		self.destination = destination
		self.rowLen = len(maze)
		self.columnLen = len(maze[0])
		self.step = [ [0 for i in range(self.columnLen)]for i in range(self.rowLen)]
		self.solution = [ [0 for i in range(self.columnLen)]for i in range(self.rowLen)]
		# print(start.x,start.y)
		self.step[start.x][start.y] = 1
		self.solution[start.x][start.y] = 1
		self.solution[destination.x][destination.y] = 1

	def getStep(self):
		return self.step

	def getMaze(self):
		return self.maze

	def getSolution(self):
		return self.solution

	def makeStep(self,k):
		for i in range(self.rowLen):
			for j in range(self.columnLen):
				if self.step[i][j] == k:
					if i > 0 and self.step[i-1][j] == 0 and self.maze[i-1][j] == 0:
						self.step[i-1][j] = k + 1
					if j > 0 and self.step[i][j-1] == 0 and self.maze[i][j-1] == 0:
						self.step[i][j-1] = k + 1
					if i < self.rowLen-2 and self.step[i+1][j] == 0 and self.maze[i+1][j] == 0:
						self.step[i+1][j] = k+1
					if j < self.columnLen-2 and self.step[i][j+1] == 0 and self.maze[i][j+1] == 0:
						self.step[i][j+1] = k+1

	def printMatrix(self,maze):
		for i in range(self.rowLen):
			for j in range(self.columnLen):
				print(str(maze[i][j]).ljust(2),end=" ")
			print()
		print("\n\n")

	def printMaze(self):
		for i in range(self.rowLen):
			for j in range(self.columnLen):
				if self.maze[i][j] == 1:
					print(Fore.RED+str(self.maze[i][j]).ljust(2),end=" ")
				else:
					print(Fore.WHITE+str(self.maze[i][j]).ljust(2),end=" ")
			print(Style.RESET_ALL)
			# print()
		print("\n\n")

	def printStep(self):
		for i in range(self.rowLen):
			for j in range(self.columnLen):
				if self.step[i][j] == 0:
					print(Fore.RED+str(self.step[i][j]).ljust(2),end=" ")
				else:
					print(Fore.WHITE+str(self.step[i][j]).ljust(2),end=" ")
			print(Style.RESET_ALL)
			# print()
		print("\n\n")

	def printSolution(self):
		for i in range(self.rowLen):
			for j in range(self.columnLen):
				if self.solution[i][j] == 0:
					print(Fore.RED+str(self.solution[i][j]).ljust(2),end=" ")
				else:
					print(Fore.WHITE+str(self.solution[i][j]).ljust(2),end=" ")
			print(Style.RESET_ALL)
			# print()
		print("\n\n")


	def makePath(self):
		i = self.destination.x
		j = self.destination.y
		k = self.step[i][j]
		while k > 1:
			if i > 0 and self.step[i-1][j] == k-1:
				i -= 1
				self.solution[i][j] = 1
				k-=1
			elif j > 0 and self.step[i][j-1] == k-1:
				j -= 1
				self.solution[i][j] = 1
				k-=1
			elif i < self.rowLen-1 and self.step[i+1][j] == k-1:
				i += 1
				self.solution[i][j] = 1
				k-=1
			elif j < self.columnLen-1 and self.step[i][j+1] == k-1:
				j += 1
				self.solution[i][j] = 1
				k-=1

	def solveMaze(self):
		print("THE MAZE:")
		self.printMaze()
		k=0
		while self.step[end.x][end.y] == 0:
			k+=1
			self.makeStep(k)
			self.printStep()
			time.sleep(1)
		print("THE STEPS:")
		self.printStep()
		self.makePath()
		print("THE SOLUTION:")
		self.printSolution()






a = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
start = Point(1,1)
end = Point(2,5)

bfsMaze1 = bfsMaze(a,start,end)
bfsMaze1.solveMaze()

