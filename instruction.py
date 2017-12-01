class Instruction():
	"""docstring for ClassName"""
	def __init__(self, controller):
		super(Instruction, self).__init__()
		self.controller = controller

	def execute(self):
		print("executing, pc: %s" % (self.controller.pc))
		instruction = self.controller.get_instruction()

		opcode_delegate = {
           	0x3 : self.i_type_decode_3,
           	0xf : self.i_type_decode_f,
           	0x13 : self.i_type_decode_13,
           	0x17 : self.u_type_decode_17,
           	0x1b : self.i_type_decode_1b,
           	0x23 : self.s_type_decode_23,
           	0x33 : self.r_type_decode_33,
           	0x37 : self.u_type_decode_37,
           	0x3b : self.r_type_decode_3b,
           	0x63 : self.sb_type_decode_63,
           	0x67 : self.i_type_decode_67,
           	0x6f : self.uj_type_decode_6f,
           	0x73 : self.i_type_decode_73
		}

		opcode_delegate[instruction & 0x7f](instruction)

		print("finished executing, pc: %s" % (self.controller.pc))
		return self.controller

	'''
	I-type
	'''
	def i_type_decode_3(self, instruction):
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		imm = (0xfff00000 & instruction) >> 20

		i_type_delegate = {
			0x0 : self.i_lb,
			0x1 : self.i_lh,
			0x2 : self.i_lw,
			0x3 : self.i_ld,
			0x4 : self.i_lbu,
			0x5 : self.i_lhu,
			0x6 : self.i_lwu
		}

		i_type_delegate[funct3](imm, rs1, rd)

	def i_type_decode_f(self, instruction):
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		imm = (0xfff00000 & instruction) >> 20

		i_type_delegate = {
			0x0 : self.i_fence,
			0x1 : self.i_fence_i
		}

		i_type_delegate[funct3](imm, rs1, rd)

	def i_type_decode_13(self, instruction):
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		imm = (0xfff00000 & instruction) >> 20

		i_type_delegate = {
			(0x0, 0x0) : self.i_addi,
			(0x1, 0x0) : self.i_addi,
			(0x2, 0x0) : self.i_addi,
			(0x3, 0x0) : self.i_addi,
			(0x4, 0x0) : self.i_addi,
			(0x5, 0x0) : self.i_addi,
			(0x5, 0x20) : self.i_addi,
			(0x6, 0x0) : self.i_addi,
			(0x7, 0x0) : self.i_addi
		}

		i_type_delegate[funct3](imm, rs1, rd)

	def i_type_decode_1b(self, instruction):
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		imm = (0xfff00000 & instruction) >> 20

		i_type_delegate = {
			(0x0,0x0) : self.i_addi,
			(0x1,0x0) : self.i_addi,
			(0x5,0x0) : self.i_addi,
			(0x5,0x20) : self.i_addi
		}

		i_type_delegate[funct3](imm, rs1, rd)

	def i_type_decode_67(self, instruction):
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		imm = (0xfff00000 & instruction) >> 20

		i_type_delegate = {
			0x0 : self.i_jalr
		}

		i_type_delegate[funct3](imm, rs1, rd)

	def i_type_decode_73(self, instruction):
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		imm = (0xfff00000 & instruction) >> 20

		i_type_delegate = {
			(0x0,0x0) : self.i_ecall,
			(0x0,0x1) : self.i_ebreak,
			(0x1,0x0) : self.i_csrrw,
			(0x2,0x0) : self.i_csrrs,
			(0x3,0x0) : self.i_csrrc,
			(0x5,0x0) : self.i_csrrwi,
			(0x6,0x0) : self.i_csrrsi,
			(0x7,0x0) : self.i_csrrci
		}

		i_type_delegate[funct3](imm, rs1, rd)

	def i_lb(self, imm, rs1, rd):
		pass

	def i_lh(self, imm, rs1, rd):
		pass

	def i_lw(self, imm, rs1, rd):
		pass

	def i_lbu(self, imm, rs1, rd):
		pass

	def i_lhu(self, imm, rs1, rd):
		pass

	def i_lwu(self, imm, rs1, rd):
		pass

	def i_addi(self, imm, rs1, rd):
		b = self.controller.reg[rs1] 
		print("addi instruction, sum: %s" % (imm + b) )

		self.controller.reg[rd] = imm + b
		self.controller.increment_pc()
		print(self.controller.pc)
		return self.controller

	def i_slli(self, imm, rs1, rd):
		pass

	def i_xori(self, imm, rs1, rd):
		pass

	def i_srli(self, imm, rs1, rd):
		pass

	def i_sraj(self, imm, rs1, rd):
		pass

	def i_ori(self, imm, rs1, rd):
		pass

	def i_andi(self, imm, rs1, rd):
		pass

	def i_jalr(self, imm, rs1, rd):
		pass

	'''
	R-type
	'''
	def r_type_decode_33(self, instruction):
		#print("r type decode %s " % (instruction))
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		rs2 = (0x1f00000 & instruction) >> 20
		funct7 = (0xfe000000 & instruction) >> 25

		r_type_delegate = {
			(0x0, 0x0) : self.r_add,
			(0x0, 0x20) : self.r_sub,
			(0x1, 0x0) : self.r_sll,
			(0x2, 0x0) : self.r_slt,
			(0x3, 0x0) : self.r_sltu,
			(0x4, 0x0) : self.r_xor,
			(0x5, 0x0) : self.r_srl,
			(0x5, 0x20) : self.r_sra,
			(0x6, 0x0) : self.r_or,
			(0x7, 0x0) : self.r_and,
		}

		r_type_delegate[(funct3, funct7)](rs2, rs1, rd)

	def r_type_decode_3b(self, instruction):
		#print("r type decode %s " % (instruction))
		rd = (0xf80 & instruction) >> 7
		funct3 = (0x7000 & instruction) >> 12
		rs1 = (0xf8000 & instruction) >> 15
		rs2 = (0x1f00000 & instruction) >> 20
		funct7 = (0xfe000000 & instruction) >> 25

		r_type_delegate = {
			(0x0, 0x0) : self.r_addw,
			(0x0, 0x20) : self.r_subw,
			(0x1, 0x0) : self.r_sllw,
			(0x5, 0x0) : self.r_srlw,
			(0x5, 0x20) : self.r_sraw,
		}

		r_type_delegate[(funct3, funct7)](rs2, rs1, rd)

	def r_add(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1]  + self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_sub(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1]  - self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_sll(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1] << self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_xor(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1] ^ self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_srl(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1] >> self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_sra(self, rs2, rs1, rd):
		print("sra not yet implemented")
		pass

	def r_or(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1] | self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_and(self, rs2, rs1, rd):
		self.controller.reg[rd] = self.controller.reg[rs1] & self.controller.reg[rs2]
		self.controller.increment_pc()
		return self.controller

	def r_lr_d(self, rs2, rs1, rd):
		print("lr_d not yet implemented")
		pass

	def r_sc_d(self, rs2, rs1, rd):
		print("sc_d not yet implemented")
		pass

	'''
	S-Type
	'''
	def s_type_decode(self, instruction):
		print(instruction)

	def s_sb(self, pc):
		pass

	def s_sh(self, pc):
		pass

	def s_sw(self, pc):
		pass

	def s_sd(self, pc):
		pass

	'''
	SB-Type
	'''
	def sb_type_decode(self, instruction):
		print(instruction)

	def sb_beq(self, pc):
		pass

	def sb_bne(self, pc):
		pass

	def sb_blt(self, pc):
		pass

	def sb_bge(self, pc):
		pass

	def sb_bltu(self, pc):
		pass

	def sb_bgeu(self, pc):
		pass

	'''
	U-Type
	'''
	def u_type_decode(self, instruction):
		print(instruction)

	def u_lui(self, pc):
		pass

	'''
	UJ-Type
	'''
	def uj_type_decode(self, instruction):
		print(instruction)

	def uj_jal():
		pass

	'''
	Util functions
	'''
	def hex_to_binary(self, hex_data):
		return bin(hex_data)[2:].zfill(32)

	def int_to_binary(self, int_data):
		return bin(int_data)[2:].zfill(32)

class R_type():
	"""docstring for ClassName"""
	def __init__(self, instruction):
		self.rd = 0xf80 & instruction
		self.funct3 = 0x7000 & instruction
		self.rs1 = 0xf8000 & instruction
		self.rs2 = 0x1f00000 & instruction
		self.funct7 = 0xfe000000 & instruction

class I_type():
	"""docstring for ClassName"""
	def __init__(self, imm, rs1, funct3, rd):
		self.imm = imm
		self.rs1 = rs1
		self.funct3 = funct3
		self.rd = rd


