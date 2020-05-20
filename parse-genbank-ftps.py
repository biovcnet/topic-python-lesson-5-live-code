#!/usr/bin/env python3

import sys

genomes = []

for line in open(sys.argv[1], "r"): #use sys library to read in a single file entry
	genomes.append(line.strip()) #assumes a single column of unique identifiers added to search list

bigdict = {}

for line in open("assembly_summary_genbank.txt", "r"): #parse the GenBank text file
	if line[0] != "#": #skip the header lines
		line = line.strip() #remove trailing \n character
		data = line.split("\t") #create a list split on \t 
		#select the appropriate index values that have the uniq identifier and the target output
		#bigdict[data[15]] = data[19]  
		bigdict[data[5]] = data[19]
		

outfile1 = open("matched.FTP-calls.txt", "w") #assign an outfile with correct matches
outfile2 = open("unmatched-ref-ids.tmp", "w") #assign an outfile with failed matches

for i in genomes: #iterate through the search list
	#using the try-except formatting to search within the dictionary. if no matching key
	#we assume that the ID is not correctly in the text file
	#record ID in the failed matches outfile
	try:
		outfile1.write("wget "+str(bigdict[i])+"/*_genomic.fna.gz"+"\n")
	except KeyError:
		outfile2.write(str(i)+"\n")
