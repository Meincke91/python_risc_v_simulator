class Controller(object):
	"""docstring for ClassName"""
	def __init__(self, instruction_set):
		super(Controller, self).__init__()
		self.pc = 0
		self.reg = [0] * 32
		self.instruction_set = instruction_set
		
	def get_instruction(self):
		return self.instruction_set[self.pc]

	def increment_pc(self):
		self.pc = self.pc + 1
		return self

	def set_pc(self, pc):
		self.pc = pc
		return self

	def set_reg(self, reg):
		self.reg = reg
		return self