#!/usr/bin/env python

"""
 Extract the 100 longest assembled transcripts from your cufflinks output (transcripts.gtf) into FASTA format
"""

# Module import section

import sys
import operator

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

# replication step

list_sequences = []

for sid, sequences in reader:

    seq_list.append(sequences)

seq_sort = sorted(seq_list)

one_hundred_seq = seq_sort[:100]