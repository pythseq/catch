"""Dataset with 'European bat 1 lyssavirus' sequences.

A dataset with 95 'European bat 1 lyssavirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/european_bat_1_lyssavirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
