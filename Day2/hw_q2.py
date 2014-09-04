#!/usr/bin/env python
import pandas as pd 
import matplotlib.pyplot as plt

female_10   = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
female_11   = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
female_12   = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
female_13   = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
female_14A  = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
female_14B  = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
female_14C  = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
female_14D  = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
male_10     = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
male_11     = "/Users/cmdb/data/results/SRR072894_clout/genes.fpkm_tracking"
male_12     = "/Users/cmdb/data/results/SRR072895_clout/genes.fpkm_tracking"
male_13     = "/Users/cmdb/data/results/SRR072896_clout/genes.fpkm_tracking"
male_14A    = "/Users/cmdb/data/results/SRR072897_clout/genes.fpkm_tracking"
male_14B    = "/Users/cmdb/data/results/SRR072899_clout/genes.fpkm_tracking"
male_14C    = "/Users/cmdb/data/results/SRR072901_clout/genes.fpkm_tracking"
male_14D    = "/Users/cmdb/data/results/SRR072903_clout/genes.fpkm_tracking"

df1 = pd.read_table(female_10)
df2 = pd.read_table(female_11)
df3 = pd.read_table(female_12)
df4 = pd.read_table(female_13)
df5 = pd.read_table(female_14A)
df6 = pd.read_table(female_14B)
df7 = pd.read_table(female_14C)
df8 = pd.read_table(female_14D)

#print df1["gene_short_name"].head 
#print df1.str.extract("Sxl")

df_female=[df1, df2, df3, df4, df5, df6, df7, df8]

Sxl_genes = df1["gene_short_name"]== "Sxl"

for i in df_female:
    open (i)
    while True:
            line=f.readline()
            if "Sxl" in line:
                fields = line.rstrip("\r\n").split("\t")
                break
