from daycare import daycare
from common import inputString

def main():
	care = daycare("Test Care", "../input/pigeonNames.json", "../input/help.txt")
	care.do("help")

	while True:
		try:
			if care.do(input(inputString())) == 0:
				break
		except EOFError:
				print("\n")
				break

main()
