from Core.Assembler import *


class VirtualMachine:
	def __init__(self):
		self.is_running = False
		self.max_memory = 1024 * 4
		self.memory = [ORG for index in range(self.max_memory)]
		self.pc     = ORG
		self.ac     = ORG
		self.dr     = ORG
		self.sp     = self.max_memory
		self.fp     = self.max_memory
		
	def load(self,dump = []):
		self.is_running = False
		self.pc = dump[1][1]
		loc = 2
		while loc < len(dump):
			value = dump[loc]
			self.memory[value[0]] = value[1]
			loc = loc + 1
	
	def push(self,value = 0):
		self.sp = self.sp - 1
		self.memory[self.sp] = value
		
	def pop(self):
		value = self.memory[self.sp]
		self.sp = self.sp + 1
		return value
		
	def execute(self):
		opcode = self.memory[self.pc]
		if opcode == HALT:
			self.is_running = False
		elif opcode == NOP:
			pass
		elif opcode == INP:
			self.ac = chr(int(input()))
			self.pc = self.pc + 1;
		elif opcode == OUT:
			print("{}".format(chr(self.ac)),end="")
			self.pc = self.pc + 1;
		elif opcode == SCAN:
			self.ac = int(input())
			self.pc = self.pc + 1;
		elif opcode == PRINT:
			print("{}".format(self.ac),end="")
			self.pc = self.pc + 1;
		elif opcode == ADD:
			self.ac = int(self.dr + self.ac)
			self.pc = self.pc + 1;
		elif opcode == SUB:
			self.ac = int(self.dr - self.ac)
			self.pc = self.pc + 1;
		elif opcode == MUL:
			self.ac = int(self.dr * self.ac)
			self.pc = self.pc + 1;
		elif opcode == DIV:
			self.ac = int(self.dr // self.ac)
			self.pc = self.pc + 1;
		elif opcode == MOD:
			self.ac = int(self.dr % self.ac)
			self.pc = self.pc + 1;
		elif opcode == NEG:
			self.ac = int(-int(self.ac))
			self.pc = self.pc + 1;
		elif opcode == INC:
			self.ac = int(int(self.ac) + 1)
			self.pc = self.pc + 1;
		elif opcode == DEC:
			self.ac = int(int(self.ac) - 1)
			self.pc = self.pc + 1;
		elif opcode == AND:
			self.ac = int(self.dr & self.ac)
			self.pc = self.pc + 1;
		elif opcode == OR:
			self.ac = int(self.dr | self.ac)
			self.pc = self.pc + 1;
		elif opcode == NOT:
			self.ac = int(~int(self.ac))
			self.pc = self.pc + 1;
		elif opcode == XOR:
			self.ac = int(self.dr ^ self.ac)
			self.pc = self.pc + 1;
		elif opcode == SHL:
			self.ac = int(self.dr << self.ac)
			self.pc = self.pc + 1;
		elif opcode == SHR:
			self.ac = int(self.dr >> self.ac)
			self.pc = self.pc + 1;
		elif opcode == EQ:
			self.ac = 1 if self.dr == self.ac else 0
			self.pc = self.pc + 1;
		elif opcode == NE:
			self.ac = 1 if self.dr != self.ac else 0
			self.pc = self.pc + 1;
		elif opcode == LT:
			self.ac = 1 if self.dr <  self.ac else 0
			self.pc = self.pc + 1;
		elif opcode == LE:
			self.ac = 1 if self.dr <= self.ac else 0
			self.pc = self.pc + 1;
		elif opcode == GT:
			self.ac = 1 if self.dr >  self.ac else 0
			self.pc = self.pc + 1;
		elif opcode == GE:
			self.ac = 1 if self.dr >= self.ac else 0
			self.pc = self.pc + 1;
		elif opcode == BR:
			self.pc = self.memory[self.pc + 1]
		elif opcode == BRN:
			if self.ac < 0:
				self.pc = self.memory[self.pc + 1]
			else:
				self.pc = self.pc + 2;
		elif opcode == BRZ:
			if self.ac == 0:
				self.pc = self.memory[self.pc + 1]
			else:
				self.pc = self.pc + 2;
		elif opcode == BRP:
			if self.ac > 0:
				self.pc = self.memory[self.pc + 1]
			else:
				self.pc = self.pc + 2;
		elif opcode == ENT:
			self.sp = self.sp - self.memory[self.pc + 1]
			self.pc = self.pc + 2;
		elif opcode == CALL:
			address = self.memory[self.pc + 1]
			nargs   = self.memory[self.pc + 2]
			args = []
			for i in range(nargs):
				args.append(self.pop())
			self.push(self.fp)
			self.push(self.pc + 3)
			self.fp = self.sp
			counter = nargs - 1
			while counter >= 0:
				self.push(args[counter])
				counter = counter - 1
			self.pc = address
		elif opcode == RET:
			value   = self.ac
			self.sp = self.fp
			address = self.pop()
			self.fp = self.pop()
			self.push(value)
			self.pc = address
		elif opcode == CONST:
			self.ac = self.memory[self.pc + 1]
			self.pc = self.pc + 2;
		elif opcode == MVA:
			self.dr = self.ac
			self.pc = self.pc + 1;
		elif opcode == MVD:
			self.ac = self.dr
			self.pc = self.pc + 1;
		elif opcode == SWAP:
			temp    = self.ac
			self.ac = self.dr
			self.dr = temp
			self.pc = self.pc + 1;
		elif opcode == PUSH:
			self.push(self.ac)
			self.pc = self.pc + 1
		elif opcode == STA:
			self.memory[self.memory[self.pc + 1]] = self.ac
			self.pc = self.pc + 2
		elif opcode == STR:
			self.memory[self.memory[self.memory[self.pc + 1]]] = self.ac
			self.pc = self.pc + 2
		elif opcode == STO:
			self.memory[self.fp - self.memory[self.pc + 1]] = self.ac
			self.pc = self.pc + 2
		elif opcode == POP:
			self.ac = self.pop();
			self.pc = self.pc + 1
		elif opcode == LDA:
			self.ac = self.memory[self.memory[self.pc + 1]]
			self.pc = self.pc + 2
		elif opcode == LDR:
			self.ac = self.memory[self.memory[self.memory[self.pc + 1]]]
			self.pc = self.pc + 2
		elif opcode == LDO:
			self.ac = self.memory[self.fp - self.memory[self.pc + 1]]
			self.pc = self.pc + 2
		else:
			print(self.memory[self.sp:])
			print("Unknown Opcode {}: at {}.".format(opcode,self.pc))
			exit()

	def run(self):
		if self.is_running == False:
			self.is_running = True
			while self.pc < self.max_memory:
				if self.is_running == False:
					break
				self.execute()
				#print(self.memory[self.sp:])
				'''
				print()
				print("pc:{} dr: {} ac: {} sp: {} fp: {}".format(
					self.pc,self.dr,self.ac,self.sp,self.fp))
				print()
				'''

