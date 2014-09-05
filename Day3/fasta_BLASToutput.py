#!/usr/bin/env python


""""
Day 3 lunch exercise
"""

import sys

class BlastOutReader(object):
    def __init__(self, file):    
        self.file=file
        self.last_sid = None
    def next (self):

#        if self.last_sid is None: 
#            line = sys.stdin.readline()     
#            assert line.startswith(">")     
#            sid = line[1:].rstrip ("\r\n")
#        else:
#            sid = self.last_sid
                
        sequences =[]
        while True:
            line = sys.stdin.readline() 
            if line == "" and not sequences: 
                raise StopIteration 
            elif line.startswith("Query=") or line == "":    
                sid = line[6:].rstrip ("\n")[:25]
                parts=line.split(" ")
                break                   
          
        sequence= "".join(sequences)   
        return sid, sequence 
    def __iter__(self):
        return self
        
#sid = line[6:].rstrip ("\r\n")
#sequences.append(line.strip()) 