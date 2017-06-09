class CreateTriangles(object):
	"""Create triangles inside triangles"""
	def __init__(self, size, spacer=' '):
		self.size = size
		self.col_count = size + (size - 1)
		self.row_count = size
		# matrix when printed draws all triangles
		self.print_matrix = []
		# current mark
		self.typo = '*'
		self.spacer = spacer
		# params to update with each new triangle
		self.params = {
			'offset_row' : 0,
			'offset_col' : 0,
			'size' : size,
			# what side next triangle is going to be
			'side' : 'up'
		}
		# initialize matrix
		self.init_matrix()

	def init_matrix(self):
		# total base size of any triangle
		for rows in range(self.row_count):
			curr_matrix = [self.spacer] * self.col_count
			self.print_matrix.append(curr_matrix)

	def run(self):
		# draw main triangle first
		self.up_triangle()
		self.calculate_next_params()
		while self.params['size'] >= 2:
			getattr(self, '{0}_triangle'.format(self.params['side']))()
			self.calculate_next_params()
		self.display_triangles()
		print '\n\n \t\t- size {0}, Happy Codding \n\n'.format(self.size)

	def swap_typo(self):
		if self.typo == '*':
			self.typo = '#'
		else:
			self.typo = '*'

	def up_triangle(self, size=None, offset_row=0, offset_col=0):
		size = self.params['size']
		offset_col = self.params['offset_col']
		offset_row = self.params['offset_row']
		mark1 = None
		mark2 = None
		for row in range(offset_row, offset_row + size):
			if row == offset_row:
				# first row just 1 astrik
				self.print_matrix[row][offset_col + size - 1] = self.typo
				mark1 = offset_col + size - 1 - 1
				mark2 = offset_col + size
			elif row == (offset_row + size - 1):
				# base of triangle
				flag = True
				for i in range(offset_col, offset_col + size + (size-1)): # base of self.typo and ' '
					if flag:
						self.print_matrix[row][i] = self.typo
						flag = not flag
					else:
						flag = not flag
			else:
				self.print_matrix[row][mark1] = self.typo
				self.print_matrix[row][mark2] = self.typo
				mark1 -= 1
				mark2 += 1
		self.swap_typo()

	def down_triangle(self, size=None, offset_row=0, offset_col=0):
		size = self.params['size']
		offset_col = self.params['offset_col']
		offset_row = self.params['offset_row']
		mark1 = None
		mark2 = None
		for row in range(offset_row-1, offset_row + size -1):
			if row == (size -1):
				# last row just 1 astrik
				self.print_matrix[row][size - 1] = self.typo
			elif row == offset_row - 1:
				# base of triangle
				flag = True
				for i in range(offset_col, offset_col + size + (size-1)): # base of self.typo and ' '
					if flag:
						self.print_matrix[row][i] = self.typo
					flag = not flag
				# set marks
				mark1 = offset_col + 1
				mark2 = offset_col + (2 * size) - 3
			else:
				self.print_matrix[row][mark1] = self.typo
				self.print_matrix[row][mark2] = self.typo
				mark1 += 1
				mark2 -= 1
		self.swap_typo()


	def calculate_next_params(self):
		# calculate all offsets and next size
		next_size = self.params['size'] / 2

		if self.params['side'] == 'up':
			# next side is down inside an up
			if self.params['size'] % 2 == 1:
				self.params['offset_col'] += next_size + 1
			else :
				self.params['offset_col'] += next_size

			self.params['size'] = next_size
			self.params['offset_row'] += next_size + 1
			
			self.params['side'] = 'down'
		else:
			# next side is up in side a down
			if self.params['size'] % 2 == 1:
				# 
				# this is odd number 3, 9, ...
				self.params['offset_col'] += (next_size + 1)
				self.params['size'] = next_size
				self.params['side'] = 'up'
			else: 
				# this is even number triangle
				self.params['offset_row'] -= 1
				self.params['offset_col'] += next_size
				self.params['size'] = next_size
				self.params['side'] = 'up'


	def display_triangles(self):
		for row in range( self.row_count ):
			print ''.join([ str(x) for x in self.print_matrix[row] ] )

if __name__ == '__main__':
	while True:
		print '\n1. Choose size of triangle\n2. Choose range of sizes for multiple triangles\n3. Exit'
		choice = input('>> ')
		if choice == 1:
			size = input('Enter size of triangle >> ')
			if size < 1:
				print 'Invalid size'
			else:
				tr = CreateTriangles(size)
				tr.run()

		elif choice == 2:
			size1 = input('Enter start of range >> ')
			size2 = input('Enter end of range >> ')
			for size in range(size1, size2+1):
				tr = CreateTriangles(size)
				tr.run()

		elif choice == 3:
			break

		else:
			print "Wrong Choice"
	
