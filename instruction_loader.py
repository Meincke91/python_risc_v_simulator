class instruction_loader:
	"""docstring for ClassName"""
	def remove_comments(self, text_instruction):
		return text_instruction.split('//')[0]

	def remove_comma_and_space(self, text_instruction):
		return text_instruction.split(', ')[0]

	def load_from_file(self, file_name):
		instruction_set = []
		with open(file_name, 'r') as f:
			for instruction in f:
				instruction_code = int(self.remove_comments(self.remove_comma_and_space(instruction)), 0)
				instruction_set.append(instruction_code)
		return instruction_set
		