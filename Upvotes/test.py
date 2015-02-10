class Test:
	def __init__(self):
		self.n = 12
		self.dict = {'1':3}

	def change_me(self):
		self.change(self.n, self.dict)
	
	def change(self,n,dict):
		n.__radd__(1)
		dict[4] = 'bla'
t = Test()
t.change_me()
print t.n
print t.dict


