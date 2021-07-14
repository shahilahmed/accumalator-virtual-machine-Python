NAME    = "Accumalator Virtual Machine with Assembler"
VERSION = "v0.4.0"
AUTHOR  = "Md Shahil Ahmed"

HALT  =  0
NOP   =  1
INP   =  2
OUT   =  3
SCAN  =  4
PRINT =  5

ADD   =  6
SUB   =  7
MUL   =  8
DIV   =  9
MOD   = 10
NEG   = 11
INC   = 12
DEC   = 13

AND   = 14
OR    = 15
NOT   = 16
XOR   = 17
SHL   = 18
SHR   = 19

EQ    = 20
NE    = 21
LT    = 22
LE    = 23
GT    = 24
GE    = 25

BR    = 26
BRN   = 27
BRZ   = 28
BRP   = 29
ENT   = 30
CALL  = 31
RET   = 32

BRT   = BRP
BRF   = BRZ

PUSH  = 33
STA   = 34
STR   = 35
STO   = 36

POP   = 37
LDA   = 38
LDR   = 39
LDO   = 40

CONST = 41
MVA   = 42
MVD   = 43
SWAP  = 44



START = -3
DAT   = -2
ORG   = -1

'''
instructions_opcodes = {
	"HALT"  : HALT, 
	"NOP"   : NOP,
	"INP"   : INP,
	"OUT"   : OUT,
	"SCAN " : SCAN,
	"PRINT" : PRINT,
	
	"ADD"   : ADD,
	"SUB"   : SUB,
	"MUL"   : MUL,
	"DIV"   : DIV,
	"MOD"   : MOD,
	"NEG"   : NEG,
	"INC"   : INC,
	"DEC"   : DEC,
	
	"AND"   : AND,
	"OR"    : OR,
	"NOT"   : NOT,
	"XOR"   : XOR,
	"SHL"   : SHL,
	"SHR"   : SHR,
	
	"EQ"    : EQ,
	"NE"    : NE,
	"LT"    : LT,
	"LE"    : LE,
	"GT"    : GT,
	"GE"    : GE,
	
	"BR"    : BR,
	"BRN"   : BRN,
	"BRZ"   : BRZ,
	"BRP"   : BRP,
	"ENT"   : ENT,
	"CALL"  : CALL,
	"RET"   : RET,
	
	"PUSH"  : PUSH,
	"STA"   : STA,
	"STR"   : STR,
	"STO"   : STO,
	
	"POP"   : POP,
	"LDA"   : LDA,  
	"LDR"   : LDR,
	"LDO"   : LDO,

	"CONST" : CONST,
	"MVA"   : MVA,
	"MVD"   : MVD,
	"SWAP"  : SWAP,
		
	"ORG"   : ORG,
	"DAT"   : DAT,
	"DATA"  : DATA
}
'''
instructions_opcodes = {
        "HALT" : 0,
        HALT : {"opcode" : HALT, "to_str" : "HALT", "nargs" : 0},
        "NOP" : 1,
        NOP : {"opcode" : NOP, "to_str" : "NOP", "nargs" : 0},
        "INP" : 2,
        INP : {"opcode" : INP, "to_str" : "INP", "nargs" : 0},
        "OUT" : 3,
        OUT : {"opcode" : OUT, "to_str" : "OUT", "nargs" : 0},
        "SCAN" : 4,
        SCAN  : {"opcode" : SCAN , "to_str" : "SCAN ", "nargs" : 0},
        "PRINT" : 5,
        PRINT : {"opcode" : PRINT, "to_str" : "PRINT", "nargs" : 0},
        "ADD" : 6,
        ADD : {"opcode" : ADD, "to_str" : "ADD", "nargs" : 0},
        "SUB" : 7,
        SUB : {"opcode" : SUB, "to_str" : "SUB", "nargs" : 0},
        "MUL" : 8,
        MUL : {"opcode" : MUL, "to_str" : "MUL", "nargs" : 0},
        "DIV" : 9,
        DIV : {"opcode" : DIV, "to_str" : "DIV", "nargs" : 0},
        "MOD" : 10,
        MOD : {"opcode" : MOD, "to_str" : "MOD", "nargs" : 0},
        "NEG" : 11,
        NEG : {"opcode" : NEG, "to_str" : "NEG", "nargs" : 0},
        "INC" : 12,
        INC : {"opcode" : INC, "to_str" : "INC", "nargs" : 0},
        "DEC" : 13,
        DEC : {"opcode" : DEC, "to_str" : "DEC", "nargs" : 0},
        "AND" : 14,
        AND : {"opcode" : AND, "to_str" : "AND", "nargs" : 0},
        "OR" : 15,
        OR : {"opcode" : OR, "to_str" : "OR", "nargs" : 0},
        "NOT" : 16,
        NOT : {"opcode" : NOT, "to_str" : "NOT", "nargs" : 0},
        "XOR" : 17,
        XOR : {"opcode" : XOR, "to_str" : "XOR", "nargs" : 0},
        "SHL" : 18,
        SHL : {"opcode" : SHL, "to_str" : "SHL", "nargs" : 0},
        "SHR" : 19,
        SHR : {"opcode" : SHR, "to_str" : "SHR", "nargs" : 0},
        "EQ" : 20,
        EQ : {"opcode" : EQ, "to_str" : "EQ", "nargs" : 0},
        "NE" : 21,
        NE : {"opcode" : NE, "to_str" : "NE", "nargs" : 0},
        "LT" : 22,
        LT : {"opcode" : LT, "to_str" : "LT", "nargs" : 0},
        "LE" : 23,
        LE : {"opcode" : LE, "to_str" : "LE", "nargs" : 0},
        "GT" : 24,
        GT : {"opcode" : GT, "to_str" : "GT", "nargs" : 0},
        "GE" : 25,
        GE : {"opcode" : GE, "to_str" : "GE", "nargs" : 0},
        "BR" : 26,
        BR : {"opcode" : BR, "to_str" : "BR", "nargs" : 1},
        "BRN" : 27,
        BRN : {"opcode" : BRN, "to_str" : "BRN", "nargs" : 1},
        "BRZ" : 28,
        "BRF" : 28,
        BRZ : {"opcode" : BRZ, "to_str" : "BRZ", "nargs" : 1},
        "BRP" : 29,
        "BRT" : 29,
        BRP : {"opcode" : BRP, "to_str" : "BRP", "nargs" : 1},
        "ENT" : 30,
        ENT : {"opcode" : ENT, "to_str" : "ENT", "nargs" : 1},
        "CALL" : 31,
        CALL : {"opcode" : CALL, "to_str" : "CALL", "nargs" : 2},
        "RET" : 32,
        RET : {"opcode" : RET, "to_str" : "RET", "nargs" : 0},
        "PUSH" : 33,
        PUSH : {"opcode" : PUSH, "to_str" : "PUSH", "nargs" : 0},
        "STA" : 34,
        STA : {"opcode" : STA, "to_str" : "STA", "nargs" : 1},
        "STR" : 35,
        STR : {"opcode" : STR, "to_str" : "STR", "nargs" : 1},
        "STO" : 36,
        STO : {"opcode" : STO, "to_str" : "STO", "nargs" : 1},
        "POP" : 37,
        POP : {"opcode" : POP, "to_str" : "POP", "nargs" : 0},
        "LDA" : 38,
        LDA : {"opcode" : LDA, "to_str" : "LDA", "nargs" : 1},
        "LDR" : 39,
        LDR : {"opcode" : LDR, "to_str" : "LDR", "nargs" : 1},
        "LDO" : 40,
        LDO : {"opcode" : LDO, "to_str" : "LDO", "nargs" : 1},
        "CONST" : 41,
        CONST : {"opcode" : CONST, "to_str" : "CONST", "nargs" : 1},
        "MVA" : 42,
        MVA : {"opcode" : MVA, "to_str" : "MVA", "nargs" : 0},
        "MVD" : 43,
        MVD : {"opcode" : MVD, "to_str" : "MVD", "nargs" : 0},
        "SWAP" : 44,
        SWAP : {"opcode" : SWAP, "to_str" : "SWAP", "nargs" : 0},
        "ORG" : -1,
        ORG : {"opcode" : ORG, "to_str" : "ORG", "nargs" : 1},
        "DAT" : -2,
        DAT : {"opcode" : DAT, "to_str" : "DAT", "nargs" : 1},
        "START" : -3,
        START : {"opcode" : START, "to_str" : "START", "nargs" : 1}
}












