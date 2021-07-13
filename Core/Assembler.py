from Core.Utils import *


class Assembler:
	
	def __init__(self,source = ""):
		self.source = source
		self.labels = {} 

	def tokenize(self):
		result = []
		tokens = list(map(lambda x : sanitize(x),(self.source.split("\n"))))
		tokens = list(filter(lambda x: len(x) != 0,tokens))
		tokens = list(map(lambda x : x.split(),tokens))
		return tokens
	
	def pass1(self,tokens = []):
		result = []
		loc = 0
		pc = 0
		while loc < len(tokens):
			token = tokens[loc]
			token[0] = token[0].upper()
			if pc == 0 and loc == 0 and token[0] != "START":
				result.append([START,0])
			if token[0] == "LABEL":
				label = token[1]
				self.labels[label] = pc
			elif token[0] == "ORG":
				token[0] = instructions_opcodes[token[0]]
				token[1] = int(token[1])
				result.append(token)
				##print("{} {}".format(pc,token))
				pc = int(token[1])
			elif token[0] == "DAT":
				token[0] = instructions_opcodes[token[0]]
				token[1] = int(token[1])
				result.append(token)
				##print("{} {}".format(pc,token))
				pc = pc + 1
			elif token[0] == "START":
				if pc == 0 and loc == 0:
					token[0] = instructions_opcodes[token[0]]
					try:
						token[1] = int(token[1])
					except Exception as e:
						token[1] = token[1]
					result.append(token)
				else:
					print("This start \"{}\" command must be at the first line.".format(" ".join(token)))
					exit()
			else:
				arr = []
				if token[0] not in instructions_opcodes:
					print("Invalid Command \"{}\"".format(token[0]))
					exit()
				token[0] = instructions_opcodes[token[0]]
				nargs = instructions_opcodes[token[0]]["nargs"];
				if len(token) - 1 != nargs:
					print("Invalid Number of Operands to Command \"{}\" required {} but got {}.".format(
						 instructions_opcodes[token[0]]["to_str"],nargs,len(token) - nargs))
					exit()
				for value in token:
					try:
						arr.append(int(value))
					except Exception as e:
						arr.append(value)	
				##print("{} {}".format(pc,token))
				result.append(arr)
				pc = pc + len(arr)
			loc = loc + 1
		
		return result
	
	def pass2(self,tokens = []):
		result = []
		loc = 0
		while loc < len(tokens):
			token = tokens[loc]
			arr = []
			for value in token:
				if isinstance(value,str):
					if value in self.labels:
						arr.append(self.labels[value])
					else:
						print("Error: {} is not decalared as label.".format(value))
						exit()
				else:
					arr.append(value)
			result.append(arr)
			loc = loc + 1
		return result
	
	
	def assemble(self):
		tokens = self.tokenize()
		tokens = self.pass1(tokens)
		tokens = self.pass2(tokens)
		return tokens
		
	def to_str_code(self):
		str_code = ""
		code = self.assemble()
		str_code = "\n".join(list(map(lambda x : " ".join(list(map(lambda y : str(y),x))),code)))
		str_code = str_code.strip()
		return str_code
	
	@staticmethod
	def to_str_disassemble(source = ""):
		str_code = ""
		tokens = copy.deepcopy(Assembler(source).tokenize())
		for token in tokens:
			token[0] = int(token[0])
			if token[0] not in instructions_opcodes:
				print("Invalid Command \"{}\"".format(token[0]))
				exit()
			nargs = instructions_opcodes[token[0]]["nargs"];
			if len(token) - 1 != nargs:
				print("Invalid Number of Operands to Command \"{}\" required {} but got {}.".format(
					 instructions_opcodes[token[0]]["to_str"],nargs,len(token) - nargs))
				exit()
			token[0] = instructions_opcodes[token[0]]["to_str"].lower()
			for value in token[1:]:
				try :
					int(value)
				except Exception as e:
					if(isinstance(value,str)):
						print("Error: \"{}\" Not a Number.".format(value))
						exit()
		code = copy.deepcopy(tokens)
		str_code = "\n".join(list(map(lambda x : " ".join(list(map(lambda y : str(y),x))),code)))
		str_code = str_code.strip()
		return str_code

	@staticmethod
	def object(source = ""):
		str_code = ""
		source = Assembler.to_str_disassemble(source)
		code = Assembler(source).assemble()
		tokens = copy.deepcopy(code)
		loc = 0
		pc  = 0
		while loc < len(tokens):
			token = tokens[loc]
			if token[0] == ORG:
				pc = token[1]
			elif token[0] == DAT:
				str_code = str_code + "{}  {}\n".format(pc,token[1])
				pc  = pc + 1
			else:
				counter = 0
				while counter < len(token):
					if counter == 0:
						str_code = str_code + "{}  {} ; {}\n".format(
							pc,token[counter],instructions_opcodes[token[0]]["to_str"].lower())
					else:
						str_code = str_code + "{}  {}\n".format(pc,token[counter])
					pc     = pc + 1
					counter = counter + 1
			loc = loc + 1
		return str_code
