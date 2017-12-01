from instruction_loader import instruction_loader
from instruction import Instruction
from controller import Controller

class python_risc_v_simulator():
	"""docstring for ClassName"""
	def __init__(self, instruction_set):
		super(python_risc_v_simulator, self).__init__()
		self.instruction_set = instruction_set
		self.controller = Controller(instruction_set)

	def instructions_executer(self):
		terminated = False

		while self.controller.pc < len(self.instruction_set):
			print(self.controller.reg)
			instruction = Instruction(self.controller)
			self.controller = instruction.execute()
			print(self.controller.reg)
			print()
		print("program terminated")
			

if __name__ == '__main__':
	instruction_loader = instruction_loader()
	
	instruction_set = instruction_loader.load_from_file('test_instruction_1.txt')

	python_risc_v_simulator = python_risc_v_simulator(instruction_set)
	python_risc_v_simulator.instructions_executer()