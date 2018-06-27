""",------------------------------,
  /		Phone Number Extractor   /
 /	Author: Jacob Clark			/
/______________________________/
"""

import re
import io

def extractor(line):
	"""Recieves a string that ends in a newline character.
	Returns a phone number (with no formatting)"""
	num = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
	if len(num):
		phnum = re.sub("\D", "", num[0])
		if len(phnum) > 9:
			if phnum is not None:
				return phnum

def main():
	print('Type the name of the text file you would like to open. It must exist inside this directory.')
	fname = input()
	numlist = []
	try:
		with io.open(fname,'r',encoding='ascii',errors='ignore') as infile:
			data = infile.readlines()
			for line in data:
				numlist.append(extractor(line))
		
		print("Enter a name for your output file.")
		ofile = input()
		with io.open(ofile,'w',encoding='ascii',errors='ignore') as outfile:
			for num in numlist:
				if num is not None:
					outfile.write(str(num) + '\n')
	except IOError:
		print('File not found.')
		return 0
	
	
main()
