#!/usr/bin/env python


""""
Day3 Lunch exercise
"""

import sys
from fasta_BLASToutput import BlastOutReader
reader = BlastOutReader(sys.stdin)        

for sid, sequence in reader:
    print sid, sequence