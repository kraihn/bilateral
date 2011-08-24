#! /usr/bin/env python
import sys

def main():
	lines = int(sys.argv[1])
	
	input = []
	
	for i in range(0,lines):
		input.append(sys.stdin.readline().replace('\n', ''))
		
	print input

if __name__ == '__main__':
	main()
