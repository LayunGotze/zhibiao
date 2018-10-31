import sys
def clear(inp, oup):
	oup = open(oup, 'w')
	with open(inp, 'r') as inp:
		for oline in inp:
			line = oline.split('[')[0].strip()
			if line and line[-1] == '*': continue
			oup.write(oline)
if __name__ == '__main__':
	clear(sys.argv[1], sys.argv[2])