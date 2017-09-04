#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers (dest='command')

    read_parser = subparsers.add_parser ('read')
    read_parser.add_argument('-r', '--read', default='notes.txt')

    add_parser = subparsers.add_parser ('add')
    add_parser.add_argument('-a', '--add', nargs='+', default='none')

    return parser

def run_add ():
	print('Добавляем запись')

def run_read ():
	print('Читаем записи из файла')

if __name__ == "__main__":
	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])

	if namespace.command == "read":
		run_read()
	elif namespace.command == "add":
		run_add()
	else:
		print("нет такой команды")