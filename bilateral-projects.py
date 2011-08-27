#! /usr/bin/env python
import sys

def main():
	
	# Get number of projects being presented
	lines = int(sys.stdin.readline().replace('\n', ''))
	
	# Initialize lists
	stockholm = []	
	london = []
	invitees = []
	
	# Parse the input
	for i in range(0,lines):
		line = sys.stdin.readline().replace('\n', '').split(' ')			
		stockholm.append(int(line[0]))
		london.append(int(line[1]))

	# Determine invitee list
	for i in range(0, lines):
		
		# If an employee is already attending, default to them
		if invitees.count(stockholm[i]) > 0 or invitees.count(london[i]) > 0:
			pass
		
		# If the Stockholm employee works on more projects, select that employee
		elif stockholm.count(stockholm[i]) > london.count(london[i]):
			invitees.append(stockholm[i])
			
		# If the London employee works on more projects, select that employee
		elif stockholm.count(stockholm[i]) < london.count(london[i]):
			invitees.append(london[i])
		
		# Select the friend if possible
		elif stockholm[i] == 1009:
			invitees.append(1009)
			
		# Default to the London employee
		else:
			invitees.append(london[i])
	
	# Print results
	print len(invitees)		# Number of employees invited
	for i in invitees:		# Employee numbers
		print i

if __name__ == '__main__':
	main()
