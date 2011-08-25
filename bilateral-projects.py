#! /usr/bin/env python
import sys


class Project():
	pass
	

def main():
	lines = int(sys.stdin.readline().replace('\n', ''))
	
	items = []	
	for i in range(0,lines):
		line = sys.stdin.readline().replace('\n', '').split(' ')
				
		item = Project()
		item.id = i
		item.stockholm = line[0]
		item.london = line[1]
		
		items.append(item)
		#print str(item.id) + ' ' + item.stockholm + ' ' + item.london
		
	#print items

if __name__ == '__main__':
	main()
