#!/usr/bin/env python3

import sys

genomes = []
#for line in open("GORG-TROPICS-SAGS.50.ids", "r"):
#for line in open("PATRIC-ref-TAXON.ids", "r"):
for line in open(sys.argv[1], "r"):
	genomes.append(line.strip())

bigdict = {}

for line in open("assembly_summary_genbank.txt", "r"):
	if line[0] != "#":
		line = line.strip()
		data = line.split("\t")
		#bigdict[data[15]] = data[19]
		bigdict[data[5]] = data[19]
		

outfile1 = open("matched.FTP-calls.txt", "w")
outfile2 = open("unmatched-ref-ids.tmp", "w")

for i in genomes:
	try:
		outfile1.write("wget "+str(bigdict[i])+"/*_genomic.fna.gz"+"\n")
	except KeyError:
		outfile2.write(str(i)+"\n")
