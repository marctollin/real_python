import csv
import os
import sys
import argparse
my_path="~/real_python/"


parser = argparse.ArgumentParser()
parser.add_argument('-i')
parser.add_argument('-o')
parser.add_argument('-r')


args=parser.parse_args()
args.r=int(args.r)


with open(args.i,"rb") as data:
	data_reader = csv.reader(data)
	next(data_reader)
	print data_reader[1:100]


with open(args.i) as data:
	data_reader = csv.reader(data)
	numrows =sum(1 for row in data_reader)
	totalchunks=int(numrows/args.r)
	if numrows % args.r !=0:
		totalchunks=totalchunks+1

for chunk in range(totalchunks):
	print chunk
	with open(args.o+'_'+str(chunk)+'.csv',"w") as data_out, open(args.i) as data:
		data_writer = csv.writer(data_out)
		for i,row in enumerate(csv.reader(data)):
			if i==0:
				data_writer.writerow(row)
			if args.r*chunk< i <= args.r+args.r*chunk:
				data_writer.writerow(row)

