from Core.VirtualMachine import *

def cmd_assemble(path = ""):
	if file_exists(file_path_full(path)):
		file = file_path_full(path)
		source = file_get_contents(file)
		filename = path.split("\\")[-1].split(".")[0]
		str_code = Assembler(source).to_str_code()
		str_code = str_code.strip()
		file_put_contents(filename + ".code",str_code)
		print("{} has been assembled to {} sucessfully.".format(path,filename + ".code"))		

def cmd_disassemble(path = ""):
	if file_exists(file_path_full(path)):
		file = file_path_full(path)
		source = file_get_contents(file)
		filename = path.split("\\")[-1].split(".")[0]
		str_code = Assembler.to_str_disassemble(source)
		str_code = str_code.strip()
		file_put_contents(filename + "_disassemble.asm",str_code)
		print("{} has been disassembled to {} sucessfully.".format(path,filename + "_disassemble.asm"))

def cmd_object(path = ""):
	if file_exists(file_path_full(path)):
		file = file_path_full(path)
		source = file_get_contents(file)
		filename = path.split("\\")[-1].split(".")[0]
		str_code = Assembler.object(source)
		str_code = str_code.strip()
		file_put_contents(filename + ".object",str_code)
		print("{} has been written to {} sucessfully.".format(path,filename + ".object"))

def load_object(path = ""):
	if file_exists(file_path_full(path)):
		file = file_path_full(path)
		source = file_get_contents(file)
		tokens = list(map(lambda x : sanitize(x),(source.split("\n"))))
		tokens = list(filter(lambda x: len(x) != 0,tokens))
		tokens = list(map(lambda x : list(map(lambda y : int(y),x.split())),tokens))
		return tokens
'''
cmd_assemble("asm\\fibo.asm")
##cmd_disassemble("fibo.code")
cmd_object("fibo.code")
##print(load_object("fibo.object"))

vm = VirtualMachine()
vm.load(load_object("fibo.object"))
vm.run()
'''
##print(instructions_opcodes[MVD])


def print_info():
	print()
	print("{} {} {}".format(NAME,VERSION,AUTHOR))
	print()
	print("usage: python main.py")
	print()

def main():
	print_info()
	argv = sys.argv[1:] # Link: https://stackoverflow.com/questions/509211/understanding-slice-notation
	if len(argv) >= 1:
		command = argv.pop(0)
		##argv = list(map(lambda x : file_path_full(x),argv))
		argv = list(filter(lambda x : file_exists(file_path_full(x)),argv))
		if command == "-help":	
			print()
			print("python main.py -X path\file_1.ext path\file_2.ext path\file_n.ext")
			print()
			print("Here -X is given below")
			print()
			print(" -h : help")
			print(" -a : generate assembly byte(*.code)")
			print(" -d : generate source assembly code(*.asm) from assembly byte code(*.code)")
			print(" -o : generate object code with extension(*.object)")
			print(" -r : take object code(*.object) and run the file")
			print(" -m : make and run the file")
			print()
		if command == "-a":	
			for path in argv:
				cmd_assemble(path)
		elif command == "-d":	
			for path in argv:
				cmd_disassemble(path)
		elif command == "-o":	
			for path in argv:
				cmd_object(path)
		elif command == "-r":	
			for path in argv:
				vm = VirtualMachine()
				vm.load(load_object(path))
				vm.run()
		elif command == "-m":	
			for path in argv:
				filename = path.split("\\")[-1].split(".")[0]
				cmd_assemble(path)
				cmd_object(filename + ".code")
				print()
				vm = VirtualMachine()
				vm.load(load_object(filename + ".object"))
				vm.run()
		else:
			print("usage: python main.py -help")
	else:
		print("usage: python main.py -help")
	
if __name__ == "__main__":
	main()

