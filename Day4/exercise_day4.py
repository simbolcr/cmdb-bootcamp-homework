#!/usr/bin/env python
import pandas as pd 

df=pd.read_csv("transcripts.gtf", index_col=False, header=None, sep='\t|\s+')

#I then looked at a subset of the file using head and transposed it to look at all the column names
#df.head().T

#It looked like the first few columns of the data file are being read as the "index" rather than data. So I need to define those columns as being part of the data and not an index (otherwise known as the title columns). To do so I needed to "reset" the index. This issue is fixed if I just set the pd.read_csv to consider the indoex_col=False which I added to df one line #4
#df2=df.reset_index() 

#I made a list of the columns that I wanted to keep in my new file. There are two ways to do this if I want more than one column. I can list a range or specify specific columns. AND I can put them together. 
keep_col= range(2,5) + [6] + range(10,16)
#to see the output. Just enter keep_col in ipython and press enter:
# In [68]: keep_col
# Out[68]: [2, 3, 4, 6, 10, 11, 12, 13, 14, 15]

#.ix means to look at the index. Within the bracket in the first group you define how many lines you want to see. In this case, we are looking at the first 5 lines. Pandas is inclusive so it will include that fifth line number but python normally would not. Another way we could do this is to write [2:5] which would show lines 2 through 5. The second group in the bracket indicates which columns you want. Normally you would put numbers. However, since I already defined the variable keep_col as a list of column numbers that I wanted from the file, I can just use the variable instead of listing each column I want. 
#df.ix[:5,keep_col]


#if i want to paste more than one line of text from this TM file into ipython, I can use %paste <ENTER> and it will paste the lines into the command line/terminal. 


#But ultimately I want all the lines in the file, so I just keep that first section open-ended
df2 = df.ix[:,keep_col]

#I ultimately want to be able to just pull out the lines that include "transcript" in column 2. 
df2.ix[df2[2] == 'transcript']


#________________________________________________________________
#________________________________________________________________
#________________________________________________________________
#If I want to make a copy of a file I just do the following:
#df3 = df2.copy()

#If I want to create a boolen to find the lines that have a "+" in column 6 which will indicate positive strands
#In: df2[6] == '+'
#Out: 
#0      True
#1      True
#2      True
#3      True
#4      True
#5      True
#6      True
#7      True
#8      True
#9      True
#10     True
#11     True
#12    False
#13    False
#14    False
#Name: 6, Length: 215864, dtype: bool <----- Column 6 data, 215000 lines, and it is a bool type!

#Here is a way to see the answers without needing to see the index:
#In: (df2[6] == 'transcript').values
#Out: array([ True, True, True, ..., False,  False, False], dtype=bool)


#Here is a way to add a column onto the end of the copied file d3 that is named "Cmoney"...that addes 250 integers to the number found in column 3. See below for the output.
#In [85]: df3['Cmoney'] = df3[3] + 250

#In [86]: df3.head()
#Out[86]: 
#            2     3     4  6             10              11           12  \
#0  transcript  7529  9484  +  transcript_id  "FBtr0300689";         FPKM   
#1        exon  7529  8116  +  transcript_id  "FBtr0300689";  exon_number   
#2        exon  8193  9484  +  transcript_id  "FBtr0300689";  exon_number   
#3  transcript  7529  9484  +  transcript_id  "FBtr0330654";         FPKM   
#4        exon  7529  8116  +  transcript_id  "FBtr0330654";  exon_number   

#                13    14               15  Cmoney  <---- NOTE THIS LAST COLUMN! (7529+250=7779)
#0  "0.0000025392";  frac      "0.000009";    7779  
#1             "1";  FPKM  "0.0000025392";    7779  
#2             "2";  FPKM  "0.0000025392";    8443  
#3  "0.0005066557";  frac      "0.001831";    7779  
#4             "1";  FPKM  "0.0005066557";    7779 

