#!/usr/bin/env python

#understanding the .SAM format - use the following url. to help define the optional fields/columns http://biobits.org/samtools_primer.html#Tutorial
converted_file="/Users/cmdb/data/day1/converted_file.sam"

f = open (converted_file)

nl=0
while True: 
    line = f.readline()
    nl = nl + 1
    if not line:
        break
        
print nl         



counter = 0
for line in f:
    if "NH:i" not in line: 
        print "Invalid criteria"
        break
        
    if "NH:i:1" in line:
        counter = counter +1
print counter
