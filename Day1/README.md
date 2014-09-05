cmdb-bootcamp-homework
====================== 

LUNCH EXERCISES:
Basic
1) How many lines?
	wc dmel-all-r5.57-removeFASTA.gff
153048099 lines

2)How many lines deal with the gene Sxl
	 grep -e "Sxl" dmel-all-r5.57-removeFASTA.gff | wc
6470 lines

3) What are the unique features:
	BAC_cloned_genomic_insert
	CDS
	DNA_motif
	RNAi_reagent
	TF_binding_site
	TSS
	breakpoint
	chromosome
	chromosome_arm
	chromosome_band
	complex_substitution
	deletion
	enhancer
	exon
	exon_junction
	five_prime_UTR
	gene
	insertion_site
	insulator
	intron
	mRNA
	match
	match_part
	mature_peptide
	miRNA
	modified_RNA_base_feature
	ncRNA
	oligonucleotide
	origin_of_replication
	orthologous_region
	orthologous_to
	pcr_product
	point_mutation
	polyA_site
	pre_miRNA
	protein
	protein_binding_site
	pseudogene
	rRNA
	region
	regulatory_region
	repeat_region
	rescue_fragment
	sequence_variant
	silencer
	snRNA
	snoRNA
	syntenic_region
	tRNA
	tandem_repeat
	three_prime_UTR
	transposable_element
	transposable_element_insertion_site
	uncharacterized_change_in_nucleotide_sequence

4) How many of each feature type? (see file /Users/cmdb/data/day1/gff/column__features.txt)
5) push file into repository on Github