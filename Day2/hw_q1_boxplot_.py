#!/usr/bin/env python
import pandas as pd 
import matplotlib.pyplot as plt

#male data
cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df = pd.read_table(cufflinks_output)

#print df. describe() 
male_low = df.sort("FPKM", ascending=False)[1:4746] #only for these rows
male_med = df.sort("FPKM", ascending=False)[4746:9491] #only for these rows
male_hi  = df.sort("FPKM", ascending=False)[9491:14237] #only for these rows


#female data
cufflinks_output2= "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output2)

#print df2. describe() 
female_low = df2.sort("FPKM", ascending=False)[1:8158] #only for these rows
female_med = df2.sort("FPKM", ascending=False)[8158:16315] #only for these rows
female_hi  = df2.sort("FPKM", ascending=False)[16315:24473] #only for these rows

a_list =[]
for i in male_low["FPKM"], male_med["FPKM"], male_hi["FPKM"], female_low["FPKM"], female_med["FPKM"], female_hi["FPKM"]:
    a_list.append(i)


plt.boxplot(a_list)
plt.ylim(-5,500)
plt.ylabel ("FPKN")
plt.xlabel ("MALE (#1-3 =low/med/hi)             " + "FEMALE (#4-6 =low/med/hi)")
plt.savefig("boxplot.png")




#male data
#cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
#df = pd.read_table(cufflinks_output)
#df_sort = df.sort("FPKM", ascending=False)
#print df. describe() 
#male_low = df_sort ["FPKM"] [1:4746] #only for these rows
#male_med = df_sort ["FPKM"] [4746:9491] #only for these rows
#male_hi  = df_sort ["FPKM"] [9491:14237] #only for these rows


#female data
#cufflinks_output2= "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
#df2 = pd.read_table(cufflinks_output2)
#df2_sort = df2.sort("FPKM", ascending=False)
#print df2. describe() 
#female_low = df2_sort ["FPKM"] [1:8158] #only for these rows
#female_med = df2_sort ["FPKM"] [8158:16315] #only for these rows
#female_hi  = df2_sort ["FPKM"] [16315:24473] #only for these rows
