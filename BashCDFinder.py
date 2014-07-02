#!/usr/bin/env python

''' 
Copyright 2014, David Pany

	BashCDFinder v1.0 - 07/01/14
	
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
This script reads a bash history text file as an argument, finds a specified 
command, and prints preceeding "cd" commands so you can find the working
directory during command execution
	
'''
import sys
import collections
print

executeTF = True

#check argument input
if len(sys.argv) == 1 or sys.argv[1] == "-h":
	print """
	This script reads a bash history text file as an argument, finds a specified 
	command, and prints preceeding "cd" commands so you can find the working
	directory during command execution
	
	Usage:
		BashCDFinder.py .bash_history
	"""
	executeTF = False

#if there is an argument that is not -h
if executeTF:
	try:
		input_file = open(sys.argv[1])
	#in case the argument is not a valid file path	
	except:
		executeTF = False
		print "We could not find the specified file, please try again and check your path. "
		executeTF = False

#if the file path is valid
if executeTF:		
	history_input = raw_input('How many preceeding "cd" commands would you like to display? ')
	acceptable_length = False
	while not acceptable_length:
		#tests to see if history_length is between 1 and 50 and a valid integer
		try:
			if  1 <= int(history_input)  <= 50:
				acceptable_length = True
			else:
				history_input = raw_input('please enter an integer between 1 and 50 for how many "cd" commands you would like to display: ')
		except:
			history_input = raw_input('please enter an integer between 1 and 50 for how many "cd" commands you would like to display: ')
	
	history_length = int(history_input)
	CD_deque = collections.deque(history_length*"",history_length)

#if arguments and file path are valid
if executeTF:
	#what command would the user like to search for?
	command = raw_input('What command would you like to see "cd" history for? ')
	print
	read_string = input_file.readline()
	while read_string:
		
		if read_string[:2] == "cd":
			CD_deque.append(read_string)
		
		#if the command entered matches the beginning of the line read
		if command == read_string[:len(command)]:
			for i in CD_deque:
				if i != "":
					print i[:-1]
			print
			print read_string[:-1]
			
			CD_deque = collections.deque(history_length*"",history_length)
			print
		
		read_string = input_file.readline()

	input_file.close()