#In : df3.groupby(6).head()
#Out: 
#                 2         3         4  6             10              11  \
#0       transcript      7529      9484  +  transcript_id  "FBtr0300689";   
#1             exon      7529      8116  +  transcript_id  "FBtr0300689";   
#2             exon      8193      9484  +  transcript_id  "FBtr0300689";   
#3       transcript      7529      9484  +  transcript_id  "FBtr0330654";   
#4             exon      7529      8116  +  transcript_id  "FBtr0330654";   
#12      transcript     25402     59268  -  transcript_id  "FBtr0309225";   
#13            exon     25402     26688  -  transcript_id  "FBtr0309225";   
#14            exon     26766     26964  -  transcript_id  "FBtr0309225";   
#15            exon     27053     27490  -  transcript_id  "FBtr0309225";   
#16            exon     28015     28240  -  transcript_id  "FBtr0309225";   
#154877  transcript  17186112  17203123  .  transcript_id  "FBtr0084079";   
#154878        exon  17186112  17203123  .  transcript_id  "FBtr0084079";   

#                 12               13    14               15    Cmoney  
#0              FPKM  "0.0000025392";  frac      "0.000009";      9234  
#1       exon_number             "1";  FPKM  "0.0000025392";      7866  
#2       exon_number             "2";  FPKM  "0.0000025392";      9234  
#3              FPKM  "0.0005066557";  frac      "0.001831";      9234  
#4       exon_number             "1";  FPKM  "0.0005066557";      7866  
#12             FPKM  "0.0000000000";  frac      "0.000000";     59018  
#13      exon_number             "1";  FPKM  "0.0000000000";     26438  
#14      exon_number             "2";  FPKM  "0.0000000000";     26714  
#15      exon_number             "3";  FPKM  "0.0000000000";     27240  
#16      exon_number             "4";  FPKM  "0.0000000000";     27990  
#154877         FPKM  "0.0638118891";  frac      "0.000868";  17202873  
#154878  exon_number             "1";  FPKM  "0.0638118891";  17202873  



#Numpy is a library (like how Pandas is a library) of functions for math based things, we need to import numpy like we import pandas and name it as a variable we want to use (so that we can avoid writing numpy over and over again, we will instead just type np)
import numpy as np

#to see options for numpy, just type in np.log <TAB> and ipython will show what options I have to use. np.logical <TAB> shows:
#In: np.logical
#np.logical_and  np.logical_not  np.logical_or   np.logical_xor  

#Column 6 in the data is filled with either '+', '-', or '.' but I only want the + or - strand lines. Therefore I set the "true" as '.' which looks like df2[6]=='.' and use "np.logical_not" to get everything that is NOT True - basically, everything that TRUE or "." will be changed to False and everything that is NOT TRUE or in this case all the "+" and "-" will be changed to 
#In: df2.ix[np.logical_not(df2[6]=='.')].tail()
#Out: 
#                2      3      4  6              10              11  \
#215859        exon  14917  19517  +  transcript_id  "FBgn0013687";   
#215860  transcript  12734  14058  -  transcript_id  "FBtr0100888";   
#215861        exon  12734  14058  -  transcript_id  "FBtr0100888";   
#215862  transcript  14058  14130  -  transcript_id  "FBtr0100889";   
#215863        exon  14058  14130  -  transcript_id  "FBtr0100889";   


#In: df2.ix[df2[6]=='-'].head()
#Out: 
#            2      3      4  6              10              11           12  \
#12  transcript  25402  59268  -  transcript_id  "FBtr0309225";         FPKM   
#13        exon  25402  26688  -  transcript_id  "FBtr0309225";  exon_number   
#14        exon  26766  26964  -  transcript_id  "FBtr0309225";  exon_number   
#15        exon  27053  27490  -  transcript_id  "FBtr0309225";  exon_number   
#16        exon  28015  28240  -  transcript_id  "FBtr0309225";  exon_number   



plus_n_minus_strands=df2.ix[np.logical_not(df2[6]=='.')]
minus_strand= df2.ix[df2[6]=='-']
plus_strand= df2.ix[df2[6]=='+']





