"""Dataset with 'Torque teno sus virus k2a' sequences.

A dataset with 10 'Torque teno sus virus k2a' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/torque_teno_sus_virus_k2a.fasta.gz", relative=True)
sys.modules[__name__] = ds