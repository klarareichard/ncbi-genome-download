#!/usr/bin/python

import argparse
import sys
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument("cores", help = "Enter the number of cores, you want to use for downloading here", type = int)
args = parser.parse_args()

quater_cores = args.cores/4

print(args.cores)
print(quater_cores)
string = 'screen -mdS fasta_files_bacteria ncbi-genome-download bacteria -o /Users/klara/ncbi_data --format fasta --parallel '+ str(quater_cores)
print(string)

call(string, shell = True)
call(['screen -mdS gff_files_bacteria ncbi-genome-download bacteria -o /Users/klara/ncbi_data --format gff --parallel ' +str(quater_cores)], shell = True)
call(['screen -mdS fasta_files_archaea ncbi-genome-download archaea -o /Users/klara/ncbi_data --format fasta --parallel ' +str(quater_cores)], shell = True)
call(['screen -mdS gff_files_archaea ncbi-genome-download archaea -o /Users/klara/ncbi_data --format gff --parallel ' +str(quater_cores)], shell = True)
#print(args.echo)



