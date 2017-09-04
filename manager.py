	#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import argparse

def createParser ():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers (dest='command')

	read_parser = subparsers.add_parser ('read')

	add_parser = subparsers.add_parser ('add')
	add_parser.add_argument('-t', '--task', nargs='+', required=True)

	return parser

def run_read ():
	print('Читаем записи из файла')

if __name__ == "__main__":
	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])

	if namespace.command == "read":
		run_read()
	elif namespace.command == "add":
		taskName, taskDate = namespace.task[0], namespace.task[1]
		print("Task: " + taskName + " - " + taskDate)
	else:
		print("Usage: \n")
		print("manager.py add -t \"taskName\" taskDate")